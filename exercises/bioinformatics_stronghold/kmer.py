'''
Problem
For a fixed positive integer k, order all possible k-mers taken from an underlying alphabet lexicographically.

Then the k-mer composition of a string s can be represented by an array A for which A[m] denotes the number of times that the mth k-mer (with respect to the lexicographic order) appears in s.

Given: A DNA string s in FASTA format (having length at most 100 kbp).

Return: The 4-mer composition of s.
'''
from utils import read_fasta
from exercises.bioinformatics_stronghold.lexf import lexf
import re

def kmer(fasta: str, k: int) -> list:
    '''Returns the k-mer composition of s.'''
    dna = list(read_fasta(fasta).values())[0]
    kmers = lexf(['A','C','G','T'], k)
    # make sure to include overlapping matches too
    return [len(re.findall(f'(?={kmer})', dna)) for kmer in kmers]
