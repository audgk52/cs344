'''
This modle implements the Bayesian network show in the text, Exercise 5.2
It's taken from the AIMA Python code
'''


from tools.aima.probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - two-test cancer example
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2})
])

# a. Compute P(Cancer | positive results on both test) using the enumeration-ask and elimination-ask algorithms
print("P(Cancer | positive results on both test)")
print("Enumeration-ask -> " + enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
print("Elimination-ask -> " + elimination_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())


# b. Compute P(Cancer | a positive result on test 1, but a negative result on test 2)
print("\nP(Cancer | a positive result on test 1, but a negative result on test 2)")
print("Enumeration-ask -> " + enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())
print("Elimination-ask -> " + elimination_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())


'''Hand-work
a. P(Cancer | t1 = T, t2 = T) 
= <P(cancer | t1 = T, t2 = T), P(-cancer | t1 = T, t2 = T)> 
= <(0.01 * 0.9 * 0.9), (0.99 * 0.2 * 0.2)>
= <0.0081, 0.0396>
= <0.17, 0.83>

//Bold P and upper case C, you need to consider both cancer and -cancer given that t1 and t2 gets the positive result. 
For cancer = T, both test 1 and 2 have 0.9 probability of getting it right.
For cancer = F, both test 1 and 2 have 0.2 probability of getting positive results.  


b. P(Cancer | t1 = T, t2 = F)
= <P(cancer | t1 = T, t2 = F), P(-cancer | t1 = T, t2 = F)
= <(0.01 * 0.9 * 0.1), (0.99 * 0.2 * 0.8)>
= <0.006, 0.994>

//Bold P and upper case C, you need to consider both cancer and -cancer given that t1 getting positive and t2 getting 
negative result.
For cancer = T, test 1 has 0.9 getting positive, and test 2 has 0.1 getting negative result. 
For cancer = F, test 1 has 0.2 getting positive, and test 2 has 0.8 getting negative result. 
'''


