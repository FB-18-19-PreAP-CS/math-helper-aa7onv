from math import *

def pythag_ther(a,b):
    '''returns the hypotnuse of a right triangle'''
    a = a * a
    b = b * b
    sums = a + b
    ans = sqrt(sums)
    
    return "{:.2f}".format(ans)

def slope(x1,y1,x2,y2):
    '''returns the slope of 2 points'''
    ans = (y1-y2)/(x1-x2)
    
    return "{:.2f}".format(ans)

def arithmetic(a1,n,d):
    '''returns last number in an arithmetic sequence'''
    ans = a1+(d*(n-1))
    
    return "{:.2f}".format(ans)

def sum_geometric(a,r,n):
    '''returns the sum of a geometric sequence'''
    pass
    
    

def main():    
    print(pythag_ther(3,4))
    print(arithmetic(2,10,2))
    
main()