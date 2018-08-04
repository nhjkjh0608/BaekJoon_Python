dp = [0 for x in range(100001)]
N = int(input())
for i in range(1,N+1):
    j =1
    while j*j<=i:
        if dp[i]> dp[i-j*j]+1 or dp[i] ==0:
            dp[i] = dp[i-j*j]+1
        j+=1
print(dp[N])
