#demonstrate floyds triangle
row=int(input("enter the amount of rows"))
x=1
for i in range(row):
    for j in range(i+1):
        print(x,end=" ")
        x = x+1
    print()