import cirq

# Surface code error correction circuit
qubits = cirq.GridQubit.rect(3, 3)
circuit = cirq.Circuit(
    cirq.X(qubits[0]),
    cirq.measure(qubits[0], key='result')
)
print(circuit)
