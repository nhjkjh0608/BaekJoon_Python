Input = sorted([int(input()) for x in range(9)])
check = sum(Input)-100
for i in range(8,1,-1):
    for j in range(i-1,0,-1):
        if Input[i]+ Input[j]<check:
            break
        elif Input[i]+ Input[j]==check:
            for idx in range(0, 9):
                if idx is not i and idx is not j:
                    print(Input[idx])
            exit()
