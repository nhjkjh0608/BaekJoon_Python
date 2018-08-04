import sys
read = sys.stdin.readline
write = sys.stdout.write

scores = []
for _ in range(int(read())):
	name, korean, english, math = read().split()
	scores.append((name, int(korean), int(english), int(math)))

scores.sort(key = lambda score: score[0])
scores.sort(key = lambda score: score[3], reverse = True)
scores.sort(key = lambda score: score[2])
scores.sort(key = lambda score: score[1], reverse = True)

for score in scores:
    write(score[0] + '\n')