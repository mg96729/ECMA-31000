import numpy as np
import scipy.stats as st

p = 0.99
z_score = st.norm.ppf(1-(1-p)/2)

def one_trial_n_iid_draws(n, p):
    return np.random.binomial(n, p, 1)

def one_trial_n_iid_draws_ci(n,p,z):
    s = np.random.binomial(n, p, 1)
    s = s[0]
    m = s/n
    ssq = np.sqrt((m*(1-m)/n))

    l = m - z*ssq
    u = m + z*ssq

    return (l, u)

def many_trial_n_iid_draws_tf(n, p, z, t):
    success = 0
    for i in range(t):
        (l, u) = one_trial_n_iid_draws_ci(n, p, z)
        if l < p < u:
            success +=1

    return success/t
'''
print(one_trial_n_iid_draws_ci(25, 0.4, z_score))

'''

for n in [25, 50, 100, 250, 500, 1000, 2000]:
    print("1000 trials with n =" + str(n) + ": " +str(many_trial_n_iid_draws_tf(n, 0.4, z_score, 1000)))




