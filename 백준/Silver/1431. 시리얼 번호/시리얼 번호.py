N = int(input())

sireal = []
for _ in range(N):
  sireal.append(input())

result = sorted(sireal,key=(lambda x:(len(x),sum(int(i) for i in x if i.isdigit()),x)))
print(*result)