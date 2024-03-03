OPENQASM 2.0;
include "qelib1.inc";

qreg q[5];
creg c[4];

h q[0];
h q[1];
sx q[1];
ccx q[0], q[1], q[2];
ccx q[0], q[1], q[3];
ccx q[0], q[1], q[4];
sx q[1];
sx q[0];
ccx q[0], q[1], q[2];
ccx q[0], q[1], q[3];
ccx q[0], q[1], q[4];
sx q[0];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[3] -> c[3];
measure q[4] -> c[3];

// @columns [0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
