from collections import deque
F,D = map(int, input().split())
q = deque()
q.append((0,F))
LL = [False]*100001
k =B__1=B_0=B_1=0
while len(q) is not 0:
    B=q.popleft()
    if LL[B[1]] :
        continue
    else:
        LL[B[1]]= True

    k = B[0]
    if B[1] == D:
        print(k)
        exit()
    B__1, B_0,B_1 =B[1]-1,B[1]*2,B[1]+1
    if 0 <= B__1 and B__1 <=100000 :
        q.append((k+1,B__1))
    if 0 <= B_0 and B_0 <=100000:
        q.append((k+1,B_0))
    if 0<= B_1 and B_1<= 100000:
        q.append((k+1,B_1))

