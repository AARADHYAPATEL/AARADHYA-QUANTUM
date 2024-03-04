import Quipper

createEntangledPair :: Circ (Qubit, Qubit)
createEntangledPair = do
    q1 <- qinit False
    q2 <- qinit False
    q1 <- hadamard q1
    q2 <- cnot q1 q2
    return (q1, q2)
