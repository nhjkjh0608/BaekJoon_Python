
import sys
dp =[]
tmp =[]
def solve(p,x,y):
    if x ==y:
        return tmp[x] if p==0 else 0

    t = dp[p][x][y]
    if t!=-1:
        return t
    if p ==0:
        dp[p][x][y] = max(solve(p^1,x+1,y)+tmp[x], solve(p^1,x,y-1)+tmp[y])
    else:
        dp[p][x][y] = min(solve(p^1, x+1,y),solve(p^1,x,y-1))
    return dp[p][x][y]
N = int(sys.stdin.readline())
for ttt in range(N):

    ttttt = int(sys.stdin.readline())
    dp = [[[-1 for ___ in range(1001)] for __ in range(1001)] for _ in range(2)]

    tmp = [0 for i in range(1001)]
    idx = 0
    for k in map(int, sys.stdin.readline().split()):
        tmp[idx] = k
        idx+=1

    sys.stdout.write(str(solve(0,0,ttttt-1))+"\n")

