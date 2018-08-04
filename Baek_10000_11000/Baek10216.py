# 언어의 한계로 시간초과 나는문제
# 같은 알고리즘으로 C 나 Java 로 돌리면 풀린다.
import sys
from collections import deque
def con(A, B):
    R = ((A[0]- B[0])**2 + (A[1]-B[1])**2)**0.5
    if R<=A[2]+ B[2]:
        return True
    else:
        return False

N = int(sys.stdin.readline())


for _ in range(N):
    num = int(sys.stdin.readline())
    L= []
    for __ in range(num):
        L.append(list(map(int, sys.stdin.readline().split())))
    visited = [False]* num
    connected = [[False for i in range(num)] for j in range(num)]
    for i in range(num):
        for j in range(i, num):
            connected[i][j] = connected[j][i] = con(L[i],L[j])

    ans = 0
    for i in range(num):
        if visited[i] :
            continue
        q = deque()

        q.append(i)
        while len(q) != 0:
            node = q.popleft()
            if visited[node]:
                continue
            else:
                visited[node] = True
            for j in range(num):
                if connected[node][j] and not visited[j]:
                    q.append(j)
                    visited[j] = True
        ans +=1
    sys.stdout.write(str(ans)+'\n')
