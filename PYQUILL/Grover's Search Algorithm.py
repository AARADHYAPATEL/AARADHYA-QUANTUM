from pyquil import Program
from pyquil.gates import H, X, CNOT

# Grover's quantum search algorithm on 3 qubits
program = Program(
    H(0), H(1), H(2),
    X(2),
    H(2),
    CNOT(1, 2),
    H(2),
    CNOT(0, 1),
    H(1),
    CNOT(1, 2),
    H(2),
    CNOT(0, 1),
    H(1),
    X(0)
)
