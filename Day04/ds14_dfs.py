# 깊이 우선 탐색
class Graph:
    def __init__(self, size) -> None:
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# 전역변수
G1 = None
stack =[]
visitedAry = []
A, B, C, D = 0, 1, 2, 3

if __name__ == "__main__":
    G1 = Graph(4)   # A=0, B=1, C=2, D=3
    G1.graph[A][C] = 1; G1.graph[A][D] = 1
    G1.graph[B][C] = 1
    G1.graph[C][A] = 1; G1.graph[C][B] = 1; G1.graph[C][D] = 1
    G1.graph[D][A] = 1; G1.graph[D][C] = 1

    print('G1 무방향 그래프')
    for item in G1.graph:
        print(item)

    current = A
    stack.append(current)
    visitedAry.append(current)

    while (len(stack) != 0):
        next = None
        for vertex in range(G1.SIZE):
            if G1.graph[current][vertex] == 1: # 엣지가 있으면
                if vertex in visitedAry: # 이미 방문 했으면 탈락
                    pass
                else: # 방문한 적이 없으면 다음 정점으로 지정
                    next = vertex
                    break # for문 완전 빠져나감
                
        if next != None: # 다음 방문할 정점이 있으면
            current = next
            stack.append(current)
            visitedAry.append(current)
        else: # 다음 방문할 정점이 없으면
            current = stack.pop() # 스택에서 꺼내옴

    print('방문순서 --> ', end = ' ')
    for i in visitedAry:
        print(chr(ord('A')+i), end = ' ->')


