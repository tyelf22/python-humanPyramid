""" Tyson Elfors
5/18/20
CS-1410
Project 1 - Human Pyramid 
"""
#imports
import time
import sys

#global vars
HITS = 0
CALLS = 0

def main():
    """ uses two functions to calculate and display how much weight each person would shoulder in a human
    pyramid assuming that everyone weighs 200lbs 
    """
    cache = {}
    startTime = time.perf_counter()

    def weightOn(r, c, weight = 200):
        """ Recursive function to calculate total weight each individual is shouldering """

        global CALLS
        CALLS = CALLS + 1

        if f'{r}:{c}' in cache:
            global HITS
            HITS = HITS + 1
            return cache.get(f'{r}:{c}')

        if r == 0:
            result = 0.0
            x = float(result)
            output = round(x, 2)
            return output
        elif c == 0:
            result = (weightOn(r - 1, c, weight) + weight) / 2
            x = float(result)
            output = round(x, 2)
            return output
        elif c == r:
            result = (weightOn(r - 1, c - 1, weight) + weight) / 2
            x = float(result)
            output = round(x, 2)
            return output
        else:
            result = weight + (weightOn(r - 1, c - 1, weight) / 2) + (weightOn(r - 1, c, weight) / 2)
            x = float(result)
            output = round(x, 2)
            return output

        
    def printTriangle(num):
        """ Properly displays the human pyramid and sets cache dictionary """
        for i in range(0, num):
            for j in range(0, i+1):
                cache[f'{i}:{j}'] = weightOn(i, j)
                print(weightOn(i, j), end = " ")
            print()

    
    printTriangle(int(sys.argv[1]))
    print("\n")
    print("Elapsed Time:", time.perf_counter() - startTime)
    print("Number of function calls: ", CALLS)
    print("Number of cache hits: ", HITS)
    
if __name__ == '__main__':
    main()


