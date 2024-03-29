OPENQASM 2.0;
include "qelib1.inc";

qreg q[5];
creg c[4];

reset q[0];
reset q[1];
reset q[2];
reset q[3];
reset q[4];
h q[0];
sx q[1];
h q[1];
cx q[1], q[2];
h q[0];
cx q[1], q[2];
h q[1];
sx q[1];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];

// @columns [0,0,0,0,0,1,1,3,4,8,8,9,10,11,12,13]
