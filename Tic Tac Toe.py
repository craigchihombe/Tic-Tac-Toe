theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '    
          }
board_keys = []
for key in theBoard:
    board_keys.append(key)
    
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-+')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-+')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    
    turn = 'X'
    count = 0
    
    for i in range(10):
        printBoard(theBoard)
        print("its your turn," + turn + " move to which place?")
        
        move = input()
        if theBoard[move]==' ':
            theBoard[move]= turn
            count += 1
        else:
            print("This place is already occupied. \nMove to which Place?")
            continue
        
        if count>=5:
            if theBoard['7']==theBoard['8']==theBoard['9'] !=' ':   #Across the top
                printBoard(theBoard)
                print(" \nGame over.\n")
                print(" ***** "+ turn +"You win.")
                break
            elif theBoard['4']==theBoard['5']==theBoard['6'] !=' ':   #Across the middle
                printBoard(theBoard)
                print(" \nGame over.\n")
                print(" ***** "+ turn +"You win.")
                break
            elif theBoard['1']==theBoard['2']==theBoard['3'] !=' ':   #Across the bottom
                printBoard(theBoard)
                print(" \nGame over.\n")
                print(" ***** "+ turn +"You win.")
                break
            elif theBoard['1']==theBoard['4']==theBoard['7'] !=' ':   #Down the left side
                printBoard(theBoard)
                print(" \nGame over.\n")
                print(" ***** "+ turn +"You win.")
                break
            elif theBoard['2']==theBoard['5']==theBoard['8'] !=' ':   #Down the middle side
                printBoard(theBoard)
                print(" \nGame over.\n")
                print(" ***** "+ turn +"You win.")
                break
            elif theBoard['3']==theBoard['6']==theBoard['9'] !=' ':   #Down the right side
                printBoard(theBoard)
                print(" \nGame over.\n")
                print(" ***** "+ turn +"You win.")
                break
            elif theBoard['7']==theBoard['5']==theBoard['3'] !=' ':   #Diagonal
                printBoard(theBoard)
                print(" \nGame over.\n")
                print(" ***** "+ turn +"You win.")
                break
            elif theBoard['1']==theBoard['5']==theBoard['9'] !=' ':   #Diagonal
                printBoard(theBoard)
                print(" \nGame over.\n")
                print(" ***** "+ turn +"You win.")
                break
            
        if count==9:
            print(" \nGame over.\n")
            print("it's a tie")
            
        if turn=='X':
            turn = 'O'
        else:
            turn = 'X'
    
    restart = input("Do you want to play again?(Y/N) ")
    if restart=="y" or restart=="Y":
        for key in board_keys:
            theBoard[key]=" "
        game()
if __name__=="__main__":
    game()
            
    