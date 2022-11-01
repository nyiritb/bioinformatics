from exercises.bioinformatics_stronghold import prtm
import utils

def test_weight_of_protein():
    ground_truth = float(utils.read_text('resources/prtm_out.txt'))
    result = prtm.weight_of_protein(utils.read_text('resources/prtm_in.txt'))
    assert(result == ground_truth)
