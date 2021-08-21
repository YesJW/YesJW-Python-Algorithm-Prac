n, m = map(int,input().split()) # n= 가로 m = 세로
a,b,d = map(int,input().split()) # a = 가로위치, b = 세로위치, d = 방향(1~4,북동남서)
ch = [[0]*m for _ in range(n)] # 방문한 곳 체크
ch[a][b] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]

arr = []

turn = 0
count = 1
for i in range(m):
    arr.append(list(map(int, input().split())))

def dir_ch():
    global d
    d -= 1
    if d == -1:
        d = 3

while True:
    dir_ch()

    x = a + dx[d]
    y = b + dy[d]

    if(ch[x][y] == 0 and arr[x][y] == 0):
        ch[x][y] = 1
        a = x
        b = y
        count+=1
        turn = 0
        continue
    else:
        turn += 1


    if turn == 4:
        x = a - dx[d]
        y = b - dy[d]
        if arr[x][y] == 0:
            a = x
            b = y
        else:
            break
        turn = 0

print(count)

# 게임 개발

