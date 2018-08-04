N, L = map(lambda x: int(x), input().split())
List = [int(x) for x in input().split()]
from collections import deque
q = deque()
for i in range(0,len(List)):
    if len(q)==0:
        q.appendleft(List[i])
    else:
        while len(q)!= 0 and q[len(q)-1]>List[i]:
            q.pop()
        q.append(List[i])
    if i>=L:
        if(q[0] == List[i-L]):
            q.popleft()
    print(q[0], end = " ")
#Using tuple costs less memory
