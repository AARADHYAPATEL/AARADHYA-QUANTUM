from projectq import MainEngine
from projectq.ops import H, Swap, R

def quantum_fourier_transform():
    eng = MainEngine()
    qubits = eng.allocate_qureg(3)

    for i, qubit in enumerate(qubits):
        H | qubit
        for j in range(i + 1, len(qubits)):
            R(-1.0 / (2 ** (j - i))) | qubits[j]
            CNOT | (qubit, qubits[j])

    Swap | (qubits[0], qubits[2])
    eng.flush()
    print(f"Quantum Fourier Transform applied to qubits: {[int(q) for q in qubits]}")

quantum_fourier_transform()
