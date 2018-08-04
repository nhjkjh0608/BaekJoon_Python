Case = int(input())
for tmp in range(Case):
    N =int(input())
    dp = [[0 for i in range(N)]for x in range(2)]
    Arr = [list(map(int, input().split())),list(map(int, input().split()))]
    dp[0][0] = Arr[0][0]
    dp[1][0] = Arr[1][0]
    if N != 1:
        dp[1][1] = Arr[1][1]+ dp[0][0]
        dp[0][1] = Arr[0][1] + dp[1][0]
        for i in range(2,N):
            dp[0][i] = Arr[0][i] + max(dp[1][i-1], dp[1][i-2])
            dp[1][i] = Arr[1][i] + max(dp[0][i-1], dp[0][i-2])
    print(max(dp[0][-1],dp[1][-1]))