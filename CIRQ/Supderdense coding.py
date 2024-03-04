import cirq

# Superdense coding circuit
alice, bob = cirq.LineQubit.range(2)
circuit = cirq.Circuit(
    cirq.H(alice),
    cirq.CNOT(alice, bob),
    cirq.X(alice),
    cirq.CZ(alice, bob),
    cirq.H(alice),
    cirq.measure(alice, bob, key='result')
)
print(circuit)
