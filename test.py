import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    d = a = list(map(int, input().split()))
    for k in range(1,n):
        print("k",k)
        test = []
        for i in range(n-k):
            print("i",i)
            q1 = a[i]-d[i+1]
            q2 = a[i+k]-d[i]
            print("max",q1,q2 )
            test.append(max(q1,q2))
        d = test
        print(d)
    print(d[0],sum(a))
    print(d[0]+sum(a)>>1)