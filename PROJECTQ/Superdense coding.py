from projectq import MainEngine
from projectq.ops import H, X, Z, CNOT, Measure

def superdense_coding():
    eng = MainEngine()
    alice = eng.allocate_qubit()
    bob = eng.allocate_qubit()

    H | alice
    CNOT | (alice, bob)
    X | alice
    Z | alice

    Measure | alice
    Measure | bob

    eng.flush()
    print(f"Superdense Coding Result: {int(alice)}, {int(bob)}")

superdense_coding()
