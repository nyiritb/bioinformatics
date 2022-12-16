import utils
from exercises.bioinformatics_stronghold.cons import consensus_string

def test_consensus_string():
    result = consensus_string('resources/cons_in.fasta')
    ground_truth = utils.read_text('resources/cons_out.txt')
    print(result)
    assert(result == ground_truth)