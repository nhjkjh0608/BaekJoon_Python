N = int(input())
arr = list(map(int, input().split()))
dp = [0 for x in range(N)]
for i in range(N):
    min = 0
    for j in range(0,i):
        if arr[j]<arr[i]:
            min = max(min, dp[j])
    dp[i] = min+1
dp2 = [0 for x in range(N)]
arr.reverse()
for i in range(N):
    min = 0
    for j in range(0,i):
        if arr[j]<arr[i]:
            min = max(min, dp2[j])
    dp2[i] = min+1
Length = len(dp)
print(max([dp[i]+ dp2[Length-1-i] for i in range(Length)])-1)
