import utils
from exercises.bioinformatics_stronghold.perm import permutate

def test_permutate(n=6):
    result = permutate(n)
    ground_truth = utils.read_text('resources/perm_out.txt')
    assert(result == ground_truth)