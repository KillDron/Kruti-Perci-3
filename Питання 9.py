"""
Програма виграховує найбільший спільний дільник між двома числами
"""

def finder(n,m):
    if n > m:
        for i in range(m,0,-1):
            if n%i==0 and m%i==0:
                return print("Найбільший спільний дільник:",i)
    elif n < m:
        for i in range(n,0,-1):
            if n%i==0 and m%i==0:
                return print("Найбільший спільний дільник:",i)
    else:
        return print("Найбільший спільний дільник:",n)
finder(int(input("Введіть перше число:")),int(input("Введіть друге число:")))
