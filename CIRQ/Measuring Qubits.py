import cirq

# Create a quantum circuit with measurement
qubits = cirq.LineQubit.range(2)
circuit = cirq.Circuit(cirq.measure(*qubits, key='result'))
print(circuit)
