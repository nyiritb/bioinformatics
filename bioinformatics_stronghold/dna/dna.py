def count_bases(dna):
    """Count the number of bases in a DNA sequence."""
    # Initialize the dictionary
    bases = {base : 0 for base in 'ACGT'}
    # Count the bases
    for base in ['A','C','G','T']:
        bases[base] = dna.count(base)
    return bases

if __name__ == '__main__':
    assert(count_bases('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC') == {'A': 20, 'C': 12, 'G': 17, 'T': 21})