N = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
dp =[0 for x in range(N+1)]
for i in range(1,N+1):
    maxDp = 0
    for j in range(i):
        if(arr[i]>arr[j]):
            maxDp = max(maxDp, dp[j])
    dp[i] = maxDp + arr[i]
print(max(dp))