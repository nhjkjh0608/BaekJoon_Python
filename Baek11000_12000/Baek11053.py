N = int(input())
arr = list(map(int, input().split()))
dp = [0 for x in range(N)]
for i in range(N):
    min = 0
    for j in range(0,i):
        if arr[j]<arr[i]:
            min = max(min, dp[j])
    dp[i] = min+1
print(max(dp))