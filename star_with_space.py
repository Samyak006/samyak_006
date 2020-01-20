x=int(input("insert the number of rows"))
s=x-1
for rows in range(0,x):
    s=x-rows-1
    for emp in range(s,0,-1):
        print(" ",end=" ")
    for col in range(0,rows+1):
        print(" * ",end=" ")

    print("\n")



