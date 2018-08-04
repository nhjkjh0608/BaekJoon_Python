from functools import reduce
print(reduce((lambda x,y: x+y), [x[0] for x in input().split("-")]))
