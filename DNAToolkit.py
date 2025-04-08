# DNA Toolkyt
from structures import *
from parsers import *

Nucleotides = ["A", "C", "G", "T", "U"]

# überprüfe, ob Sequenz DNA String ist

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


#zählt die Nukleotide
def countNucFrequency(seq):
	tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
	for nuc in seq:
		tmpFreqDict[nuc] += 1
	return tmpFreqDict

#transkribiert den sense strand
def transcribeDNA(seq):
    RNAString = ''
    for nuc in seq:
        if nuc == 'A':
            RNAString += 'A'
        elif nuc == 'C':
            RNAString += 'C'
        elif nuc == 'T':
            RNAString += 'U'
        elif nuc == 'G':
            RNAString += 'G'
    return RNAString

#gibt den komplementierten Strang in 5'-3'-Richtung aus
def complementDNA(seq):
    ComplString = ''
    for nuc in seq:
        if nuc == 'A':
            ComplString += 'T'
        elif nuc == 'C':
            ComplString += 'G'
        elif nuc == 'T':
            ComplString += 'A'
        elif nuc == 'G':
            ComplString += 'C'
    revComplString = ComplString[::-1]
    return revComplString


#gibt den GC-Anteil von einem Genom im FASTA-Format aus
def gccontent(filename):
    genome_data = parse_fasta(filename)
    for header, seq in genome_data.items():
        print(header)
        print((seq.count('G') + seq.count('C')) / len(seq) * 100)


def pointmutation(filename):
     sequences = parse_sequences(filename)
     seq1 = sequences[1]
     seq2 = sequences[2]
     n = 0
     for i in range(0, len(sequences[1])):
         if seq1[i] != seq2[i]:
             n = n + 1
     print(n)

def genetic_code(filename):
    peptidkette = ""
    with open(filename, 'r') as file:
        line = file.readline()
    triplett = [line[i:i+3] for i in range(0, len(line), 3)]
    for i in range(0, len(triplett)):
        if rna_codon_table[triplett[i]] == 'Stop':
            print(peptidkette)
            return
        peptidkette += rna_codon_table[triplett[i]]
    print(peptidkette)