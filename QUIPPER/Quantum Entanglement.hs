import Quipper

entanglement :: (Qubit, Qubit) -> Circ (Qubit, Qubit)
entanglement (q1, q2) = do
    hadamard q1
    qnot_at q2 `controlled` q1
    return (q1, q2)

main :: IO ()
main = print_simple Preview (entanglement . pair) 
