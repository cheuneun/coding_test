
A, B = map(int,input().split())
count = 1

while(B > A):
  if B % 2 == 0:
    B = B // 2
  elif B % 10 == 1:
    B = B // 10
  else:
    break
  count = count+1

if B == A :
  print(count)
else:
  print(-1)