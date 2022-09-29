last_num=int(input("enter a number: "))
for row in range(1, last_num):
    for column in range(row, 0, -1):
        print(column, end=' ')
    print("")
