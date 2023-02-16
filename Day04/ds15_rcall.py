count = 3

def openBox():
    global count
    print('종이상자를 엽니다. ')
    count -= 1
    if count == 0:
        print('상자에 반지를 넣는다.')
        return
    
    openBox() # 자신을 다시 호출
    print('종이상자를 닫습니다.')

if __name__ == '__main__':
    openBox()

