# Importing data 

with open('DNA_to_RNA/rosalind_rna.txt', 'r') as file:
    dna = file.read().replace('\n', '')

# Solution 1

rna = []

for nt in dna:
    if nt == "T":
        rna.append('U')
    else:
        rna.append(nt)

print('solution_1:', ''.join(map(str, rna)))


# Solution 2

print('solution_2:', dna.replace("T", "U"))