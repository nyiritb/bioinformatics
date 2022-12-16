def read_text(text_file: str) -> str:
    """Read a text file and return a string."""
    with open(text_file, 'r') as f:
        return f.read()

def read_fasta(fasta_file: str) -> dict:
    """Read a fasta file and return a dictionary of sequences."""
    sequences = {}
    with open(fasta_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                name = line[1:].rstrip()
                sequences[name] = ''
            else:
                try:
                    sequences[name] += line.rstrip()
                except UnboundLocalError:
                    print('The FASTA file is not properly formatted.')
                    return ''
    return sequences

def format_dict(dictionary: dict) -> str:
    """Return a dictionary of keys and values separated by space in new lines."""
    return '\n'.join([f'{key} {value}' for key, value in dictionary.items()])

def codon_table() -> dict:
    return {
        'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
        'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
        'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
        'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
        'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
        'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
        'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
        'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
        'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
        'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
        'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
        'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
        'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
        'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
        'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
    }

def monoisotopic_mass_table() -> dict:
    return {
        'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
        'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406,
        'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
        'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
        'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333
    }

def reverse_complement(dna: str) -> str:
    """Return the reverse complement of a DNA string."""
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna[::-1]])

def start_codon_idx(dna: str) -> list:
    """Return a list of start codon indices."""
    start_codon = 'ATG'
    start_codon_idx = []
    for i in range(len(dna)):
        if dna[i:i+3] == start_codon:
            start_codon_idx.append(i)
    return start_codon_idx

def stop_codon_idx(dna: str) -> list:
    """Return a list of stop codon indices."""
    stop_codons = ('TAA', 'TAG', 'TGA')
    stop_codon_idx = []
    for i in range(len(dna)):
        if dna[i:i+3] in stop_codons:
            stop_codon_idx.append(i)
    return stop_codon_idx

def dna_to_rna(dna: str) -> str:
    """Return the RNA string corresponding to a DNA string."""
    return dna.replace('T', 'U')

def rna_to_amino_acids(rna: str, include_stop = True) -> str:
    """Return the amino acid string corresponding to a RNA string."""
    if len(rna) % 3 != 0:
        raise ValueError('The length of the RNA string must be a multiple of 3.')
    translator = codon_table()
    if include_stop:
        return ''.join([translator[rna[i:i+3]] for i in range(0, len(rna), 3)])
    else:
        return ''.join([translator[rna[i:i+3]] for i in range(0, len(rna), 3) if translator[rna[i:i+3]] != 'Stop'])