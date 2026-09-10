def solution(array, commands):
    answer = []
    for a,b,c in commands:
        arrayed = array[a-1:b]
        arrayed.sort()
        answer.append(arrayed[c-1])
    return answer
