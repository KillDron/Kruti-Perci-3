A = int(input("Введіть число:"))
L = [2,3,5,7]
def P(x):
    if ((x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0) and x not in L) == True:
        return print('Число не просте')
    elif x == 1 or x == 0 :
       return print('Число не просте')
    else:
        return print('Число просте')
P(A)