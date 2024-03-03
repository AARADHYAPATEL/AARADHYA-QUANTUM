OPENQASM 2.0;
include "qelib1.inc";

qreg q[5];
creg c[4];
h q[0];
h q[2];
t q[0];
cx q[1], q[2];
h q[4];
h q[0];
h q[1];
h q[2];
s q[0];
cx q[1], q[2];
h q[2];
cx q[4], q[2];
h q[4];
h q[2];
cx q[1], q[2];
h q[2];
h q[1];
cx q[1], q[2];
h q[2];
h q[1];
cx q[0], q[1];
CX q[0], q[2];
h q[0];
h q[2];
cx q[0], q[2];
h q[2];
measure q[2] -> c[2];