import Quipper

qft :: [Qubit] -> Circ [Qubit]
qft qs = do
    forM (reverse qs) $ \q -> do
        hadamard q
        forM_ (zip [1..] (reverse qs)) $ \(k, q') -> do
            controlled (phase (2 ** (-k))) q `controlled` q'

main :: IO ()
main = print_simple Preview (qft . take 
