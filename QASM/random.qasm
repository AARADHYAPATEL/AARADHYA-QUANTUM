OPENQASM 2.0;
include "qelib1.inc";

qreg q[5];
creg c[4];
reset q[0];
reset q[1];
reset q[2];
reset q[3];
reset q[4];
z q[0];
x q[1];
h q[2];
x q[3];
z q[4];
x q[0];
z q[1];
h q[3];
x q[4];
z q[1];
x q[3];
z q[4];
z q[3];
x q[4];
