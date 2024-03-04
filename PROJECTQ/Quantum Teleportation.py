from projectq import MainEngine
from projectq.ops import H, CNOT, Measure, X, Z

def quantum_teleportation():
    eng = MainEngine()
    alice = eng.allocate_qubit()
    bob = eng.allocate_qubit()
    msg = eng.allocate_qubit()

    H | alice
    CNOT | (alice, bob)
    X | msg
    Z | msg

    Measure | alice
    Measure | msg

    CNOT | (msg, bob)
    H | msg

    Measure | msg
    eng.flush()
    print(f"Teleported qubit: {int(bob)}")

quantum_teleportation()
