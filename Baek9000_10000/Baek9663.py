n = int(input())
dia1 = [0 for i in range(2*n-1)]
dia2 = [0 for i in range(2*n-1)]
cart = [0 for i in range(n)]
result = [0]
def solution(y):
    if y>=n :
        result[0]+=1
        return
    for x in range(n):
        if cart[x] or dia1[y+x] or dia2[n-1+y-x]:
            continue
        cart[x] = dia1[y+x]= dia2[n-1+y-x] = 1
        solution(y+1)
        cart[x] = dia1[y + x] = dia2[n - 1 + y - x] = 0

solution(0)
print(result[0])
