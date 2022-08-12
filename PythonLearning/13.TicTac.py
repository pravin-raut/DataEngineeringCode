def displayGame(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("-----")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-----")
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("-----")


def takeuserinput():
    return int(input("Where do you want to place"))


def assigninput(inputList, x_o_list, userinput):
    max = len(x_o_list) - 1
    inputList[userinput] = x_o_list[max]
    x_o_list.pop()


inputList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
x_o_list = ['z', 'x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']
displayGame(inputList)
winner=0
def winCheck(inputList,one,two,three):
        if(inputList[one]==inputList[two]==inputList[three]):
            print("{} Won".format(inputList[one]))
            global winner
            winner = 1
        else:
            pass


while len(x_o_list)!=1 and winner!=1:
    userinput = takeuserinput()
    assigninput(inputList, x_o_list, userinput)
    print("\n\n")
    print("-----Next Move---------")
    print(f"winner is {winner}")
    displayGame(inputList)
    winCheck(inputList,1,2,3)
    winCheck(inputList, 4, 5, 6)
    winCheck(inputList, 7, 8, 9)
    winCheck(inputList, 1, 4, 7)
    winCheck(inputList, 2, 5, 8)
    winCheck(inputList, 3, 6, 9)
    winCheck(inputList, 1, 5, 9)
    winCheck(inputList, 3, 5, 7)

