from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
indegree = [0 for i in range(N+1)]
indegree[0] =-1
connected = [[] for i in range(N+1)]
for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    connected[a].append(b)
    indegree[b]+=1
q = deque()
for i in range(1,N+1):
    if indegree[i] == 0:
        q.append(i)
re = []
while len(q)!= 0:
    L = len(q)
    for num in range(L):
        tmp = q.popleft()
        re.append(tmp)
        indegree[tmp]-= 1
        for con in connected[tmp]:
            indegree[con]-=1
            if indegree[con]==0:
                q.append(con)

for i in map(str,re):
    sys.stdout.write(i+" ")