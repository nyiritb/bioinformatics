import utils
from exercises.bioinformatics_stronghold.kmer import kmer

def test_kmer():
    result = kmer('resources/kmer_in.fasta', 4)
    ground_truth = [int(i) for i in utils.read_text('resources/kmer_out.txt').split()]
    print(' '.join([str(r) for r in result]))
    assert(result == ground_truth)