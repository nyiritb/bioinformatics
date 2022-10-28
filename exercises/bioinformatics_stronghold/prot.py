import utils

def rna_to_prot(rna):
    codon_table = utils.codon_table()
    prot = ''
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if codon_table[codon] == 'Stop':
            break
        prot += codon_table[codon]
    return prot