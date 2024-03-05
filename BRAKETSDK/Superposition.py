from braket.circuits import Circuit
from braket.devices import LocalSimulator

def superposition():
    circuit = Circuit().h(0)
    simulator = LocalSimulator()
    result = simulator.run(circuit, shots=1).result()

    print("Qubit in superposition:")
    print("Measurement result:", result.measurement_counts)

superposition()
