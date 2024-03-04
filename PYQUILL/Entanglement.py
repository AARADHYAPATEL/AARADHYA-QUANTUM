from pyquil import Program
from pyquil.gates import H, CNOT

# Creating an entangled pair of qubits
program = Program(H(0), CNOT(0, 1))
