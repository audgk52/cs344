'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
'''

from tools.aima.probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# Compute P(Alarm | burglary and -earthquake) using the enumeration-ask and elimination-ask algorithms
print("P(Alarm | burglary and -earthquake)")
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
print(elimination_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())

'''
i. This computation solves the probability of alarm going off or not given that there is a burglary and no earthquake
'''

# Compute P(John | burglary and -earthquake) using the enumeration-ask and elimination-ask algorithms
print("\nP(John | burglary and -earthquake)")
print("Enumeration-ask -> " + enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
print("Elimination-ask -> " + elimination_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())

'''
ii. This computation solves the probability of John calling or not given that there is a burglary and no earthquake.
    In this case, alarm should be considered as a variable since it is bridging John Calls with burglary and earthquake.
'''

# Compute P(Burglary | alarm) using the enumeration-ask and elimination-ask algorithms
print("\nP(Burglary | alarm)")
print("Enumeration-ask -> " +enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
print("Elimination-ask -> " +elimination_ask('Burglary', dict(Alarm=T), burglary).show_approx())

'''
iii. This computation solves the probability of if there is a burglary or not given that alarm goes off. 
     In this case, earthquake should be considered as a variable since it influences the probability of alarm going off. 
'''

# Compute P(Burglary | John and Mary both call) using the enumeration-ask and elimination-ask algorithms
print("\nP(Burglary | John and Mary both call)")
print("Enumeration-ask -> " +enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
print("Elimination-ask -> " +elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

'''
iv. This computation solves the probability of if there is a burglary or not given that John and Mary both call. 
    In this case, all the possible variables (burglary, earthquake, alarm, John Calls, Mary Calls) should be considered 
    in the computation. 
'''
