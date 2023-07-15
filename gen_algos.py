# Algorithm characteristics:
# complexity - space, time
# input and output - values or variables accepted at the beginning, and answers/results at the end
# classification - serial, parallel, deterministic, non-deterministic, exactm, approximate
# Common Algorithms:
# search - find specific data in a structure
# sortin - take a set of data and place it into a specified order
# computational - given a specific set of data, calculate a new set
# collection - working with collections of data to perform a task, navigate the data, filter, etc.

# Euclid's Algo
# fina the GCD of 2 integers without leaving a reamainder
# STEPS:
# 1) for two integers a and b, where a>b, divide a by b
# 2) if the remainder, r, is 0, then stop--GCD is b
# 3) else, set a to b, b to r, and go back to first step and repeat
# process will stop when r is 0

def gcd(a,b):
    while (b != 0):
        a, b = b, (a % b)
    return a

print(gcd(60, 26))
print(gcd(20, 14))
