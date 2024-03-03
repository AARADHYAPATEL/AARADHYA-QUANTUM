OPENQASM 2.0;
include "qelib1.inc";

qreg q[4];
creg c[4];
h q[1];
h q[2];
s q[1];
s q[2];
h q[2];
cx q[1], q[2];
h q[2];
s q[2];
h q[2];
h q[2];
cx q[1], q[2];
h q[2];
h q[2];
measure q[2] -> c[2];
