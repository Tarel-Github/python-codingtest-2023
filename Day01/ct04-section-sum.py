# 구간합 구하기 11659
# import sys는 주피터노트북에서 사용 불가
import sys
input = sys.stdin.readline# 이부분이 없으면 백준에서 시간 초과

N, M = tuple(map(int, input().split()))
numbers = list(map(int, input().split()))
sums = [0]
temp = 0

for i in numbers:
    temp = temp + i
    sums.append(temp)

for i in range(M):
    x, y = tuple(map(int, input().split()))
    print(sums[y] - sums[x-1])