def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    answer = n - len(lost)
    for i in range(0, len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost[i] = 99
            answer += 1
    for i in range(0, len(lost)):
        if lost[i]-1 in reserve:
            reserve.remove(lost[i]-1)
            lost[i] = 99
            answer += 1    
        elif lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
            lost[i] = 99
            answer += 1
    return answer