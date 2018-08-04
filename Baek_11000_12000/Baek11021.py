N = int(input())
for i in range(1,N+1):
    print('Case #%d: %d' %(i,sum(list(map(int, input().split())))))