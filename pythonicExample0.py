################################### 1 ##################################
"""

Create a list with 10 entries all equal to 22

"""
#-----------------------------------------------------------------------
l = [22, 22, 22, 22, 22, 22, 22, 22, 22, 22]
#-----------------------------------------------------------------------
l = []
for i in range(10):
    l.append(22)
#-----------------------------------------------------------------------
l = []
for i in range(10):
    l = l + [22]
#-----------------------------------------------------------------------
l = []
for i in range(10):
    l += [22]
#-----------------------------------------------------------------------
l = [ 22 for i in range(10) ]
#-----------------------------------------------------------------------
l = [22]*10
#-----------------------------------------------------------------------
################################### 2 ##################################
"""

Create a list with 100 entries all equal to "Hola mundo"

"""
#-----------------------------------------------------------------------
l = []
for i in range(100):
    l += ["Hola mundo"]
#-----------------------------------------------------------------------
l = [ "Hola mundo" for i in range(100) ]
#-----------------------------------------------------------------------
l = ["Hola mundo"] * 100
#-----------------------------------------------------------------------
################################### 3 ##################################
"""

Create a list with all the numbers from 0 to 1000

"""
#-----------------------------------------------------------------------
l = []
for i in range(1001):
    list.append(i)
#-----------------------------------------------------------------------

l = [ i for i in range(1001) ]
#-----------------------------------------------------------------------
l = list( range(1001) )
#-----------------------------------------------------------------------
################################### 4 ##################################
"""

Create a list with all the numbers from one to 101

"""
#-----------------------------------------------------------------------
list = []
for i in range(101):
    list.append(i+1)
#-----------------------------------------------------------------------
list = [ i+1 for i in range(101) ]
#-----------------------------------------------------------------------
################################### 5 ##################################
"""

Create a list with all the numbers from 100 to zero

"""
#-----------------------------------------------------------------------
l = [ i for i in range(100, -1, -1) ]
#-----------------------------------------------------------------------
l = []
for i in range(100):
    l.append(100-i)
#-----------------------------------------------------------------------
l = [ 100-i for i in range(100) ]
#-----------------------------------------------------------------------
################################### 6 ##################################
"""

Create a list with the squares of all even numbers from 0 to 100

"""
#-----------------------------------------------------------------------
l = []
for i in range(100):
    if (i%2) == 0:
        l.append(i**2)
#-----------------------------------------------------------------------
l = [ i**2 for i in range(0,1001, 2) ]
#-----------------------------------------------------------------------
l = [  i**2 for i in range(100) if (i%2)==0]
#-----------------------------------------------------------------------