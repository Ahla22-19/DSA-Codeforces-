m=int(input())
for i in range(n):
    m=int(input())
    nums=list(map(int,input().split()))
    l,r=0,m-1
    count=0
    while l<r:
        while l < m and nums[l] == 0:
            l+=1
        while r > -1 and nums[r] == 1:
            r-=1
 
        if r > l:
            count+=1
        r-=1
        l+=1
    print(count)
