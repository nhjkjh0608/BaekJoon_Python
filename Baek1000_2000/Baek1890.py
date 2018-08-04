import sys
# sys.setrecursionlimit(100000)
K =[]
for i in range(int(sys.stdin.readline())):
    K.append(list(map(int,sys.stdin.readline().split())))

#
# L =0
# def f(x,y, n):
#     global L
#     if x ==y ==n-1:
#         L+=1
#         return
#     _x = x+K[y][x]
#     _y = y+K[y][x]
#     if _x<n:
#         f(_x,y,n)
#     if _y<n:
#         f(x,_y,n)
#
#


# f(0,0,len(K))
# print(L)

TT = [[0 for i in range(len(K))]for j in range(len(K))]
TT[len(TT)-1][len(TT)-1] = 1
Length = len(K)
K[Length-1][Length-1] = 1

for x in range(Length-1,-1,-1):
    for y in range(Length-1,-1,-1):
        _x = x + K[y][x]
        _y = y + K[y][x]
        tmp = TT[y][x]
        if _x<Length:
            tmp+= TT[y][_x]
        if _y< Length:
            tmp+= TT[_y][x]
        TT[y][x]= tmp

print(TT[0][0])


