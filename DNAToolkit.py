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

def motif_finder(filename):
    positions = []
    data = parse_sequences_as_str(filename)
    seq = data[1]
    motif = data[2]
    for i in range(0, len(seq)):
        x = seq[i:i+len(motif)]
        if x == motif:
            positions.append(str(i+1))
    print(positions)

    print(" ".join(positions))

def consensus_finder(filename):
    sequences = parse_fasta(filename)
    matrix = []
    profile = [[], [], [], []]
    for key, value in sequences.items():
        matrix_line = []
        for dna_char in value:
            matrix_line.append(dna_char)
        matrix.append(matrix_line)

    for i in range(0, len(matrix[0])):
        a = 0
        t = 0
        g = 0
        c = 0
        for j in range(0, len(sequences.keys())):
            dna_char = matrix[j][i]
            if dna_char == "A":
                a = a + 1
            elif dna_char == "T":
                t = t + 1
            elif dna_char == "C":
                c = c + 1
            elif dna_char == "G":
                g = g + 1
        profile[0].append(a)
        profile[1].append(c)
        profile[2].append(g)
        profile[3].append(t)
    print(profile)
    #Nukleotide in consensus zählen
    consensus = []
    for i in range(len(matrix[0])):
        col_count = [profile[0][i], profile[1][i], profile[2][i], profile[3][i]]
        max_count = max(col_count)
        consensus_collumn = [Nucleotides[k] for k in range(4) if col_count[k] == max_count]
        consensus.append(consensus_collumn)
    consensus_output = ['']
    print(consensus)

    for i in range(len(consensus)):
        consensus_output.append(consensus[i][0])
    #for col in consensus:
     #   consensus_output = [prefix + nuc for prefix in consensus_output for nuc in col] # it just works. trust the process

    print (''.join(str(char) for char in consensus_output))
    print("A: " + ' '.join(str(num) for num in profile[0]))
    print("C: " + ' '.join(str(num) for num in profile[1]))
    print("G: " + ' '.join(str(num) for num in profile[2]))
    print("T: " + ' '.join(str(num) for num in profile[3]))