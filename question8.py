A = int(input('Enter the number of months:'))
def Saving(A):
    J = 300
    D = 1
    while A != 0:
        if D % 6 != 0:
           J += 100
           D += 1
           A -= 1
        elif D % 6 == 0:
             J += 500
             D += 1
             A -= 1
    return print(J)
Saving(A)
