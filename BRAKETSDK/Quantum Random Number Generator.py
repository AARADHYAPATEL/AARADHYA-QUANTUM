from braket.circuits import Circuit
from braket.devices import LocalSimulator

def quantum_random_number():
    circuit = Circuit().h(0)
    simulator = LocalSimulator()
    result = simulator.run(circuit, shots=1).result()

    print("Quantum Random Number:")
    print("Measurement result:", result.measurement_counts)

quantum_random_number()
