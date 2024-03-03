OPENQASM 2.0;
include "qelib1.inc";

qreg q[5];
creg c[4];

cx q[0], q[1];
cx q[1], q[2];
cx q[0], q[3];
cx q[1], q[3];
cx q[0], q[4];
cx q[2], q[4];
measure q[4] -> c[3];
measure q[3] -> c[3];

// @columns [0,1,4,5,6,7,8,9]
