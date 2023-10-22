# cook your dish here
t=int(input())
for _ in range(t):
    s=int(input())
    if(s<=70):
        print(0)
    elif(s<=100):
        print(500)
    else:
        print(2000)