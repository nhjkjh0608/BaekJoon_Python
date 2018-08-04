# from timeit import  Timer 로 시간측정
import itertools
n=int(input())
T=True
for i in range(1,11):
    L=list(itertools.combinations("9876543210",i))
    L.reverse()
    if n<len(L):
        print(''.join(L[n]))
        T=False
        break
    else:
        n-=len(L)
if T:
    print(-1)




