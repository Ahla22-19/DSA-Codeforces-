n=int(input())
for i in range (n):
    m=list(map(int,input().split()))
    s=m[0]+m[1]==m[2]
    u=m[0]-m[1]==m[2]
    if (s):
       print ("+")
    elif(u):
        print ("-")
    else:
        continue
