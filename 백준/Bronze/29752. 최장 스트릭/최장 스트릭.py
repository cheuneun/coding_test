n = int(input())
x = list(map(int, input().split()))

current = 0
result = 0
for i in range(n):
  if x[i]!= 0:
    current += 1
    if current > result:
      result = current
  else:
    current = 0

print(result)