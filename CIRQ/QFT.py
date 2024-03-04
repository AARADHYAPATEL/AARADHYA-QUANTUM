import cirq

# Quantum Fourier Transform on 3 qubits
qubits = cirq.LineQubit.range(3)
circuit = cirq.Circuit(
    cirq.H.on_each(*qubits),
    (cirq.CZ**-1).on(qubits[0], qubits[2]),
    (cirq.CZ**-2).on(qubits[1], qubits[2]),
    cirq.H.on(qubits[2]),
    cirq.measure(*qubits, key='result')
)
print(circuit)
