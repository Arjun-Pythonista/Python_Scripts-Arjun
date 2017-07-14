# Powersets
# Task 3: By -Arjun
# Powersets
# Creating a program that has the ability to expand a powerset from a set of numbers (or characters)

def p(s):
    powerset = set()
    for i in range(2**len(s)):
        subset = tuple([x for j,x in enumerate(s) if (i >> j) & 1])
        powerset.add(subset)
    return powerset
p([1,2,3])