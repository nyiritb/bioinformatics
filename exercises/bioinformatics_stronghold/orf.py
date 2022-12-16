'''
Problem
Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
'''

from utils import read_fasta, reverse_complement, start_codon_idx, stop_codon_idx, rna_to_amino_acids, dna_to_rna

def open_reading_frame(fasta: str) -> list:
    '''Return every distinct candidate protein string that can be translated from ORFs of s.
    '''
    dna = read_fasta(fasta)
    dna = list(dna.values())[0]
    for strand in [dna, reverse_complement(dna)]:
        for start in start_codon_idx(strand):
            for stop in stop_codon_idx(strand):
                if stop > start and (stop - start) % 3 == 0:
                    yield rna_to_amino_acids(dna_to_rna(strand[start:stop]))
                    break