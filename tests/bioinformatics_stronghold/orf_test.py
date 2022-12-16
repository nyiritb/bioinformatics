import utils
from exercises.bioinformatics_stronghold.orf import open_reading_frame

def test_shortest_common_superstring():
    result = set(open_reading_frame('resources/orf_in.fasta'))
    print('\n'.join(result))
    ground_truth = set(utils.read_text('resources/orf_out.txt').split('\n'))
    assert(result == ground_truth)