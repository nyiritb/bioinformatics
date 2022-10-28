import utils
from exercises.bioinformatics_stronghold import prot

def test_rna_to_prot():
    ground_truth = utils.read_text('resources/prot_out.txt')
    result = prot.rna_to_prot(utils.read_text('resources/prot_in.txt'))
    assert(result == ground_truth)