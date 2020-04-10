import random
import threading
import copy
import json
import logging.config
from threading import Lock
from collections import defaultdict


class Disease:

    def __init__(self, infection_prob, average_life_span):

        """Represents a disease

            Parameters
            ----------
            infection_prob : float [0.1]
                The probability of a healthy citizen to get infected by a sick citizen
                as a result of a physical meeting
            average_life_span : int
                The average time (number of steps) that the disease is infactius before
                removed (the infected citizen is cured or dead)

            Other Parameters
            ----------------
            is_sick : bool
                By default, the citizen is not infected
            counter : int
                count the number of steps (time)
            """

        self._infection_prob = infection_prob
        self.life_span = abs(int(random.normalvariate(mu=average_life_span, sigma=0.5)))
        self.is_sick = False
        self.counter = 0

    def step(self):

        """Forward the disease one time step"""

        self.counter += 1
        if self.counter >= self.life_span:
            self.is_sick = False

    def infection_prob(self,  citizen):

        """Returns the infection probability.
            TODO: make the infection probability depends on the citizen's properties"""

        if citizen.removed:
            return 0
        return self._infection_prob

    def start(self):

        """The citizen is sick and can infect other citizens"""

        self.is_sick = True


class Citizen:

    def __init__(self, community, _id, disease):

        """Represents a citizen in a community

            Parameters
            ----------
            community : Community
                The community that the citizen belongs to
            _id : int
                The citizen's id
            disease : Disease
                The disease

            Other Parameters
            ----------------
            removed : bool
                If True it indicates that the citizen is cured or dead
            """

        self.id = _id
        self.community = community
        self.disease = disease
        self.removed = False

    def step(self):

        """Forward the citizen one time step"""

        self.community.meet(self)
        if self.disease.is_sick:
            self.disease.step()
            if not self.disease.is_sick:
                self.removed = True

    def sick(self):

        """The citizen is sick and can infect other citizens"""

        if not self.removed:
            self.disease.start()


class Community:

    def __init__(self, num_of_citizens, average_physical_connections,
                 disease, num_of_infected, cliqe_prob):

        """Represents a community of citizens

            Parameters
            ----------
            num_of_citizens : int
                The number of citizens in the community
            average_physical_connections : int
                The average of physical connection that a citizen within
                the community has (the disease  can be spread only by an
                infected citizen making a physical connection with another citizen
            disease : Disease
                The disease
            num_of_infected : int
                The initial number of infected citizens in the community
            cliqe_prob : float
                The probabilty that the physical connections of a citizen
                in the community is a closed clique (equivalent to quarentine)
            """

        self.logger = None
        self.id = -1
        self.citizens = []
        self.citizens_cliqes = []
        self.lock = Lock()
        self.locked = False #TODO: simulate moving of citizens between communities
        self.connections = defaultdict(set)
        self.total_infected = 0
        self.curr_connections = []

        # initializing citizens
        while len(self.citizens) < num_of_citizens:
            self.citizens.append(Citizen(community=self,
                                         _id=len(self.citizens),
                                         disease=Disease(disease._infection_prob,
                                                         disease.life_span)))

        # initializing infected citizens
        infected = random.sample(range(num_of_citizens), int(num_of_infected))
        for citizen in infected:
            self.citizens[citizen].sick()
            self.total_infected += 1

        # divide the citizens to closed cliques and randomly connected
        random.shuffle(self.citizens)
        self.citizens_cliqes = self.citizens[:int(len(self.citizens) * cliqe_prob)]
        self.citizens = self.citizens[int(len(self.citizens) * cliqe_prob):]

        # initializing physical connections
        for citizen in self.citizens:
            __physical_connections = abs(int(random.normalvariate(mu=average_physical_connections, sigma=0.5)))

            # if not already connected to sufficient number of citizens
            if __physical_connections - len(self.connections[citizen.id]) > 0:
                num_of_physical_connections = __physical_connections - len(self.connections[citizen.id])
                num_of_physical_connections = min(num_of_physical_connections, len(self.citizens))
                _physical_connections = random.sample(range(len(self.citizens)), int(num_of_physical_connections))
                if citizen.id in _physical_connections:
                    _physical_connections.remove(citizen.id)
                for cit in _physical_connections:
                    self.connections[citizen.id].add(cit)
                for id in _physical_connections:
                    self.connections[self.citizens[id].id].add(citizen.id) # a connection is mutual

        self.citizens = self.citizens_cliqes + self.citizens

        # initializing cliques of physical connections
        curr_clique = 0
        while curr_clique < len(self.citizens_cliqes):
            self.init_cliques(self.citizens_cliqes[curr_clique:curr_clique + average_physical_connections],
                              average_physical_connections)
            curr_clique += average_physical_connections
            # can be lonely citizens, thats ok

    def set_logger(self, logger):
        self.logger = logger

    def set_id(self, _id):
        self.id = _id

    def init_cliques(self, citizens, average_physical_connections):

        """Initializing closed cliques of physical connection"""

        index = 0
        while index < len(citizens):
            curr_clique_size = abs(int(random.normalvariate(mu=average_physical_connections, sigma=0.5)))
            cliqe = citizens[index:index + curr_clique_size]
            for c in range(len(cliqe) - 1):
                self.connections[self.citizen(c).id] = set()
                for c_2 in range(c+1, len(cliqe[c:])):
                    self.connections[self.citizen(c).id].add(self.citizen(c_2).id)
            index += curr_clique_size

    def citizen(self, c):
        if isinstance(c, Citizen):
            return c
        else:
            return self.citizens[c]

    def meet(self, citizen_1):

        """Simulates meetings between citizen_1 and all of his physical connections"""

        self.lock.acquire()

        for citizen_2 in self.curr_connections[citizen_1.id]:
            if self.citizen(citizen_1).id == self.citizen(citizen_2).id:
                # a citizen cannot meet himself
                continue
            c_2 = self.citizen(citizen_2)

            if citizen_1.disease.is_sick and not c_2.disease.is_sick:
                if random.random() <= citizen_1.disease.infection_prob(c_2):
                    c_2.sick()
                    self.total_infected += 1
            elif not citizen_1.disease.is_sick and c_2.disease.is_sick:
                if random.random() <= c_2.disease.infection_prob(citizen_1):
                    citizen_1.sick()
                    self.total_infected += 1

            if citizen_1.id in self.curr_connections[c_2.id]: # don't need to meet twice
                self.curr_connections[c_2.id].remove(citizen_1.id)

        self.lock.release()

    def step(self):

        """Stepping the community one time unit"""

        self.curr_connections = copy.deepcopy(self.connections)

        class CitizenThread(threading.Thread):
            def __init__(self, citizen):
                super(CitizenThread, self).__init__()
                self.citizen = citizen

            def run(self):
                self.citizen.step()

        threads = [CitizenThread(citizen) for citizen in self.citizens]
        random.shuffle(threads)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        #active_sick = len([citizen for citizen in self.citizens if citizen.disease.is_sick])
        self.logger.info("number of total cases in community " + str(self.id) + " is " + str(self.total_infected))


class Simulator:
    def __init__(self):

        """Simulator of communities of citizens spreading a disease"""

        self.setup_logging()
        self.logger = logging.getLogger()
        self.communities = []

    def setup_logging(self, path="logger_config.json"):
        with open(path, 'rt') as f:
            config = json.load(f)
            logging.config.dictConfig(config)

    def add_community(self, community):
        community.set_logger(self.logger)
        self.communities.append(community)
        community.set_id(len(self.communities))

    def run(self, num_of_steps):
        for step in range(num_of_steps):
            for community in self.communities:
                community.step()
