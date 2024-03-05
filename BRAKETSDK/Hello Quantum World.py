from braket.circuits import Circuit
from braket.devices import LocalSimulator

def hello_quantum_world():
    circuit = Circuit()
    simulator = LocalSimulator()
    result = simulator.run(circuit, shots=1).result()

    print("Hello Quantum World!")
    print("Measurement result:", result.measurement_counts)

hello_quantum_world()
