# DNA Toolkyt


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

#soll fasta format in header und sequence ausgeben
def parse_fasta(filename):
    """
    A simple generator function to read a FASTA file and yield tuples of
    (header, sequence_string).
    """
    fastasequence = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                header = line[1:]
                fastasequence[header] = ""
            else:
                fastasequence[header] += line
        return(fastasequence)

#gibt den GC-Anteil von einem Genom im FASTA-Format aus
def gccontent(filename):
    genome_data = parse_fasta(filename)
    for header, seq in genome_data.items():
        print(header)
        print((seq.count('G') + seq.count('C')) / len(seq) * 100)

#wenn eine .txt nur per Zeilenumbruch Sequenzen
def parse_sequences(filename):
    sequence = {}
    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            line = line.strip()
            sequence[i] = []
            sequence[i] += line
        return(sequence)

def pointmutation(filename):
     sequences = parse_sequences(filename)
     seq1 = sequences[1]
     seq2 = sequences[2]
     n = 0
     for i in range(0, len(sequences[1])):
         if seq1[i] != seq2[i]:
             n = n + 1
     print(n)