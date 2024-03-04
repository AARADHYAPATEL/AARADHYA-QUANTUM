import cirq

# Simulate a quantum circuit
qubit = cirq.LineQubit(0)
circuit = cirq.Circuit(cirq.H(qubit), cirq.measure(qubit, key='result'))

simulator = cirq.Simulator()
result = simulator.run(circuit)
print(result)
