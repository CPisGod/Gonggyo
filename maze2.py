a = input()
can = True

for i in range(1,len(a)-3):
    if a[i+1] == 1 and a[i+2] == 1:
        can = False

if can == True: print("탈출 가능")
else: print("탈출 불가")
