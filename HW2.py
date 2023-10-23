import numpy as np

p = 0.4 # probability of each draw
n = 100 #number of tosses in each trial
t = 250 #number of trials

ep = 0.1 #the radius of confidence interval

number_of_good_ci = 0 #the total number of CI out of 250 trials that captures true p
for i in range(t):
    s_i = np.random.binomial(n, p, 1)
    avg_s_i = sum(s_i) / (n)
    if p > avg_s_i-ep and p<avg_s_i+ep:
        number_of_good_ci += 1

print([i for i in range(10, -1, -1)])
