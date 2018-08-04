a =input()
L = []
result = 0
for i in range(len(a)):
    if a[i]== '(':
        L.append(a[i])
    else:
        L.pop()
        if a[i-1] =='(':
            result+=len(L)
        else:
            result+=1
print(result)