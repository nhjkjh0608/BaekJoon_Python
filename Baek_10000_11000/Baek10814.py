import functools
d = {}
N = int(input())
L =[]
def cmp(i1, i2):
    return int(i1[0]) - int(i2[0])
for i in range(N):
    L.append(tuple(input().split()))
for i in sorted(L, key = functools.cmp_to_key(cmp)):
    print(i[0], i[1])
