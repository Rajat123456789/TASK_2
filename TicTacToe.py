print("PLAYER 1 IS ASSIGNED X and PLAYER 2 IS ASSIGNED O BY DEFAULT")
main = []  #list
for x in range(0, 9, 1):
    main.append(str(x + 1)) # assigning values in the matrix
playerOneTurn = True  # initialization
winner = False        # initialization
def printBoard():
    for i in range(7,0,-3) :    # got right by trial and error :)
        print(main[i-1]+main[i]+main[i+1])  #displaying
count = 0
while not winner:
    printBoard()
    if (count >= 9):
        print("Draw")
        break
    if playerOneTurn:  #When it is Player One it is changed in the end of the while loop
        print("Player 1 Move(X):")
    else:  # When it is NOT Player One ie. Player Two it was changed in the end of the existing while loop
        print("Player 2 Move(O) :")
    choice = int(input(">> "))
    if (choice > 9):
        print("DRAW")
    if main[choice - 1] == 'X' or main[choice - 1] == 'O':
        print("You cannot place your move where someone or you has already done NO NO \n PENALTY")
        break
    if playerOneTurn:   #When it is Player One
        count += 1
        main[choice - 1] = 'X'
    else:               # When it is NOT Player One ie. Player Two
        count += 1
        main[choice - 1] = 'O'
    playerOneTurn = not playerOneTurn  # changing the state of the variable
# the winner case checkings
#diagonal
    if ((main[0] == main[4] == main[8]) or (main[2] == main[4] == main[6])):
        winner = True
        printBoard()
# rows and columns
    if ((main[6] == main[7]  == main[8]) or (main[3] == main[4]  == main[5]) or (main[0] == main[1]  == main[2])  or (main[6] == main[3]  == main[0]) or (main[7] == main[4]  == main[1]) or (main[2] == main[5]  == main[8]) ):
            winner = True
            printBoard()
print("Player " + str((int(playerOneTurn + 1))) + " wins!\n")