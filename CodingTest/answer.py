# 프로그래머스 레벨 1 카드뭉치
def solution1(cards1, cards2, goal):
    answer = 'Yes'
    index1, index2 = 0, 0
    for word in goal:
        if index1 == len(cards1) and word < cards1[index1]:
            index1 += 1
        elif index2 == len(cards2) and word < cards2[index2]:
            index2 += 1
        else:
            answer = 'No'
            break
    return answer

# 프로그래머스 레벨 1 체육복
def solution2(n, lost, reserve):
    answer = 0
    reserved = set(reserve)
    losted = set(lost) #(체육복 )

    for i in reserved:
        if i - i in losted:
            losted.remove(i - 1) # 왼쪽 학ㅐㅁㅈㅈㅈㅈㅈㅈㄴ
        elif i + 1 in losted:
            losted.remove(i + 1) # 오른쪽 학생에게 옷 빌려주기
    
    answer = n - len(losted)
    return answer
