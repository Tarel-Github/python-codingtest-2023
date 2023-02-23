# 백준 1991 - 트리 순회
import sys
input = sys.stdin.readline
N = int(input())
tree ={}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def preOrder(now):  #전위순회
    if now == '.': return
    print(now, end = '')   # 부모노드 출력
    preOrder(tree[now][0]) # 좌측노드 출력
    preOrder(tree[now][1]) # 우측노드 출력

def inOrder(now):  #중위순회
    if now == '.': return
    inOrder(tree[now][0]) # 좌측노드 출력
    print(now, end = '')   # 부모노드 출력
    inOrder(tree[now][1]) # 우측노드 출력


def postOrder(now):  #후위순회
    if now == '.': return
    postOrder(tree[now][0]) # 좌측노드 출력
    postOrder(tree[now][1]) # 우측노드 출력
    print(now, end = '')   # 부모노드 출력

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
print()