// Deutsch's quantum algorithm
operation DeutschAlgorithm(isConstant: Bool) : Unit {
    using (qubit = Qubit()) {
        H(qubit);
        if (isConstant) {
            X(qubit);
        }
    }
}
