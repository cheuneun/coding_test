# 2512
import sys
input = sys.stdin.readline

N = int(input())
n_list = list(map(int, input().split()))
M = int(input())

left,right = 0,max(n_list)
while left <= right:
    mid = (left+right)//2
    total = sum(min(mid, n) for n in n_list)
    if total <= M:
        left = mid + 1
    else:
        right = mid - 1
print(right)