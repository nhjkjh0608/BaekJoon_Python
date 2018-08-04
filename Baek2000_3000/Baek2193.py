N = int(input())
dp= [[0 for i in range(2)]for i in range(N)]
dp[0] = [0,1]
for i in range(1,N):
    dp[i][0] = dp[i-1][0]+ dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(sum(dp[-1]))
