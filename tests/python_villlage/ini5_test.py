import utils
from exercises.python_village import ini5

def test_even_numbered_lines():
    ini5.even_numbered_lines('resources/ini5_in.txt', 'resources/ini5_out.txt')
    assert(utils.read_text('resources/ini5_out.txt') == utils.read_text('resources/ini5_out_ground_truth.txt'))