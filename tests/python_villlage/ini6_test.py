import utils
from exercises.python_village import ini6

def test_word_occurences():
    ground_truth = utils.read_text('resources/ini6_out.txt')
    result = ini6.word_occurences(utils.read_text('resources/ini6_in.txt'))
    assert(utils.format_dict(result) == ground_truth)