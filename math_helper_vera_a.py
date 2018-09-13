from math import *

def pythag_ther(a,b):
    '''returns the hypotnuse of a right triangle'''
    a = a * a
    b = b * b
    sums = a + b
    ans = sqrt(sums)
    
    return "{:.2f}".format(ans)

def main():    
    print(pythag_ther(3,4))
main()