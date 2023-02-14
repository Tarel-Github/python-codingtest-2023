# 단순 연결리스트 구현
class Node:
    def __init__(self) -> None:
        self.data = None
        self.link = None

# 전역변수
memory = [] #lists()
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

def printNodes(start):
    current = start
    if current == None:
        return
    
    print(current.data, end = ' -> ')
    while current.link != None:
        current = current.link
        if current.link == None:
            print(current.data)
        else:
            print(current.data, end = ' -> ')

# 노드 추가
def insertNode(findData, insertData):
    global memory, pre, current, head

    if head.data == findData: # 첫 노드 앞
        node = Node()
        node.data = insertData
        node.link = head
        return
    
    current = head # 제일 앞으로

    while current.link != None: # 중간노드
        pre = current
        current = current.link

        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    # current.link == None 까지 온 것
    node = Node()
    node.data = insertData
    current.link = node
    return

if __name__ == '__main__':
    node = Node()
    node.data = dataArray[0] # 다현
    head = node
    memory.append(head)
    
    for data in dataArray[1:]: # 두 번째 노드(1번째) 이후부터 끝까지
        pre = node
        node = Node()
        node.data = data    # 정연, 쯔위, 사나, 지효 순
        pre.link = node
        memory.append(node)

    printNodes(head)


