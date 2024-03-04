import cirq

# Create a quantum circuit with entangled qubits
qubits = cirq.LineQubit.range(2)
circuit = cirq.Circuit(cirq.H(qubits[0]), cirq.CNOT(qubits[0], qubits[1]))
print(circuit)
