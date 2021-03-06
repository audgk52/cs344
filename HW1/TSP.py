"""
This program shows the shortes path way starting and ending at the same city 
"""
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
import random



class TspProblem(Problem):
    def __init__(self, initial, distance):
        self.initial = initial
        self.distance = distance

    def actions(self, state):
        actions = []
        for i in range(3):
            # randomly sample pairs of 2 cities and append them into actions array
            pair = random.sample(range(1, len(state) - 1), 2)
            actions.append(pair)
        return actions

    def result(self, state, move):
        new_state = state[:]
        city_1 = new_state[move[0]]
        city_2 = new_state[move[1]]
        new_state[move[0]] = city_2
        new_state[move[1]] = city_1
        return new_state

    def value(self, state):
        total_dist = 0
        for i in range(0, len(state) - 1):
            c = [state[i], state[i+1]]
            c.sort()
            total_dist += self.distance[tuple(c)]
        return -1 * total_dist


if __name__ == '__main__':
    # starting at 0 and ending at 0
    cities = [0, 1, 2, 3, 4, 5, 6, 0]

    # randomized hardcoded distances between cities
    distances = {(0,1) : 1, (0,2) : 2, (0,3) : 4, (0,4) : 10, (0,4) : 8, (0,5) : 15, (0,6) : 11, (1,2) : 3, (1,3): 14,
                 (1,4) : 19, (1,5) : 3, (1,6) : 5, (2,3) : 5, (2,4) : 18, (2,5) : 9, (2,6) : 16, (3,4) : 33, (3,5): 11,
                 (3,6) : 57, (4,5) : 66, (4,6): 29, (5,6) : 21}

    # setting up the p with initial as cities and distance as distances
    p = TspProblem(cities, distances)

    # Hill-Climbing solution and value
    hill_solution = hill_climbing(p)
    print('Hill_climbing -> \t' + 'Solution: ' + str(hill_solution) + '\tValue: ' + str(p.value(hill_solution)))

    # Simulated-Annealing solution and value
    annealing_solution = simulated_annealing(p,exp_schedule(k=20, lam=0.005, limit=10000))
    print('Simulated_annealing -> \t' + 'Solution: ' + str(annealing_solution) + '\tValue: ' + str(p.value(annealing_solution)))



