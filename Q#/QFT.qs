// Quantum Fourier Transform on 3 qubits
operation QFT() : Unit {
    using (qubits = Qubit[3]) {
        ApplyToEach(H, qubits);
        ApplyToEach(Phase(1.0/2.0, _), new Int[]{ 1 }, qubits);
        ApplyToEach(Phase(1.0/4.0, _), new Int[]{ 2 }, qubits);
        ApplyToEach(Phase(1.0/8.0, _), new Int[]{ 3 }, qubits);
        SWAP(qubits[0], qubits[2]);
    }
}
