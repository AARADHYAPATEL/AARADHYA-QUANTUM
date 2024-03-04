from projectq import MainEngine
from projectq.ops import H, X, Measure

def deutsch_algorithm(is_constant):
    eng = MainEngine()
    qubit = eng.allocate_qubit()

    H | qubit

    if is_constant:
        X | qubit

    Measure | qubit
    eng.flush()

    result = int(qubit)
    print(f"Deutsch's Algorithm Result: {result}")

deutsch_algorithm(True)
