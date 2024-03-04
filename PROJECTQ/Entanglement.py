from projectq import MainEngine
from projectq.ops import H, CNOT, Measure

def entanglement():
    eng = MainEngine()
    qubit1 = eng.allocate_qubit()
    qubit2 = eng.allocate_qubit()
    H | qubit1
    CNOT | (qubit1, qubit2)
    Measure | qubit1
    Measure | qubit2
    eng.flush()
    print(f"Entangled qubits: {int(qubit1)}, {int(qubit2)}")

entanglement()
