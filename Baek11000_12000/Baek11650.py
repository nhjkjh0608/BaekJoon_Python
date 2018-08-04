import functools
N = int(input())
a = []
for i in range(N):
    a.append(tuple(map(int, input().split())))
def compare(item1, item2):
    if item1[0] == item2[0]:
        return item1[1] - item2[1]
    else:
        return item1[0] - item2[0]
for i in sorted(a, key = functools.cmp_to_key(compare)):
    print(i[0],i[1])