import Quipper

superposition :: Int -> Circ Qubit
superposition n = do
    q <- qinit False
    replicateM_ n (hadamard q)
    return q
