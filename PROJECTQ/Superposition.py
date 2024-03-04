from projectq import MainEngine
from projectq.ops import H, Measure

def superposition():
    eng = MainEngine()
    qubit = eng.allocate_qubit()
    H | qubit
    Measure | qubit
    eng.flush()
    print(f"Qubit in superposition: {int(qubit)}")

superposition()
