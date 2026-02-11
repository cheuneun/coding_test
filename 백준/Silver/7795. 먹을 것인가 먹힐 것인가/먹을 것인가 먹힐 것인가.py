import sys
input = sys.stdin.readline

line = input().strip()
if line:
  T = int(line)
  for i in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    B.sort()

    count = 0
    for a in A:
      start = 0
      end = M - 1

      while start <= end:
        mid = (start+end)//2
        if B[mid] >= a:
          end = mid - 1
        else:
          start = mid + 1

      count += end + 1
    print(count)