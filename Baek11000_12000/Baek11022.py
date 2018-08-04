N = int(input())
for i in range(1,N+1):
    x,y = list(map(int, input().split()))
    print('Case #%d: %d + %d = %d' %(i,x,y,x+y))