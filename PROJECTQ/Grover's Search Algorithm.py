from projectq import MainEngine
from projectq.ops import H, X, Y, Z, Rz, CNOT, Measure

def grover_search():
    eng = MainEngine()
    qubits = eng.allocate_qureg(3)

    H | qubits

    X | qubits[2]
    H | qubits[2]

    for _ in range(2):
        H | qubits[0:2]
        X | qubits[0:2]
        CNOT | (qubits[1], qubits[0])
        X | qubits[0:2]
        H | qubits[0:2]

        H | qubits[2]
        X | qubits[2]
        H | qubits[2]

    Measure | qubits
    eng.flush()
    print(f"Grover's Search Result: {[int(q) for q in qubits]}")

grover_search()
