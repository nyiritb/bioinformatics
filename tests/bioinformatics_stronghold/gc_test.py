import utils
from exercises.bioinformatics_stronghold import gc


def test_gc_content():
    ground_truth = utils.read_text('resources/gc_out.txt')
    result = gc.largest_gc_content('resources/gc_in.txt')
    assert(f'{result[0]}\n{result[1]}' == ground_truth)