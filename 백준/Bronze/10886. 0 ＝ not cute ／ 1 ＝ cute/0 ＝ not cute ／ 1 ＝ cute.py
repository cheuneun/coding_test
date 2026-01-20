import sys

n = int(sys.stdin.readline())
votes = [int(sys.stdin.readline()) for _ in range(n)]

if votes.count(1) > votes.count(0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")