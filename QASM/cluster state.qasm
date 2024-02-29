OPENQASM 2.0;
include "qelib1.inc";

qreg q[4];
creg c[4];
h q[0];
h q[1];
h q[2];
h q[3];
swap q[0], q[1];
h q[0];
swap q[1], q[2];
swap q[2], q[3];
h q[3];
rx(pi/2) q[3];
cx q[2], q[3];
measure q[3] -> c[3];
