include "globals.mzn";

% Parameters
int: max_time = 26;
array[VALVE,VALVE] of int: time; % time to go from valve x to valve y, and to open valve y
int: p = 10; % A guess for the length of the path to speed up processing
array[VALVE] of int: valve_flow_rate;

/*
enum VALVE = {AA, BB, CC, DD, EE, HH, JJ, XXX};
int: n = 8;
time = 
[|0, 2, 3, 2, 3, 6, 3, 0|
  2, 0, 2, 3, 4, 7, 4, 0|
  3, 2, 0, 2, 3, 6, 5, 0|
  2, 3, 2, 0, 2, 5, 4, 0|
  3, 4, 3, 2, 0, 4, 5, 0|
  6, 7, 6, 5, 4, 0, 8, 0|
  3, 4, 5, 4, 5, 8, 0, 0|
  100, 100, 100, 100, 100, 100, 100, 0|];
valve_flow_rate = [0, 13, 2, 20, 3, 22, 21, 0];
*/
enum VALVE = {AA, CY, HM, IN, KC, KD, KX, LR, MX, NU, PD, QI, SJ, VQ, XXX, YO, YR};
int: n = 17;
time = 
[|0, 5, 9, 8, 7, 9, 4, 7, 3, 4, 6, 4, 7, 4, 0, 6, 5|
  5, 0, 13, 12, 11, 13, 4, 11, 3, 8, 10, 3, 11, 8, 0, 10, 3|
  9, 13, 0, 3, 7, 8, 12, 7, 11, 6, 4, 12, 13, 10, 0, 5, 13|
  8, 12, 3, 0, 8, 6, 11, 5, 10, 5, 5, 11, 14, 11, 0, 3, 12|
  7, 11, 7, 8, 0, 9, 10, 7, 9, 4, 4, 10, 7, 4, 0, 6, 11|
  9, 13, 8, 6, 9, 0, 12, 4, 11, 6, 6, 12, 15, 12, 0, 4, 13|
  4, 4, 12, 11, 10, 12, 0, 10, 4, 7, 9, 3, 10, 7, 0, 9, 6|
  7, 11, 7, 5, 7, 4, 10, 0, 9, 4, 4, 10, 13, 10, 0, 3, 11|
  3, 3, 11, 10, 9, 11, 4, 9, 0, 6, 8, 4, 9, 6, 0, 8, 3|
  4, 8, 6, 5, 4, 6, 7, 4, 6, 0, 3, 7, 10, 7, 0, 3, 8|
  6, 10, 4, 5, 4, 6, 9, 4, 8, 3, 0, 9, 10, 7, 0, 3, 10|
  4, 3, 12, 11, 10, 12, 3, 10, 4, 7, 9, 0, 10, 7, 0, 9, 4|
  7, 11, 13, 14, 7, 15, 10, 13, 9, 10, 10, 10, 0, 4, 0, 12, 11|
  4, 8, 10, 11, 4, 12, 7, 10, 6, 7, 7, 7, 4, 0, 0, 9, 8|
  100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 0, 100, 100|
  6, 10, 5, 3, 6, 4, 9, 3, 8, 3, 3, 9, 12, 9, 0, 0, 10|
  5, 3, 13, 12, 11, 13, 6, 11, 3, 8, 10, 4, 11, 8, 0, 10, 0|];
valve_flow_rate = [0, 14, 24, 22, 12, 13, 7, 18, 6, 8, 10, 5, 23, 11, 0, 20, 21];

VALVE: start_valve = AA;
VALVE: null_valve = XXX;


% Variables
array[1..p] of var VALVE: me_visited; % valves that you visited and their order
var int: me_time_spent = sum(i in 1..p-1)(time[me_visited[i],me_visited[i+1]]);
var int: me_flow_amount = sum(i in 1..p-1)((max_time-sum(j in 1..i)(time[me_visited[j],me_visited[j+1]]))*valve_flow_rate[me_visited[i+1]]);

array[1..p] of var VALVE: el_visited; % valves that you visited and their order
var int: el_time_spent = sum(i in 1..p-1)(time[el_visited[i],el_visited[i+1]]);
var int: el_flow_amount = sum(i in 1..p-1)((max_time-sum(j in 1..i)(time[el_visited[j],el_visited[j+1]]))*valve_flow_rate[el_visited[i+1]]);

constraint me_visited[1] = start_valve;
constraint me_time_spent <= max_time;

constraint el_visited[1] = start_valve;
constraint el_time_spent <= max_time;

constraint alldifferent_except(me_visited, {XXX});
constraint alldifferent_except(el_visited, {XXX});
constraint alldifferent_except(me_visited[2..p]++el_visited[2..p], {XXX});

solve maximize el_flow_amount+me_flow_amount;

output [show(el_visited)++" "++show(me_visited)++" "++show(el_time_spent+me_time_spent)++" "++show(el_flow_amount+me_flow_amount)]