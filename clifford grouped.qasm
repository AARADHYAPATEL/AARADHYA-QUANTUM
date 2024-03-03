OPENQASM 2.0;
include "qelib1.inc";

qreg q[6];
creg c[4];

h q[0];
cx q[0], q[1];
cx q[1], q[2];
cx q[0], q[3];
cx q[0], q[4];
s q[0];
h q[1];
h q[0];
cx q[1], q[0];
s q[1];
cx q[0], q[1];
cx q[0], q[1];
s q[0];
s q[1];
cx q[1], q[0];
h q[0];
s q[1];
h q[0];
cx q[1], q[0];
cx q[1], q[0];
s q[1];
h q[1];
cx q[0], q[1];
cx q[1], q[0];
h q[1];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[3] -> c[3];
measure q[4] -> c[3];
measure q[5] -> c[3];

// @columns [0,1,2,3,4,5,5,6,7,8,9,10,11,11,12,13,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
