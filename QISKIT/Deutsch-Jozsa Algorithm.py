from qiskit import QuantumCircuit, Aer, transpile, assemble

# Oracle for a balanced function
def balanced_oracle(qc, n):
    for qubit in range(n):
        qc.x(qubit)
    qc.append(oracle(n, 'balanced'), range(n))
    for qubit in range(n):
        qc.x(qubit)

# Oracle for a constant function
def constant_oracle(qc, n):
    qc.append(oracle(n, 'constant'), range(n))

# Generalized oracle
def oracle(n, oracle_type='balanced'):
    oracle_qc = QuantumCircuit(n+1, name='oracle')
    if oracle_type == 'balanced':
        for qubit in range(n):
            oracle_qc.cx(qubit, n)
    elif oracle_type == 'constant':
        pass  # Do nothing, i.e., apply the identity operation
    return oracle_qc.to_instruction()

# Deutsch-Jozsa Algorithm
def deutsch_jozsa_algorithm(n, oracle_type='balanced'):
    qc = QuantumCircuit(n+1, n)
    qc.x(n)
    qc.h(n)
    qc.h(range(n+1))

    if oracle_type == 'balanced':
        balanced_oracle(qc, n)
    elif oracle_type == 'constant':
        constant_oracle(qc, n)

    qc.h(range(n))
    qc.measure(range(n), range(n))

    return qc

# Simulate the Deutsch-Jozsa Algorithm
n = 3  # Number of qubits
sim = Aer.get_backend('aer_simulator')
dj_circuit = deutsch_jozsa_algorithm(n, 'balanced')
compiled_circuit = transpile(dj_circuit, sim)
result = sim.run(assemble(compiled_circuit)).result()

# Display the result
print(result.get_counts())
