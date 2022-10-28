import utils

def count_bases(dna):
    """Count the number of bases in a DNA sequence."""
    # Initialize the dictionary
    bases = {base : 0 for base in 'ACGT'}
    # Count the bases
    for base in ['A','C','G','T']:
        bases[base] = dna.count(base)
    return bases

if __name__ == '__main__':
    print(count_bases(utils.read_fasta('resources/dna_in.txt')))