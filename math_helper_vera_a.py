from math import *
from time import *


print('''W E L C O M E  T O
MATH HELPER''')
print('. . . . . . . . . . .')

def rerun():
            #either runs the program again or breaks
    print('Would you like to use another formula?')
    ans = input("Type [y] for yes or [n] for no: ")
    if ans.upper() == 'Y':
        print()
        main()
    elif ans.upper() == 'N':
        print('Thank you for using Math Helper... Goodbye')
        exit()
    else:
        print('Invalid Input')
        rerun()

def main():    
    '''The UI for math helper
'''    
    print('Please select a formula by typing its number')
    print('''(1) Pythagorean Theorem
(2) Slope
(3) Arithmetic Sequence (last term)
(4) Sum of Geometric Sequence
(5) Area of a Sector
(6) Quit''')
    print('=========================')
    while True:
        try:
            choices = {1,2,3,4,5,6}
            
            user = int(input('> '))
            if user in choices:
                if user == 1:
                    print('+ Pythagorean Theorem Selected +')
                    a = float(input('Enter length of side 1: '))
                    b = float(input('Enter length of side 2: '))
                    print()
                    print('The hypotenuse is {}'.format(pythag_ther(a,b)))
                    print('≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡')
                    sleep(1.5)
                    rerun()
                    main()
                                 
                if user == 2:
                    print('+ Slope Selected +')
                    x1 = float(input('Enter first x-coordinate: '))
                    y1 = float(input('Enter first y-coordinate: '))
                    x2 = float(input('Enter second x-coordinate: '))
                    y2 = float(input('Enter second y-coordinate: '))
                    print()
                    print('The slope is {}'.format(slope(x1,y1,x2,y2)))
                    print('≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡')
                    sleep(1.5)
                    rerun()     
                    main()
                                              
                if user == 3:
                    print('+ Arithmetic Sequence (last term) Selected +')
                    a1 = float(input('Enter the first term in the sequence: '))
                    d = float(input('Enter the common diffence: '))
                    n = float(input('Enter the nth term you want: '))
                    print()
                    print('The last term is {}'.format(arithmetic(a1,d,n)))
                    print('≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡')
                    sleep(1.5)
                    rerun()
                    main()
                                                 
                if user == 4:
                    print('+ Geometric Sum Selected +')
                    a = float(input('Enter the first term in the sequence: '))
                    r = float(input('Enter the common ratio: '))
                    n = float(input('Enter the number of terms: '))
                    print()
                    print('The sum of the terms is {}'.format(sum_geometric(a,r,n)))
                    print('≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡')
                    sleep(1.5)
                    rerun() 
                    main()
                    
                if user == 5:
                    print('+ Area of a Sector Selected +')
                    r = float(input('Enter the radius of the circle: '))
                    a = float(input('Enter the angle in degrees: '))
                    print()
                    print('The area of the sector is {}'.format(area_of_sector(r,a)))
                    print('≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡')
                    sleep(1.5)
                    rerun()
                    main()
                                
                if user == 6:
                    print('Thank you for using Math Helper... Goodbye')
                    break
                            
            else:
                print('Please enter a number 1->5')
        except Exception as e:
            print('▀■' *24 )
            print('Invalid Input: ' + str(e))
            print('■▀' *24 )
            main() 
    
      


def pythag_ther(a,b):
    '''returns the hypotenuse of a right triangle
    >>> pythag_ther(3,4)
    5.0
    >>> pythag_ther(-2,5)
    5.39
    >>> pythag_ther(0,4)
    Traceback (most recent call last):
        ...
    ValueError: Sides cannot have a length of 0
    >>> pythag_ther(1.1, 2.6)
    2.82
    >>> pythag_ther(-2,-2)
    2.83
    '''
    if a == 0 or b == 0:
        raise ValueError("Sides cannot have a length of 0")
        
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
    0.933
    
    '''
    yans = (y1-y2)
    xans =(x1-x2)
    if xans == 0:
        raise ValueError("denominator cannot equal 0")
    ans = yans / xans
    if ans == -0.0:
        ans = 0.0
    ans = round(ans,3)
    
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

def area_of_sector(r,a):
    '''calculates the area of a sector, and changes degrees to radian
    >>> area_of_sector(75,135)
    6626.8
    >>> area_of_sector(0,87)
    0.0
    >>> area_of_sector(14,0)
    0.0
    >>> area_of_sector(-12,131)
    Traceback (most recent call last):
        ...
    ValueError: cannot have a negative input
    >>> area_of_sector(20,72)
    251.33
    
'''
    if r < 0 or a < 0:
        raise ValueError("cannot have a negative input")

    a = a * pi / 180
    ans = .5*(r*r) * a
    
    
    return round(ans,2)    
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #main()


