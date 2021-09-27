A = "abcdefghijklmnopqrstuvwxyz"
n = 0
while n < len(A):
    print(A)
    A = A[1:100] + A[0]
    n += 1
"""    
A = str(input("Введіть від 0 до 100 символів з пробілом в кінці:"))
n = 0
while n < len(A):
    print(A)
    A = A[1:100] + A[0]
    n += 1
    
A = " ♦ ♣ ♥ ♠ ♦ ♣ ♥ ♠ ♦ ♣ ♥ ♠ ♦ ♣ ♥ ♠"
n = len(A)/2
while n < len(A):
    print(A)
    A = A[1:100] + A[0]
    n += 1
"""
