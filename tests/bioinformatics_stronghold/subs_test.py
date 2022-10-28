import utils
from exercises.bioinformatics_stronghold import subs

def test_substring_match():
    ground_truth = utils.read_text('resources/subs_out.txt')
    text, substr = utils.read_text('resources/subs_in.txt').split()
    result = subs.substring_match(text, substr)
    assert(' '.join([str(r) for r in result]) == ground_truth)