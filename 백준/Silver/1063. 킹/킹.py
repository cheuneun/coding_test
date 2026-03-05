king, rock, N = input().split()

l = []
for i in range(int(N)):
  l.append(input())

x = ord(king[0])
y = int(king[1])
rx = ord(rock[0])
ry = int(rock[1])

for n in l:
  nx, ny = x,y
  
  if n == 'R':
    nx += 1
  elif n == 'L':
    nx -= 1
  elif n == 'B':
    ny -= 1
  elif n == 'T':
    ny += 1
  elif n == 'RT':
    nx += 1
    ny += 1
  elif n == 'LT':
    nx -= 1
    ny += 1
  elif n == 'RB':
    nx += 1
    ny -= 1
  elif n == 'LB':
    nx -= 1
    ny -= 1

  if nx == rx and ny == ry:
    nrx, nry = rx + (nx - x), ry + (ny - y)
    if 65 <= nrx <= 72 and 1 <= nry <= 8:
        rx, ry = nrx, nry
        x, y = nx, ny
  else:
    if 65 <= nx <= 72 and 1 <= ny <= 8:
      x, y = nx, ny


last_king = chr(x)+str(y)
last_rock = chr(rx)+str(ry)
print(last_king)
print(last_rock)