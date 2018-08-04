import sys
N = int(sys.stdin.readline())
L = sys.stdin.readline().split()
# def pal(a,b):
#     global L
#     while a<b:
#         if L[a] != L[b]:
#             sys.stdout.write("0\n")
#             return
#         a+=1
#         b-=1
#     else:
#         sys.stdout.write("1\n")
#
#
# for _ in range(int(sys.stdin.readline())):
#     a, b = map(int, sys.stdin.readline().split())
#     pal(a-1,b-1)
dp = [[0 for i in range(N)]for j in range(N)]
for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if L[i]== L[i+1]:
        dp[i][i+1]= dp[i+1][i] = 1

for i in range(2,N):
    for j in range(N-i):

        k = j+i
        if L[j] == L[k] and dp[j+1][k-1]==1:
            dp[j][k] = 1
for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(dp[a-1][b-1])+'\n')