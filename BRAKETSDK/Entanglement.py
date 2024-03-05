from braket.circuits import Circuit
from braket.devices import LocalSimulator

def entanglement():
    circuit = Circuit().h(0).cnot(0, 1)
    simulator = LocalSimulator()
    result = simulator.run(circuit, shots=1).result()

    print("Entangled qubits:")
    print("Measurement result:", result.measurement_counts)

entanglement()
