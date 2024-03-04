from pyquil import Program
from pyquil.gates import H, CNOT

# Bit flip quantum error correction
program = Program(H(0), CNOT(0, 1), CNOT(0, 2), CNOT(1, 2), H(0))
