# importing data

with open('reverse_comp/rosalind_revc.txt', 'r') as file:
    dna = file.read().replace('\n', '')

# solution 1

seq  = []

for i in dna:
    for j in i:
        seq.append(j)

nt_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

rc_seq = [nt_dict[base] for base in seq]

print(''.join(map(str, rc_seq[::-1])))


# solution 2 (borrowed)

print(dna[::-1].translate(str.maketrans('ACGT', 'TGCA')))