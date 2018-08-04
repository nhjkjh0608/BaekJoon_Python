n = int(input())
k = int(input())
arr = [input() for x in range(n)]
from itertools import permutations
print(len(set(map(lambda x: ''.join(x),permutations(arr, k)))))
