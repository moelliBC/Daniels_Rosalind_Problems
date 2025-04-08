#wenn eine .txt nur per Zeilenumbruch Sequenzen
def parse_sequences(filename):
    sequence = {}
    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            line = line.strip()
            sequence[i] = []
            sequence[i] += line
        return sequence

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
        return fastasequence

def parse_sequences_as_str(filename):
    sequence = {}
    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            line = line.strip()
            sequence[i] = ""
            sequence[i] += line
        return sequence