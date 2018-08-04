from sys import stdin
import sys
sys.setrecursionlimit(10000)
n,m = map(int, stdin.readline().split())
p = [[False for i in range(n+1)] for j in range(n+1)]
visit = [False for i in range(n+1)]
def dfs(cnt):
    visit[cnt] = True
    for i in range(1,n+1):
        if (not visit[i]) and p[cnt][i]:
            dfs(i)

for _ in range(m):
    x,y= map(int,stdin.readline().split())
    p[x][y] = p[y][x] = True
TT = 0
for i in range(1,n+1):
    if not visit[i]:
        TT+=1
        dfs(i)

print(TT)
