import cirq

# Grover's algorithm for a 3-qubit search
qubits = cirq.LineQubit.range(3)
circuit = cirq.Circuit(
    cirq.H.on_each(*qubits),
    cirq.X(qubits[2]),
    cirq.H(qubits[2]),
    cirq.CCX(qubits[0], qubits[1], qubits[2]),
    cirq.H(qubits[2]),
    cirq.X(qubits[2]),
    cirq.H.on_each(*qubits),
    cirq.measure(*qubits, key='result')
)
print(circuit)
