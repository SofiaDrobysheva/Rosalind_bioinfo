# """ Counting nucleotides. """

with open('/home/sofia/Desktop/Rosalind/Rosalind_bioinfo/DNA_nt/rosalind_dna.txt', 'r') as file:
    DNAi = file.read().replace('\n', '')

a = 0
c = 0
g = 0
t = 0

for i in DNAi:
    if i == "A":
        a += 1
    if i == "C":
        c += 1
    if i == "G":
        g += 1
    if i == "T":
        t += 1 

print(a, " ", c, " ", g, " ", t)
