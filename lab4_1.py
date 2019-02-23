'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013
'''

from tools.aima.probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|catch = T)
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)

print(PC.show_approx())


''' 
Hand-work summary 
P(Cavity | catch) = <P(cavity|toothache), P(-cavity|toothache)>

i. Probability of cavity & catch = True / Probability of catch = True
    = (0.108 + 0.072) / (0.108 + 0.072 + 0.016 + 0.144)
    = 0.529
    
ii. Probability of -cavity & catch / Probability of catch = True
    = 1 - 0.529
    = 0.471
    
<0.529. 0.471>
'''





'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by Lab4, flipping coins.
It is based on the code from AIMA probability.py.

'''


# The Joint Probability Distribution of flipping 2 coins
P1 = JointProbDist(['Coin1', 'Coin2'])
# True: Head, False: Tail
T, F = True, False

P1[T, T] = 0.25; P1[T, F] = 0.25
P1[F, T] = 0.25; P1[F, F] = 0.25

# Compute P(Coin2|coin1 = heads)
PC1 = enumerate_joint_ask('Coin2', {'Coin1': T}, P1)

print(PC1.show_approx())


'''
Hand-work summary 
P(Coin2 | coin1 = heads) = 

i. Probability of coin2 & coin1 = heads / Probability of coin1 = heads
    = 0.25 / (0.25 + 0.25) = 0.5
ii. Probability of coin2 = tail & coin1 = heads / Probability of coin1 = heads
    = 1 - 0.5 
    = 0.5

<0.5, 0.5>                             
                         
'''



'''
The full joint is generally not used in probabilistic systems, I believe because it is not always the case when the 
evidences for every case is given, and that is why we are using the Bayes rule with limited evidence given. 
'''