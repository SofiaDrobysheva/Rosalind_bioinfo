# Counting nucleotides.

with open('DNA_nt/rosalind_dna.txt', 'r') as file:
    dna = file.read().replace('\n', '')

for i in dna: 
    print(i)

a = 0
c = 0
g = 0
t = 0

for i in dna:
    if i == "A":
        a += 1
    if i == "C":
        c += 1
    if i == "G":
        g += 1
    if i == "T":
        t += 1 

print(a, " ", c, " ", g, " ", t)


# Another approach 

for c in 'ACGT': print dna.count(c)

