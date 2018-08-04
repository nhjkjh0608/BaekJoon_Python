a = input()
b = [int(x) for x in input().split()]
b.sort()
c = input()
d = [int(x) for x in input().split()]
def binarySearch(alist, item):
    first = 0
    last = len(alist) -1
    found  = False
    while first<= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item< alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

for i in d:
    if binarySearch(b,i):
        print(1)
    else:
        print(0)
