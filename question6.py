import math

def number_e(n):
    e = 0
    m = 1
    for k in range(m, n+1):
        e += 1/math.factorial( m )
        m += 1
    return e
n = int(input('Enter the number n: '))
print( number_e (n) )