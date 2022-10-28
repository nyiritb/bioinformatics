def read_text(text_file: str) -> str:
    """Read a text file and return a string."""
    with open(text_file, 'r') as f:
        return f.read()

def read_fasta(fasta_file: str) -> str:
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