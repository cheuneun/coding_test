def solution(num_list):
    answer = []
    
    a = 0
    b = 0
    
    for n in num_list:
        if n%2 ==0:
            a= a+1
        elif n%2==1:
            b = b+1
    
    answer.append(a)
    answer.append(b)
    return answer