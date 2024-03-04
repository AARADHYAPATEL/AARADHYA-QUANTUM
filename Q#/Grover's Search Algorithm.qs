// Grover's quantum search algorithm on 3 qubits
operation GroverSearch() : Unit {
    using (qubits = Qubit[3]) {
        ApplyToEach(H, qubits);
        X(qubits[2]);
        H(qubits[2]);
        ApplyToEach(Controlled X, qubits[0..1], qubits[2]);
        H(qubits[2]);
        ApplyToEach(Controlled X, qubits[0..1], qubits[2]);
        H(qubits[2]);
        ApplyToEach(X, qubits);
        ApplyToEach(H, qubits);
    }
}
