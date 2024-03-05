Qubit qAlice = qAlloc();
Qubit qBob = qAlloc();
Qubit qData = qAlloc();

H(qData);
CNOT(qData, qAlice);
H(qAlice);
CNOT(qAlice, qBob);
H(qBob);

Measure(qData);
Measure(qAlice);
Measure(qBob);
