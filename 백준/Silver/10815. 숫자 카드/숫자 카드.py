N = int(input())
n_card = list(map(int, input().split()))
M = int(input())
m_card = list(map(int, input().split()))

n_card.sort()

def binary_search(array,target,start,end):
  while start <= end:
    mid = (start+end)//2
    if array[mid] == target :
      return mid
    elif array[mid] < target:
      start = mid + 1
    else:
      end = mid - 1

for i in m_card:
  result = binary_search(n_card,i,0,N-1)
  if result != None:
    print(1, end = " ")
  else:
    print(0, end = " ")