n = int(input())
file = []
for i in range(n):
  file.append(input())

result = ""

for i in range(len(file[0])):
  same = True
  for j in range(n):
    if file[0][i] != file[j][i]:
      same = False
      break

  if same == True:
    result += file[0][i]
  else: 
    result += "?"

print(result)