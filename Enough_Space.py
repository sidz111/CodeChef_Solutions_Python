# cook your dish here
for i in range(int(input())):
    a,b,c=map(int, input().split())
    if (b+2*c)<=a:
        print("YES")
    else:
        print("NO")