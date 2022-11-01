import utils

def weight_of_protein(amino_acids):
    """
    Given a string of amino acids, return the weight of the protein.
    """
    mass_table = utils.monoisotopic_mass_table()
    sum_weight = 0
    for aa in amino_acids:
        sum_weight += mass_table[aa]
    return sum_weight