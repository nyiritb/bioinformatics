import utils
from exercises.bioinformatics_stronghold import dna

def test_count_bases():
    ground_truth = utils.read_text('resources/dna_out.txt')
    result = dna.count_bases(utils.read_text('resources/dna_in.txt'))
    assert(f"{result['A']} {result['C']} {result['G']} {result['T']}" == ground_truth)