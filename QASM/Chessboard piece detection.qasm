OPENQASM 2.0;
include "qelib1.inc";

qreg q[5];
creg c[5];

reset q[0];
reset q[1];
reset q[2];
reset q[3];
reset q[4];
h q[1];
h q[2];
h q[4];
cx q[2], q[0];
h q[0];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[4] -> c[4];

// @columns [0,0,0,0,0,1,1,1,2,3,4,5,6,7]
