# Import data

with open('gc_content/rosalind_gc.txt') as file:
    lines = file.readlines()

# Formatting the FASTA file

name_seq = dict()

for line in lines:

    if line.startswith('>'): 
        title = line[1:].strip()
        name_seq[title] = '' 

    else: 
        name_seq[title] += ''.join(line.split()) # getting rid of multi-FASTA format

# Calculatinf GC-content and fitting to the needed format

output = []

for name, seq in name_seq.items():
    gc_cont = "%.4f" % round(((seq.count('C') + seq.count('G')) / len(seq) * 100), 4) # allowed default error of 0.001, thus 4 decimals after the . 
    print(name, gc_cont)
    output.append(name) 
    output.append(gc_cont)

# Saving to file

with open('gc_content/gc_output.txt', 'w') as output_file:
    for element in output:
        output_file.write(str(element) + '\n')
