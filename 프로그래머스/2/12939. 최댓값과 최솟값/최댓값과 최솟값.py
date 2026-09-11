def solution(s):
    answer = ''
    st = list(map(int,s.split(' ')))
    maxx = max(st)
    minn = min(st)
    answer = str(minn) + ' ' + str(maxx)
    return answer