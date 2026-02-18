#14501

n = int(input())

t = []
p = []
for _ in range(n):
  ti,pi = input().split()
  t.append(int(ti))
  p.append(int(pi))

dp = [0]* (n+1) # 끝나는날까지,,
for i in range(n):
  dp[i] = max(dp[i],dp[i-1])
  # 전의 일수까지의 금액이 더 클수도 있잖아
  if t[i]+ i <= n:
    dp[t[i]+i] = max(dp[t[i]+i],dp[i]+p[i])

print(max(dp))