n = int(input())
s = list(map(int, input().split()))

s.sort()
s_len = len(s) // 2

answer = []
for i in range(n):
    answer.append(s[i] + s[-1-i])

print(min(answer))