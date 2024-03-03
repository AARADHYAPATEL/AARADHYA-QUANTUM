OPENQASM 2.0;
include "qelib1.inc";

qreg q[5];
creg c[4];

h q[0];
h q[1];
h q[3];
h q[4];
cx q[4], q[2];
cx q[3], q[4];
cx q[0], q[2];
s q[0];
s q[1];
s q[3];
h q[0];
h q[1];
h q[3];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[3] -> c[3];
measure q[4] -> c[3];

// @columns [0,0,0,1,2,4,5,7,7,7,8,8,8,9,10,11,12,13]
