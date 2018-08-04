def solve(x):
    return x+ sum([int(y) for y in str(x)])

N = int(input())
for i in range(N- len(str(N))*9, N):
    if solve(i) == N:
        print(i)
        break
else:
    print(0)