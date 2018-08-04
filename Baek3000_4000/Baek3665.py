import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    L = [[0 for j in range(N+1)]for i in range(N+1)]
    indegree = [0 for j in range(N+1)]
    Li = list(map(int, sys.stdin.readline().split()))
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            L[Li[i-1]][Li[j-1]] = 1
            indegree[Li[j-1]]+=1
    # print(indegree)
    for __ in range(int(sys.stdin.readline())):
        m,n = map(int, sys.stdin.readline().split())
        if L[m][n]== 1:
            L[m][n] = 0
            L[n][m] = 1
            indegree[n]-=1
            indegree[m]+=1
        else:
            L[m][n] = 1
            L[n][m] = 0
            indegree[n]+=1
            indegree[m]-=1
    Q = deque()
    for i in range(1, N+1):
        if indegree[i] ==0:
            Q.append(i)
    # print(Q)

    rank = []
    ans = 0
    for ___ in range(N):
        if len(Q)==0:
            ans = -1
            break
        if len(Q)>1:
            ans = -2
            break
        Next = Q.popleft()
        rank.append(Next)
        for i in range(1, N+1):
            if L[Next][i] ==1:
                indegree[i]-=1;
                if indegree[i] ==0:
                    Q.append(i)
    if ans ==0:
        sys.stdout.write(" ".join(map(str, rank))+"\n")
    elif ans == -1:
        sys.stdout.write("IMPOSSIBLE\n")
    else:
        sys.stdout.write("?\n")