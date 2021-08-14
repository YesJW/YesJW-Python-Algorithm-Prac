n, k = map(int, input().split())
count = 0
while(True):
    if n == 1:
        break
    count += 1

    if(n%k != 0):
        n -= 1
    else:
        n /= k

print(count)

#1이 될 때까지