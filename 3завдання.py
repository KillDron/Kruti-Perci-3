string = str(input())
distinct = []
for char in string[::]:
    if char not in distinct:
        distinct.append(char)
print(len(distinct))
