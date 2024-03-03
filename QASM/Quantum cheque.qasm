OPENQASM 2.0;
include "qelib1.inc";

qreg q[4];
creg c[4];

h q[0];
cx q[1], q[2];
cx q[0], q[2];
h q[1];
t q[0];
t q[1];
tdg q[2];
cx q[1], q[2];
cx q[0], q[1];
t q[2];
cx q[0], q[2];
tdg q[1];
tdg q[2];
cx q[0], q[1];
cx q[1], q[2];
h q[1];
t q[2];
cx q[1], q[2];
h q[0];
measure q[0] -> c[0];

// @columns [0,2,3,4,5,5,5,6,7,7,8,9,9,10,11,12,12,13,14,15]
