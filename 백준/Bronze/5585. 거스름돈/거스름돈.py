n = int(input())

answer = 0 
coins = [500,100,50,10,5,1]

rest = 1000 - n
for coin in coins:
  answer += rest // coin
  rest = rest % coin

print(answer)