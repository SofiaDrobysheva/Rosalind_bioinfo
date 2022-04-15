# Rabbits and Recurrence Relations 

k = int(input('How many pair of rabbits are born per rabbit couple? '))
n = int(input('What month do you want to calculate the rabbits for? '))

# k = 2
# n = 28

babi = [1]
mature = [0]
total = []

for i in range(n):
    t = babi[i] + mature[i] 
    total.append(t)

    babi.append(mature[i]*k)
    mature.append(babi[i]+mature[i])

print('The total number of rabbits at month', n,' is:', total[-1])