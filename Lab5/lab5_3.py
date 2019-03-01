"""
This modle implements the Bayesian network show in the text, Exercise 5.3
It's taken from the AIMA Python code
"""
from tools.aima.probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - tow-cause happiness example
happiness = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])

# a. i) Compute P(Raise | sunny) using the enumeration-ask and elimination-ask algorithms
print("P(Raise | sunny)")
print("Enumeration-ask -> " + enumeration_ask('Raise', dict(Sunny=T), happiness).show_approx())
print("Elimination-ask -> " + elimination_ask('Raise', dict(Sunny=T), happiness).show_approx())

# a. ii) Compute P(Raise | happy and sunny) using the enumeration-ask and elimination-ask algorithms
print("\nP(Raise | happy and sunny)")
print("Enumeration-ask -> " + enumeration_ask('Raise', dict(Happy=T, Sunny=T), happiness).show_approx())
print("Elimination-ask -> " + elimination_ask('Raise', dict(Happy=T, Sunny=T), happiness).show_approx())

'''
Hand-work
a. i) P(Raise | sunny) 
      = <P(raise | sunny), P(-raise | sunny)>
      = <0.01 * 0.7, 0.99 * 0.7>
      = <0.007, 0.693>
      = <0.001, 0.99)

    //Bold P and upper case R, you need to consider both raise and -raise given that it is sunny. 
    For raise = T, probability of getting raise is 0.01 and being sunny is 0.7. 
    For raise = F, probability of not getting raise is 0.99 and being sunny is 0.7. 

   ii) P(Raise | sunny ^ happy)
       = <P(raise | sunny ^ happy), P(-raise | sunny ^ happy)>
       = <0.01 * 0.7 * 1.0, 0.99 * 0.7 * 0.7>
       = <0.007, 0.485>
       = <0.0142, 0.986>

    //Bold P and upper case R, you need to consider both raise and -raise given that it is sunny and happy. 
    For raise = T, probability of getting raise is 0.01, being sunny 0.7, being happy 1.0.
    For raise = F, probability of not getting raise is 0.99, being sunny 0.7, being happy 0.7.
'''

# b. i) Compute P(Raise | happy) using the enumeration-ask and elimination-ask algorithms
print("\nP(Raise | happy)")
print("Enumeration-ask -> " + enumeration_ask('Raise', dict(Happy=T), happiness).show_approx())
print("Elimination-ask -> " + elimination_ask('Raise', dict(Happy=T), happiness).show_approx())

# b. ii) Compute P(Raise | happy and -sunny) using the enumeration-ask and elimination-ask algorithms
print("\nP(Raise | happy and -sunny)")
print("Enumeration-ask -> " + enumeration_ask('Raise', dict(Happy=T, Sunny=F), happiness).show_approx())
print("Elimination-ask -> " + elimination_ask('Raise', dict(Happy=T, Suuny=F), happiness).show_approx())


'''
At first, it did not make sense to me to measure probability of getting raise depending on being happy or/and sunny. 
Suspected that there will be not much correlation between raise and being happy & sunny at all, it turns out to have
rare chance of getting raise while one is happy and weather is nice. Another thing to note here is that for 
P(Raise | happy and -sunny), enumeration_ask and elimination_ask return different result unlike other probabilities. 
'''
