
x=int(input("insert the number of rows"))
s=x-1
for rows in range(0,x):
    s=x-rows-1
    for emp in range(s,0,-1):
        print(" ",end=" ")
    for col in range(0,rows+1):
            print("*",end=" ")
    print("\n")

y=int(input("enter the number of rows"))
for row in range(0,y+1):
    for col in range(0,row):
        print("*",end='')
    print("\n")


z=int(input("enter the number of rows"))
for row in range(z,0,-1):
    for col in range(0,row):
        print("*",end='')
    print('\n')

w=int(input("enter the number of rows"))

for row in range(w,0,-1):
    s = w - row
    for space in range(0,s):
        print(" ",end="")
    for col in range(0,row):
        print("*",end='')

    print("\n")
