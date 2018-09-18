from math import *

def pythag_ther(a,b):
    '''returns the hypotnuse of a right triangle
    >>> pythag_ther(3,4)
    5.0
    >>> pythag_ther(-2,5)
    5.39
    >>> pythag_ther(0,4)
    4.0
    >>> pythag_ther(1.1, 2.6)
    2.82
    >>> pythag_ther(-2,-2)
    2.83
    
    
    '''
    a = a * a
    b = b * b
    sums = a + b
    ans = sqrt(sums)
    ans = round(ans,2)
    
    return ans

def slope(x1,y1,x2,y2):
    '''returns the slope of 2 points
    >>> slope(0,1,0,3)
    Traceback (most recent call last):
        ...
    ValueError: denominator cannot equal 0
    >>> slope(1,2,3,4)
    1.0
    
    
    
    '''
    yans = (y1-y2)
    xans =(x1-x2)
    #if xans == 0:
      #  return ValueError:
    ans = round(ans,2)
    
    return ans

def arithmetic(a1,n,d):
    '''returns last number in an arithmetic sequence'''
    ans = a1+(d*(n-1))
    ans = round(ans,2)
    
    return ans

def sum_geometric(a,r,n):
    '''returns the sum of a geometric sequence'''   
    pass

def eccentricity_ellipse(a,b):
    pass

def velocity():
    pass
    
if __name__ =="__main__":
    import doctest
    doctest.testmod()
#main()