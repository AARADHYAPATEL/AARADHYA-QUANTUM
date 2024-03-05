Qubit qInput = qAlloc();
Qubit qOutput = qAlloc();

X(qInput);
H(qOutput);
H(qInput);
CNOT(qInput, qOutput);
H(qInput);

Measure(qOutput);
