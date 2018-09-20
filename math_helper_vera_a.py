from math import *

def main():
    print('''W E L C O M E  T O
MATH HELPER''')
    print('. . . . . . . . . ')
    print('Please select a formuala by typing its number')
    a = int(input('''(1) Pythagorean Theorem
(2) Slope
(3) Arithmetic Sequence
(4) Sum of Geometric Sequence
(5) Eccentricity of Ellipse
>  '''))
    while True:
        if a == 1 or 2 or 3 or 4 or 5:
            print("ERROR: Please input a valid number")
            a = input('> ')
        else:
            break




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
    >>> slope(1,2,4,2)
    0.0
    >>> slope(5,7,6,1)
    -6.0
    >>> slope(3,-9,-2,4)
    -2.6
    >>> slope(-2,-2,13,12)
    0.93
    
    '''
    yans = (y1-y2)
    xans =(x1-x2)
    if xans == 0:
        raise ValueError("denominator cannot equal 0")
    ans = yans / xans
    if ans == -0.0:
        ans = 0.0
    ans = round(ans,2)
    
    return ans

def arithmetic(a1,d,n):
    '''returns last number in an arithmetic sequence
    >>> arithmetic(3,0,4)
    3
    >>> arithmetic(12,4,6)
    32
    >>> arithmetic(1.1,-2,6)
    -8.9
    >>> arithmetic(1,7,0)
    Traceback (most recent call last):
        ...
    ValueError: number of terms cannot equal 0
    >>> arithmetic(12,5,23)
    122
'''
    if n == 0:
        raise ValueError("number of terms cannot equal 0")
    ans = a1+(d*(n-1))
    ans = round(ans,4)
    
    return ans

def sum_geometric(a,r,n):
    '''returns the sum of a geometric sequence
    >>> sum_geometric(1,2,8)
    255.0
    >>> sum_geometric(-2.1,1.1,4)
    -9.75
    >>> sum_geometric(3,0,3)
    3.0
    >>> sum_geometric(1,3,0)
    0.0
    >>> sum_geometric(1,1,1)
    Traceback (most recent call last):
        ...
    ValueError: 'r' cannot be 1
'''   
    if r == 1:
        raise ValueError("'r' cannot be 1")
    num = a*(1 - (r**n))
    den = 1 - r
    ans = num / den
    if ans == -0.0:
        ans = 0.0
    ans = round(ans,2)
    
    return ans

def eccentricity_ellipse(a,b):
    e = ((b / a)**2)
    e = sqrt((1-e))
    e = round(e,2)
    return e


    
if __name__ =="__main__":
    #import doctest
    #doctest.testmod()
    main()