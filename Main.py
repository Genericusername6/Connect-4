from random import randint

column1 = ["  " for i in range(6)]
column2 = ["  " for i in range(6)]
column3 = ["  " for i in range(6)]
column4 = ["  " for i in range(6)]
column5 = ["  " for i in range(6)]
column6 = ["  " for i in range(6)]
column7 = ["  " for i in range(6)]
# setting up the board
def print_grid():
    for i in range(6):
        print(column1[i],column2[i],column3[i],column4[i],column5[i],column6[i],column7[i], sep=" | ")
        print("------------------------------")
    print("::::::::::::::::::::::::::::")


def restart():
    global turns
    for i in range(7):
        row1[i] = "0"
    for i in range(7):
        row2[i] = "0"
    for i in range(7):
        row3[i] = "0"
    for i in range(7):
        row4[i] = "0"
    for i in range(7):
        row5[i] = "0"
    for i in range(7):
        row6[i] = "0"
    turns = 0


turns = 0
while turns < 21:
    if turns % 2 == 0:
        typed = input("Start with the number of the column: " )
    else:
        typed = str(randint(1,7))
    if typed == "1":
        for i in range(6):
            if column1[-(i + 1)] == "  ":
                column1[-(i + 1)] = "🔵" if turns % 2 == 0 else "🔴"
    
                print_grid()
                break

    turns += 1



