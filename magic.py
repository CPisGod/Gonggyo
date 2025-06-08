n = int(input())
print("*"*n)

for i in range(n-2):
    print("*",end='')
    for j in range(n-2):
        if i == j:
            print("*",end='')
        elif i+j == n-3:
            print("*",end='')
        elif i % 2 == 1 and i & j and i+j & n-3:
            print("*",end='')
        elif i % 2 == 1 and i & j and i+j & n-3:
            print("*",end='')
        elif j % 2 == 1 and i & j and i+j & n-3:
            print("*",end='')
        elif j % 2 == 1 and i & j and i+j & n-3:
            print("*",end='')
        else: print(" ",end='')
    print("*")

print("*"*n)
