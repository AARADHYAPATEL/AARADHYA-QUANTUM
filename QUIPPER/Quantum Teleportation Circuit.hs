import Quipper

teleport :: (Qubit, Qubit) -> Circ (Qubit, Qubit)
teleport (psi, target) = do
    q <- createEntangledPair
    target <- hadamard target
    target <- cnot psi target
    psi <- hadamard psi
    q <- cnot psi q
    psi <- cnot target psi
    return (psi, target)
