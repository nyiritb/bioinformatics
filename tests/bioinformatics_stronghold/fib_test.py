from exercises.bioinformatics_stronghold.fib import fibonaccis_rabbits

def test_fibonaccis_rabbits(n=29, k=4):
    result = fibonaccis_rabbits(n, k)
    ground_truth = 170361678269
    assert(result == ground_truth)