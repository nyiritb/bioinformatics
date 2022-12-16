from exercises.bioinformatics_stronghold.splc import splicing
import utils

def test_splicing():
    result = splicing('resources/splc_in.fasta')
    ground_truth = utils.read_text('resources/splc_out.txt')
    assert(result == ground_truth)