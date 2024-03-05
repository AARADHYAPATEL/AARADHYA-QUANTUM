Qubit q1 = qAlloc();
Qubit q2 = qAlloc();
H(q1);
CNOT(q1, q2);
Measure(q1);
Measure(q2);
