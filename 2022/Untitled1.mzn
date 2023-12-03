var 1..3: x;
var int: tot = sum(j in 2..5)(j+x);
solve maximize tot;

output [show(tot)];