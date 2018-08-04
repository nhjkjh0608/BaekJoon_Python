import sys
read = sys.stdin.readline
N = int(read())
from collections import defaultdict
from functools import cmp_to_key
D = defaultdict(int)
for i in range(N):
    D[int(read())]+=1
K = list(D.items())
def cmp(i1, i2):
    if i1[1] == i2[1]:
        return i1[0]-i2[0]
    else:
        return -i1[1]+ i2[1]
t = sorted(K,key= cmp_to_key(cmp))
print(t[0][0])