from math import *

def pythag_ther(a,b):
    '''returns the hypotnuse of a right triangle
    >>> pythag_ther(3,4)
    5.00
    
    
    
    
    '''
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
    
if __name__ =="__main__":
    import doctest
    doctest.testmod()
#main()