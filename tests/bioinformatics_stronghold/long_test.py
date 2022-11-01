import utils
from exercises.bioinformatics_stronghold.long import shortest_common_superstring

def test_shortest_common_superstring():
    strings = utils.read_fasta('resources/long_in.fasta').values()
    result = shortest_common_superstring(strings)
    ground_truth = utils.read_text('resources/long_out.txt')
    assert(result == ground_truth)