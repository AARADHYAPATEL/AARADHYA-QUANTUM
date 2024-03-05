from projectq import MainEngine
from projectq.ops import H, Measure

def quantum_random_number():
    eng = MainEngine()
    qubit = eng.allocate_qubit()

    H | qubit
    Measure | qubit

    eng.flush()
    random_number = int(qubit)
    print(f"Quantum Random Number: {random_number}")

quantum_random_number()
