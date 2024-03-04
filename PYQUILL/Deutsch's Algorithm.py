from pyquil import Program
from pyquil.gates import X, H

# Deutsch's quantum algorithm
program = Program(H(0), X(0), H(0))
