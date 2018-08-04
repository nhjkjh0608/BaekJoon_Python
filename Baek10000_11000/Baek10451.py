import sys

def f(L):

    Length = len(L)
    visited = [False]* Length
    cycle = 0
    for i in range(Length):
        if visited[i] :
            continue
        else:
            cycle +=1
            idx = i
            while not visited[idx]:
                visited[idx] = True
                idx = L[idx]-1

    sys.stdout.write(str(cycle)+'\n')

for _ in range(int(sys.stdin.readline())):
    sys.stdin.readline()
    f(list(map(int, sys.stdin.readline().split())))