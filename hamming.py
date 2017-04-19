def distance(dna1,dna2):
    hamming = 0
    if len(dna1) == len(dna2):
        index = 0
        while index < len(dna1):
            if dna1[index] != dna2[index]:
                hamming += 1
            index = index + 1
        return hamming
    raise ValueError('The length of the DNA strands do not match')
