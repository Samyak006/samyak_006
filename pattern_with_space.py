x=int(input("insert the number of rows"))
s=x-1
for rows in range(0,x):
    s=x-rows-1
    for emp in range(s,0,-1):
        print(" ",end=" ")
    for col in range(0,rows+1):
        print(" * ",end=" ")

    print("\n")

y=int(input("insert the number of rows"))
s=y-1
num=65
for rows in range(0,y):
    s=y-rows-1
    for emp in range(s,0,-1):
        print(" ",end=" ")
    for col in range(0, rows + 1):
        print(" ",chr(num), end=" ")
        num = num + 1
    print("\n")
z = int(input("insert the number of rows"))
s = z - 1
num = 1
for rows in range(0, y):
    s = z - rows - 1
    for emp in range(s, 0, -1):
        print(" ", end=" ")
    for col in range(0, rows + 1):
        print(" ",num, end=" ")
        num = num + 1
    print("\n")






