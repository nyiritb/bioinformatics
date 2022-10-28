import utils

def gc_content(dna):
    """Calculate the GC content of a DNA sequence."""
    # Initialize the dictionary
    bases = {base : 0 for base in 'ATGC'}
    # Count the bases
    for base in bases:
        bases[base] = dna.count(base)
    return((bases['G'] + bases['C']) / sum(bases.values()) * 100)

def largest_gc_content(fasta_file):
    """Return the content of the FASTA file with the largest GC content."""
    # Read the FASTA file
    named_sequences = utils.read_fasta('resources/gc_in.fasta')
    # Calculate the GC content of each sequence
    results = {name : gc_content(sequence) for name, sequence in named_sequences.items()}
    # Find the sequence with the largest GC content
    return(max(results, key=results.get), results[max(results, key=results.get)])

if __name__ == '__main__':
    print(largest_gc_content('resources/gc_in.fasta'))