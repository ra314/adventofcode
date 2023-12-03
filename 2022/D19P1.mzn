include "globals.mzn";

% Parameters
int: max_time = 24;
enum ROCK = {ORE, CLAY, OBSIDIAN, GEODE, NULL};
array[ROCK,ROCK] of int: rock_per_robot;
rock_per_robot =
[|1, 0, 0, 0, 0|
  0, 1, 0, 0, 0|
  0, 0, 1, 0, 0|
  0, 0, 0, 1, 0|
  0, 0, 0, 0, 0|];
array[ROCK,ROCK] of int: blueprint;

array[1..max_time] of var ROCK: decisions;

function var int: earned (array[1..max_time] of var ROCK:decisions, int: time, ROCK: rock) = 
  (if rock=ORE then time-1 else 0 endif) + % This represents the ore robot that you start out with.
  sum(i in 1..time-1)(if decisions[i]=rock/\rock!=NULL then ((time-i)-1) else 0 endif);

%Resources earned. Given an array of decisions and a point in time.
function array[1..5] of var int: earned (array[1..max_time] of var ROCK:decisions, int: time) = 
  [earned(decisions,time,rock) | rock in ROCK];

%Resources spent. Given an array of decisions, a point in time and a blueprint.
function array[1..5] of var int: spent (array[1..max_time] of var ROCK:decisions, int: time, array[ROCK,ROCK] of int: blueprint) = 
  [sum(i in 1..time)(blueprint[decisions[i], rock]) | rock in ROCK];

function var bool: arr_leq(array[1..5] of var int: arr1, array[1..5] of var int: arr2) =
  sum(i in 1..5)(arr1[i] <= arr2[i]) = 5;

constraint forall(i in 1..max_time)(arr_leq(spent(decisions, i, blueprint),earned(decisions, i)));
solve maximize earned(decisions, max_time)[GEODE];

% output [concat(i in 1..max_time)(show(earned(decisions,i))++" "++show(spent(decisions,i,blueprint))++" "++show(decisions[i])++" "++show(i)++"\n")];
output [show(earned(decisions,max_time))++" "++show(earned(decisions,max_time+1))];
