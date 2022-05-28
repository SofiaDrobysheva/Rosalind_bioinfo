k = 26 # AA
m = 17 # Aa
n = 27 # aa

population = [k,n,m]
tot = sum(population)
tot1 = tot-1

# calculating a probability of picking a pair of individuals and getting a dominant phenotype in their offspring 
prob_k = k/tot * (k-1)/tot1 +    k/tot * m/tot1            + k/tot *  n/tot1 
prob_m = m/tot * k/tot1     +    m/tot * (m-1)/tot1 * 0.75 + m/tot *  n/tot1 * 0.5
prob_n = n/tot * k/tot1     +    n/tot * m/tot1 * 0.5      + n/tot * (n-1)/tot1 * 0

prob_tot = prob_k + prob_m + prob_n

print(round(prob_tot, 5))