![Image description](https://i.imgur.com/Y2imFVO.png)

## General info
This project is simple Lorem ipsum dolor generator.
	
## Dependencies
Project is created with:
* Lorem version: 12.3
* Ipsum version: 2.33
* Ament library version: 999
	
## Setup
To run this project, install it locally using npm:

```
$ cd ../lorem
$ npm install
$ npm start
```
## Expample

To run this project, install it locally using npm:

```
import atlantis

dis = atlantis.Disease(infection_prob=0.2, average_life_span=18)
com = atlantis.Community(num_of_citizens=10000, average_physical_connections=10,
                         disease=dis, num_of_infected=10, cliqe_prob=0.9)
sim = atlantis.Simulator()
sim.add_community(com)
sim.run(40)
```

Output:
```
2020-04-10 13:08:54,255 - root - INFO - total cases in community 1 is 13, active cases: 13
2020-04-10 13:08:54,804 - root - INFO - total cases in community 1 is 32, active cases: 32
2020-04-10 13:08:55,331 - root - INFO - total cases in community 1 is 220, active cases: 220
2020-04-10 13:08:55,855 - root - INFO - total cases in community 1 is 947, active cases: 947
2020-04-10 13:08:56,392 - root - INFO - total cases in community 1 is 2025, active cases: 2025
2020-04-10 13:08:56,919 - root - INFO - total cases in community 1 is 2520, active cases: 2520
2020-04-10 13:08:57,496 - root - INFO - total cases in community 1 is 2675, active cases: 2675
2020-04-10 13:08:58,066 - root - INFO - total cases in community 1 is 2731, active cases: 2731
2020-04-10 13:08:58,624 - root - INFO - total cases in community 1 is 2752, active cases: 2752
2020-04-10 13:08:59,163 - root - INFO - total cases in community 1 is 2770, active cases: 2770
2020-04-10 13:08:59,724 - root - INFO - total cases in community 1 is 2778, active cases: 2778
2020-04-10 13:09:00,341 - root - INFO - total cases in community 1 is 2781, active cases: 2781
2020-04-10 13:09:00,990 - root - INFO - total cases in community 1 is 2785, active cases: 2785
2020-04-10 13:09:01,637 - root - INFO - total cases in community 1 is 2787, active cases: 2787
2020-04-10 13:09:02,262 - root - INFO - total cases in community 1 is 2789, active cases: 2789
2020-04-10 13:09:02,852 - root - INFO - total cases in community 1 is 2789, active cases: 2789
2020-04-10 13:09:03,416 - root - INFO - total cases in community 1 is 2790, active cases: 2783
2020-04-10 13:09:04,020 - root - INFO - total cases in community 1 is 2790, active cases: 2771
2020-04-10 13:09:04,597 - root - INFO - total cases in community 1 is 2791, active cases: 2691
2020-04-10 13:09:05,179 - root - INFO - total cases in community 1 is 2791, active cases: 2306
2020-04-10 13:09:05,776 - root - INFO - total cases in community 1 is 2792, active cases: 1562
2020-04-10 13:09:06,350 - root - INFO - total cases in community 1 is 2793, active cases: 753
2020-04-10 13:09:06,927 - root - INFO - total cases in community 1 is 2793, active cases: 298
2020-04-10 13:09:07,492 - root - INFO - total cases in community 1 is 2793, active cases: 129
2020-04-10 13:09:08,027 - root - INFO - total cases in community 1 is 2793, active cases: 68
2020-04-10 13:09:08,576 - root - INFO - total cases in community 1 is 2793, active cases: 47
2020-04-10 13:09:09,122 - root - INFO - total cases in community 1 is 2793, active cases: 24
2020-04-10 13:09:09,707 - root - INFO - total cases in community 1 is 2793, active cases: 15
2020-04-10 13:09:10,253 - root - INFO - total cases in community 1 is 2793, active cases: 10
2020-04-10 13:09:10,809 - root - INFO - total cases in community 1 is 2793, active cases: 8
2020-04-10 13:09:11,362 - root - INFO - total cases in community 1 is 2793, active cases: 6
2020-04-10 13:09:11,954 - root - INFO - total cases in community 1 is 2793, active cases: 4
2020-04-10 13:09:12,506 - root - INFO - total cases in community 1 is 2793, active cases: 4
2020-04-10 13:09:13,073 - root - INFO - total cases in community 1 is 2793, active cases: 4
2020-04-10 13:09:13,611 - root - INFO - total cases in community 1 is 2793, active cases: 3
2020-04-10 13:09:14,158 - root - INFO - total cases in community 1 is 2793, active cases: 2
2020-04-10 13:09:14,712 - root - INFO - total cases in community 1 is 2793, active cases: 2
2020-04-10 13:09:15,250 - root - INFO - total cases in community 1 is 2793, active cases: 1
2020-04-10 13:09:15,779 - root - INFO - total cases in community 1 is 2793, active cases: 0
2020-04-10 13:09:16,304 - root - INFO - total cases in community 1 is 2793, active cases: 0
```
