# Question - 1: With a given integral number n, write a function to generate a dictionary that
# contains (i, i*i) such that is an integral number between 1 and n (both included).
# and then the program should return the dictionary.

def squareOfNumbers(n):
    if n < 0 or n > 100:
        return
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    return d