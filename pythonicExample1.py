################################### 1 ##################################
"""

Give me a function that takes a number and returns True if it is even
and False otherwise

Usage:
>>> isEven( 2 )
True

>>> isEven( 3 )
False

"""
#-----------------------------------------------------------------------
def isEven(n):
    if n%2 == 0:
        return True
    else:
        return False
#-----------------------------------------------------------------------
def isEven(number):
    return (number % 2) == 0
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
isEven = lambda n: (n % 2) == 0
#-----------------------------------------------------------------------

################################### 2 ##################################
"""

Give me a function that takes a list of numbers and returns True if any
is even and False otherwise

Usage:
>>> anyEven( [1,2,5,6] )
True

>>> anyEven( [1,3,5,7] )
False

"""

#-----------------------------------------------------------------------
def anyEven(numbers):
    for number in numbers:
        if isEven(number):
            return True
        else:
            return False
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
def anyEven(numbers):
    areEven = [ isEven(i) for i in numbers ]
    return (True in areEven)
#-----------------------------------------------------------------------

################################### 3 ##################################
"""

Give me a function that takes a list of numbers and returns only the
even ones

Usage:
>>> evensOnly( [1,2,5,6] )
[2,6]

"""

#-----------------------------------------------------------------------
def evensOnly(numbers):
    evens = []
    for number in numbers:
        if isEven(number):
            evens.append(number)
    return evens
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
def evensOnly(numbers):
    return [ i for i in numbers if isEven(i)]
#-----------------------------------------------------------------------

################################### 4 ##################################
"""

Give me a function that takes a list of numbers and returns only the
even ones, divided by two.

Usage:
>>> halveEvensOnly( [1,2,5,6] )
[1,3]

"""
#-----------------------------------------------------------------------
def halveEvensOnly(nums):
    return [i/2 for i in nums if isEven(i)]
#-----------------------------------------------------------------------

########################################################################

print('Beautiful is better than ugly.')
