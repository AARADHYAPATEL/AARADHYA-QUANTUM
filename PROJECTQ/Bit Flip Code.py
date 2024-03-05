from projectq import MainEngine
from projectq.ops import H, CNOT, Measure

def bit_flip_code():
    eng = MainEngine()
    qubits = eng.allocate_qureg(3)

    H | qubits[0]
    CNOT | (qubits[0], qubits[1])
    CNOT | (qubits[0], qubits[2])

    # Simulate a bit flip error on qubit qubits[1]
    X | qubits[1]

    # Correct the error
    CNOT | (qubits[0], qubits[1])
    CNOT | (qubits[0], qubits[2])
    H | qubits[0]

    Measure | qubits
    eng.flush()
    print(f"Bit Flip Code Result: {[int(q) for q in qubits]}")

bit_flip_code()
