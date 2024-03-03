OPENQASM 2.0;
include "qelib1.inc";

qreg q[5];
creg c[4];

h q[0];
cx q[0], q[2];
h q[0];
h q[2];
cx q[0], q[1];
h q[0];
cx q[0], q[1];
h q[0];
h q[1];
sx q[2];
cx q[1], q[2];
h q[1];
cx q[1], q[2];
measure q[2] -> c[2];

// @columns [0,1,2,2,3,4,5,6,6,6,7,8,9,10]
