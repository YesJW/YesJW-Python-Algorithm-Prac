from collections import deque

def bfs(board,x,y):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    n, m = len(board), len(board[0])
    q = deque()
    q.append([x,y,0])
    dist = list([1e9] * m for _ in range(n))
    dist[x][y] = 0
    while q:
        now_x, now_y, now_c = q.popleft()
        
        if board[now_x][now_y] == 'G':
            return now_c
        
        for i in range(4):
            cx = now_x
            cy = now_y
            
            while 0 <= cx + dx[i] < n and 0 <= cy + dy[i] < m and board[cx+dx[i]][cy+dy[i]] != 'D':
                cx += dx[i]
                cy += dy[i]
            
            if dist[cx][cy] > now_c+1:
                dist[cx][cy] = now_c+1
                q.append([cx,cy,now_c+1])
                
    return -1
 

def solution(board):
    answer = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                answer = bfs(board,i,j)
                
    return answer
