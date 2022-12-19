from exercises.bioinformatics_stronghold.lexf import lexf
import utils

def test_lexf():
    alphabet, n = (utils.read_text('resources/lexf_in.txt').split('\n')[0]).split(), int(utils.read_text('resources/lexf_in.txt').split('\n')[1])
    result = lexf(alphabet, n)
    ground_truth = utils.read_text('resources/lexf_out.txt').split('\n')
    for r in result:
        print(r)
    assert(result == ground_truth)