#task 1
def encrypted():
    message=input("Напишіть своє повідомлення для шифрування: ")
    t=message[::2] 
    n=message[1::2] 
    return print(t+n)
encrypted()



#Task 2
def decr():
    message=input("Напишіть своє повідомлення для розшифрування: ")
    length=len(message) 
    hl=(length+1)//2 
    t=message[:hl]
    n=message[hl:] 
    decrypt=''
    if length%2==0:
        for i in range (hl): 
            join=t[i]+n[i]
            decrypt=decrypt+join
    else:
        for i in range (1,hl+1): 
            neparne=i-1 
            join=t[neparne:i]+n[neparne:i]
            decrypt=decrypt+join
    return print(decrypt)
decr()
