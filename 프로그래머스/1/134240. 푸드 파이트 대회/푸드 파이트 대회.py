def solution(food):
    result = ''
    for i in range(1, len(food)):
        temp = food[i] // 2
        result += str(i) * temp
    return result + "0" + result[::-1]