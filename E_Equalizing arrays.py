n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2= list(map(int, input().split()))

p1 = 0
p2 = 0 
operation1 = 0
operation2 = 0
c = []
d = []

while p1 < n and p2 < m:

    if arr1[p1] == arr2[p2]:
        c.append(arr1[p1])
        d.append(arr2[p2])
        p1 += 1
        p2 +=  1


    elif arr1[p1] < arr2[p2]:
        operation1 += 1
        if p1 + 1 < n:
            arr1[p1 + 1] += arr1[p1]
        p1 += 1

    else: #arr2[p2] < arr1[p1]:
        operation2 += 1
        if p2 + 1 < m:
            arr2[p2 + 1] += arr2[p2]
        p2 += 1

a = n - operation1 
b = m - operation2

if c == d and a == b:
    print(a)

else:
    print("-1")
    


  

    

        



        
