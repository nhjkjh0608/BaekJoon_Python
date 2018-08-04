import sys
a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
b.sort()
def binarysearch (alist,item) :
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
c = input()
for element in map(int, sys.stdin.readline().split()):
    if binarysearch(b, element):
        sys.stdout.write(str(1)+" ")
    else:
        sys.stdout.write(str(0) + " ")