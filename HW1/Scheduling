'''
This program shows the schedule of CS courses with non-conflicting condition with faculty, time, and classroom
'''


from csp import parse_neighbors, CSP, min_conflicts

def Scheduling():

    Courses = ['cs108', 'cs112', 'cs214', 'cs344', 'cs212']
    Faculty = ['Schuurman', 'Adams', 'Vanderlinden', 'Plantinga']
    Timeslot = ['MWF9', 'MWF1030', 'TTH9', 'TTH1030']
    Rooms = ['NH253', 'SB382']
    Assignement = {'cs108':'Schuurman', 'cs112':'Adams', 'cs214': 'Adams', 'cs344': 'Vanderlinden', 'cs212': 'Plantinga'}
    # setting Courses as variable
    variable = Courses

    # domains lists all possible combination of course, faculty, time, and room
    domains = {}
    for course in Courses:
        # making the course as the key to the domain dictionary
        domains[course] = []
        for prof in Faculty:
            for time in Timeslot:
                for room in Rooms:
                    # appending professor, time slot, room number to the course
                    domains[course].append([prof, time, room])

    # creating neighbors with each class to be neighbor to all other classes
    neighbors = parse_neighbors(""" cs108:cs112; cs108:cs212; cs108:cs344; cs108:cs214; cs112:cs212; cs112:cs344;
                cs112:cs214; cs212:cs344; cs212:cs214; cs344:cs212""", variable)

    def scheduling_constraints(courseA, a, courseB, b):
        # check if the assigned professor to the course and the professor in domain value are the same
        if (a[0] != Assignement[courseA]) or (b[0] != Assignement[courseB]):
            return False
        # check if the faculty and time slot are the same for different classes, then return false
        if a[0] == b[0] and a[1] == b[1]:
            return False
        # check if the time slot and the room number are the same for different classes, then return false
        if a[1] == b[1] and a[2] == b[2]:
            return False
        return True
    return CSP(variable, domains, neighbors, scheduling_constraints)

# printing out the result
result = min_conflicts(Scheduling())
print(result)



