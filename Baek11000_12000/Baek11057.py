N = int(input())
dp = [[1 for x in range(10)]for y in range(N)]
for i in range(1,N):
    tmpsum =0
    for j in range(10):
        tmpsum+= dp[i-1][j]
        tmpsum= tmpsum%10007
        dp[i][j] = tmpsum
print(sum(dp[-1])%10007)