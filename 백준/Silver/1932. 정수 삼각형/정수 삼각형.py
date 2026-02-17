n = int(input())

tri = []
for i in range(n):
    tri.append(list(map(int, input().split())))

# dp 테이블을 tri 복사해서 사용
dp = [row[:] for row in tri]

# 2번째 줄부터 시작
for i in range(1, n):
    for j in range(i + 1):

        # 왼쪽 끝 (위에서만 내려옴)
        if j == 0:
            dp[i][j] = dp[i-1][j] + tri[i][j]

        # 오른쪽 끝 (왼쪽 위에서만 내려옴)
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + tri[i][j]

        # 가운데 (둘 중 max)
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]

print(max(dp[n-1]))