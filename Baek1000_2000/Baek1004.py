def inCircle(List, x1, y1):
    r = ((List[0]-x1)**2+ (List[1]-y1)**2)**0.5
    if r<List[2]:
        return True
    else:
        return False
CaseNum = int(input())
for tmp in range(CaseNum):
    Cord = list(map(int, input().split()))
    N = int(input())
    cnt = 0
    for i in range(N):
        tmpList = list(map(int, input().split()))
        bolStart = inCircle(tmpList,Cord[0],Cord[1])
        bolEnd = inCircle(tmpList, Cord[2], Cord[3])
        if bolStart and bolEnd:
            continue
        elif bolStart or bolEnd:
            cnt += 1
    print(cnt)