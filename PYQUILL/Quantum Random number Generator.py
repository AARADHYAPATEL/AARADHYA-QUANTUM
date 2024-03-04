from pyquil import Program
from pyquil.gates import H, MEASURE

# Quantum random number generator
program = Program(H(0), MEASURE(0, [0]))
