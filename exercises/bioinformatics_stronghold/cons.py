from utils import read_fasta

def consensus_string(fasta: str) -> str:
    '''Return the consensus string and profile matrix for the collection of strings in FASTA format.
    '''
    strings = list(read_fasta(fasta).values())
    profile = profile_matrix(strings)
    dna_length = len(strings[0])
    consensus = ''.join([max(profile, key=lambda k: profile[k][i]) for i in range(dna_length)])
    output = consensus + '\n'
    output += pretty_print_profile(profile)
    return output

def profile_matrix(sequences: list) -> dict:
    '''Return the profile matrix for the collection of dna sequences.
    '''
    dna_len = len(sequences[0])
    profile = {'A': [0] * dna_len, 'C': [0] * dna_len, 'G': [0] * dna_len, 'T': [0] * dna_len}
    for dna in sequences:
        for i, c in enumerate(dna):
            profile[c][i] += 1
    return profile

def pretty_print_profile(profile: dict) -> str:
    '''Return the profile matrix in a pretty format.
    '''
    output = ''
    for k in profile:
        output += k + ': ' + ' '.join(map(str, profile[k])) + '\n'
    output = output.strip()
    return output