import utils

def overlaps(fasta, n=3):
    """Return the name of dnas which overlap with other dna by n bases."""
    dnas = utils.read_fasta(fasta)
    names = ''
    for name1, dna1 in dnas.items():
        for name2, dna2 in dnas.items():
            if name1 != name2 and dna1[-n:] == dna2[:n]:
                names += f'{name1} {name2}\n'
    return names.strip()
   