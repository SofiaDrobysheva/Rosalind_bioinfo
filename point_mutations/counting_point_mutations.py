# import data 
with open('point_mutations/rosalind_hamm.txt') as file:
    lines = [line.rstrip() for line in file]

s0 = lines[0]
s1 = lines[1]

hd = sum(c1!=c2 for c1,c2 in zip(s0,s1))

# Here the Hamming distance is the number of mismatches

print(f'The Hamming distance is {hd}.')