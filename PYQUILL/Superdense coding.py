from pyquil import Program
from pyquil.gates import H, X, Z, CNOT

# Superdense coding algorithm
program = Program(H(0), CNOT(0, 1), X(0), Z(0))
