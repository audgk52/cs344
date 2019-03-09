'''
This is a program to calculate the probability of each combination of weather conditions
'''

from tools.aima.probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14_12 - Weather
weatherA = BayesNet([
    ('Cloudy', '', 0.5),
    ('Rain', 'Cloudy', {T: 0.80, F: 0.20}),
    ('Sprinkler', 'Cloudy', {T: 0.10, F: 0.50}),
    ('WetGrass', 'Sprinkler Rain', {(T, T): 0.99, (T, F): 0.90, (F, T): 0.90, (F, F): 0.00})
])

# Compute P(Cloudy)
print('P(Cloudy)')
print("Enumeration-ask -> " + enumeration_ask('Cloudy', dict(), weatherA).show_approx())

# Compute P(Sprinkler | cloudy)
print('\nP(Sprinkler | cloudy)')
print("Enumeration-ask -> " + enumeration_ask('Sprinkler', dict(Cloudy=T), weatherA).show_approx())

# Compute P(Cloudy| the sprinkler is running and it’s not raining)
print('\nP (Cloudy | sprinker and -rain')
print("Enumeration-ask -> " + enumeration_ask('Cloudy', dict(Sprinkler=T, Rain=F), weatherA).show_approx())

# Compute P(WetGrass | it’s cloudy, the sprinkler is running and it’s raining)
print('\nP (WetGrass | cloudy and sprinkler and rain')
print("Enumeration-ask -> " + enumeration_ask('WetGrass', dict(Cloudy=T, Sprinkler=T, Rain=T), weatherA).show_approx())

# Compute P(WetGrass | it’s cloudy, the sprinkler is running and it’s raining)
print('\nP (WetGrass | cloudy and sprinkler and rain')
print("Enumeration-ask -> " + enumeration_ask('WetGrass', dict(Cloudy=T, Sprinkler=T, Rain=T), weatherA).show_approx())

# Compute P(Cloudy | the grass is not wet)
print('\nP (Cloudy | -wet grass)')
print("Enumeration-ask -> " + enumeration_ask('Cloudy', dict(WetGrass=F), weatherA).show_approx())
