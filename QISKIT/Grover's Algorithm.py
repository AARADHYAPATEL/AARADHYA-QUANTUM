from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram

def initialize_s(qc, qubits):
    """Apply H-gates to a list of qubits."""
    for q in qubits:
        qc.h(q)
    return qc

def diffuser(nqubits):
    """Apply inversion about the average step of Grover's algorithm."""
    qc = QuantumCircuit(nqubits)
    qc.h(range(nqubits))
    qc.append(oracle(nqubits), range(nqubits))
    qc.h(range(nqubits))
    return qc

def grover_algorithm(n, marked_items):
    grover_circuit = QuantumCircuit(n, n)
    grover_circuit = initialize_s(grover_circuit, range(n))
    iterations = int((3.14/4) * 2**(n/2))

    for _ in range(iterations):
        grover_circuit.append(diffuser(n), range(n))
        grover_circuit.append(oracle(n, marked_items), range(n))

    grover_circuit.measure(range(n), range(n))
    return grover_circuit

def oracle(n, marked_items):
    oracle_qc = QuantumCircuit(n, name='oracle')
    marked_items = [int(x) for x in str(marked_items)]  # Convert to list of integers
    for qubit in range(n):
        if qubit in marked_items:
            oracle_qc.x(qubit)
    oracle_qc.cz(range(n-1), n-1)
    for qubit in range(n):
        if qubit in marked_items:
