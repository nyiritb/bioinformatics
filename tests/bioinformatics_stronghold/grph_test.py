from exercises.bioinformatics_stronghold.grph import overlaps
import utils

def test_overlaps():
    ground_truth = utils.read_text('resources/grph_out.txt')
    result = overlaps('resources/grph_in.fasta')
    assert(result == ground_truth)