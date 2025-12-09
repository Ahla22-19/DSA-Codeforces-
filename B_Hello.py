n = input()
target = "hello"
 
count = 0
for i in n:
    if i == target[count]:
        count += 1
 
        if count == len(target):
            print("YES")
            break
 
else:
    print("NO") 