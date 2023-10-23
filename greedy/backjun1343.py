board=input()

board=board.replace("XXXX","AAAA")
board=board.replace("XX","BB")


if 'X' in board:
    print(-1)
else:
    print(board)


## 생각할 것 문자열로 입력 받기
## relace를 사용하여 문자열 치환한후 기존값에 할당
## X가 포함되어 있으면 -1출력