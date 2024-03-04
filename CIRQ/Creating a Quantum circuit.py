import cirq

# Create a quantum circuit with 2 qubits
circuit = cirq.Circuit(cirq.H(q) for q in cirq.LineQubit.range(2))
print(circuit)
