a = input()
can = True
b = a.split('1')

for i in range(1,int(len(b))-1):
    if int(len(b[i])) > 1:
        can = False

if can == True: print("탈출 가능")
else: print("탈출 불가")
