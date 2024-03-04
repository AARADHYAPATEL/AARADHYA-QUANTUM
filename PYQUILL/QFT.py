from pyquil import Program
from pyquil.gates import H, PHASE, CNOT

# Quantum Fourier Transform on 3 qubits
program = Program(
    H(0), 
    PHASE(1, 2, 0.25), CNOT(1, 2), 
    PHASE(2, 3, 0.5), CNOT(2, 3), 
    H(1), PHASE(1, 2, 0.25), CNOT(1, 2),
    H(2), PHASE(2, 3, 0.5), CNOT(2, 3),
    H(3)
)
