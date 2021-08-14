n = int(input())

tr = [1, 1]

move = list(map(str, input().split()))

for i in move:
    if(i == 'R'):
        tr[1]+=1
    elif(i == 'L'):
        tr[1]-=1
    elif (i == 'U'):
        tr[0]-=1
    else:
        tr[0]+=1
    if(tr[0] == 0):
        tr[0] = 1
    if(tr[1] == 0):
        tr[1]  = 1

print(tr[0], tr[1])

#상하좌우
