from braket.circuits import Circuit
from braket.devices import LocalSimulator

def bit_flip_code():
    circuit = Circuit().h(0).cnot(0, 1).cnot(0, 2)

    # Simulate a bit flip error on qubit 1
    circuit.x(1)

    # Correct the error
    circuit.cnot(0, 1).cnot(0, 2).h(0)

    simulator = LocalSimulator()
    result = simulator.run(circuit, shots=1).result()

    print("Bit Flip Code Result:")
    print("Measurement result:", result.measurement_counts)

bit_flip_code()
