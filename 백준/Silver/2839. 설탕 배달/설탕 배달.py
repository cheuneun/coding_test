n = int(input())

answer = -1 #초깃값 설정

f = n//5  # 5로 나누었을 때

while(f>=0):
  rest = n - (5*f)
  if rest%3==0: #3,5로 나누었을 때 나머지가 0이면 반복문 나오기
    answer = f + (rest//3) #5로 나누었을때와 3으로 나누었을 떄 합치기
    break
  f -= 1

print(answer)