n = int(input())
a = list(map(int,input().split()))

dp = [1 for i in range(n)]
# 길이가 1부터 시작,,(자기자신)

for i in range(n):
  for j in range(i):
    if a[j] > a[i]:
      dp[i] = max(dp[i],dp[j]+1)

print(max(dp))