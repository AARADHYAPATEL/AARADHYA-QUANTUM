// Quantum random number generator
operation QuantumRandomNumber() : Int {
    using (qubit = Qubit()) {
        H(qubit);
        return M(qubit);
    }
}
