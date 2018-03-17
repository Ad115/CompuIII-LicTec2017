def useless(*args, **kwargs):
    print(args)
    print(kwargs)



def enumerator(start=0, step=(lambda i: i+1)):
    s = start
    
    def enum():
        s = step(s)
    # ---
    
    return enum
# ---


def enumerator(start=0, step=(lambda i: i+1)):
    s = start
    
    while True:
        s = step(s)
        yield s
# ---

enumerator = (i for i in range(100))
    

def memoize(f):
    cache = {}
    
    def memoized(arg):
        if arg in cache:
            return cache[arg]
        else:
            result = f(arg)
            cache[arg] = result
            return result
    # ---
    return memoized
# ---


def fib(n):
    """Return the n'th Fibonacci number"""
    
    if n < 0:
        # Not a valid number
        raise ValueError("Fibbonacci numbers are not defined for negative index")
    elif n in (0,1):
        # Base case
        return n
    else:
        return fib(n-1) + fib(n-2)
# ---

class Enumerator:
    def __init__(self, start=0, nextf=(lambda i: i+1)):
        self.state = start
        self.next = nextf
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.state = self.next(self.state)
        return self.state
    
e = Enumerator()
for i in e:     
    if i > 100: 
        break
    print(i)



