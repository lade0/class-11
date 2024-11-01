# demonstrate right-angle triangle
num=int(input("enter the number of rows"))
count=1
for count in range(num):
    for j in range(count+1):
        print("* ",end="")
    print()