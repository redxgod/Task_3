# CSP: Subject Timetable Scheduling

subjects = ["Maths", "Python", "DBMS", "AI"]

time_slots = ["9:00 AM", "11:00 AM", "2:00 PM"]

# Constraints: subjects that cannot have the same time
constraints = [
    ("Maths", "Python"),
    ("DBMS", "AI")
]

assignment = {}


def is_valid(subject, time):
    # Check whether this time is already assigned
    # to a conflicting subject
    for s1, s2 in constraints:
        if subject == s1 and s2 in assignment:
            if assignment[s2] == time:
                return False

        if subject == s2 and s1 in assignment:
            if assignment[s1] == time:
                return False

    return True


def backtracking(index):
    if index == len(subjects):
        return True

    subject = subjects[index]

    for time in time_slots:
        if is_valid(subject, time):
            assignment[subject] = time

            if backtracking(index + 1):
                return True

            del assignment[subject]

    return False


# Solve CSP
if backtracking(0):
    print("Final Timetable")
    print("----------------")

    for subject in subjects:
        print(subject, "->", assignment[subject])
else:
    print("No solution found")