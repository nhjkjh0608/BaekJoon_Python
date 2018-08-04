import sys
L = [True]*10001
f = lambda x: sum(map(int, list(str(x))))+ x
for i in range(1,10001):
    t = f(i)
    while t<=10000 and L[t]:
        L[t] = False
        t = f(t)
for i in range(1,10001):
    if L[i]:
        sys.stdout.write(str(i)+'\n')

