n, m, k = map(int, input().split())
i = list(map(int,input().split()))
i.sort()
count1 = 1
count2 = 0
sum = 0

while(count1 != m-1):
    sum += i[n-1]
    count1 += 1
    count2 += 1
    if(count2 == k):
        count2 = 0
        sum += i[n-2]

print(sum)

#큰수의 법칙 그리디