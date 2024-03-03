OPENQASM 2.0;
include "qelib1.inc";

qreg q[4];
creg c[4];

h q[1];
cx q[1], q[0];
h q[1];
h q[2];
cx q[2], q[0];
h q[0];
h q[2];
t q[0];
s q[0];
h q[0];
h q[1];
h q[2];
measure q[0] -> c[0];
measure q[1] -> c[1];

// @columns [0,1,2,2,3,4,4,5,6,7,7,7,8,9]
