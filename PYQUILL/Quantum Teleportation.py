from pyquil import Program
from pyquil.gates import H, CNOT, CZ

# Quantum teleportation algorithm
program = Program(H(2), CNOT(2, 0), H(2), CNOT(0, 1), CZ(2, 1))
