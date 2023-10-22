# cook your dish here
a,b,c,d=map(int, input().split())
if ((a*2)+b) > ((c*2)+d):
    print("Messi")
elif (((c*2)+d) > ((a*2)+b)):
    print("Ronaldo")
else:
    print("Equal")