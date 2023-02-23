# 백준 11657 - 타임머신
import sys

# 두 숫자를 입력받아 N과 M에 할당, 각각 노드와 엣지임
N, M = map(int, input().split())
edges = []
distance = [sys.maxsize] * (N + 1) # 파이썬 시스템이 가질 수 있는 최대값을 배열로 저장, 이때 배열의 요소수는 N+1 개

# 3개의 숫자를 받아서 start, end, time에 할당하고, 다시 그걸 edges라는 배열에 할당, 이를 M(엣지)만큼 반복
for _ in range(M):
    start, end, time = map(int, input().split())
    edges.append((start, end, time))

# 벨만포드 수행
distance[1] = 0 # distance의 1번 요소를 0으로 변경

# 엣지에 저장된 숫자들을 다시 start, end, time에 할당하면서, 
for _ in range(N-1):
    for start, end, time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time

# 음수 사이클
mCycle = False
for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        mCycle = True #음수 사이클이 존재!
        break

if mCycle != True:
    for i in range(2, N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)
