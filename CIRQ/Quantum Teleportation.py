import cirq

# Quantum teleportation circuit
alice, bob, shared = cirq.LineQubit.range(3)
circuit = cirq.Circuit(
    cirq.H(shared),
    cirq.CNOT(shared, alice),
    cirq.H(shared),
    cirq.CNOT(alice, bob),
    cirq.CZ(shared, bob),
    cirq.measure(alice, bob, key='result')
)
print(circuit)
