import random
import time
import pygame

def console():
    print("\nWelcome to Mega Tic Tac Toe!")

    def base_tic():
        print("""
    ____|____|____   ____|____|____   ____|____|____
    ____|_1__|____   ____|_2__|____   ____|_3__|____
        |    |           |    |           |    |    

    ____|____|____   ____|____|____   ____|____|____
    ____|_4__|____   ____|_5__|____   ____|_6__|____
        |    |           |    |           |    |    

    ____|____|____   ____|____|____   ____|____|____
    ____|_7__|____   ____|_8__|____   ____|_9__|____
        |    |           |    |           |    |    
    """)

    empty_board = """
    ____|____|____
    ____|____|____
        |    |
    """

    blank = """
    __1_|__2_|__3_ 
    __4_|__5_|__6_ 
    7 |  8 |  9  
    """
    print("\nWhat is Player 1's name?")
    pl1 = input("Player 1: ")
    print("\nWhat is Player 2's name?")
    pl2 = input("Player 2: ")

    print("\nChoosing who goes first...")
    time.sleep(2)

    first =random.randint(1, 2)
    if first == 1:
        print(f"\n {pl1} goes first and will be X")
        p1 = pl1
        p2 = pl2
    else:
        print(f"\n {pl2} goes first and will be X")
        p1 = pl2
        p2 = pl1

    print("Choose which grid")
    base_tic()

    while True:
        try:
            grid_choice = int(input("> "))
        except ValueError:
            print("Enter a whole number between 1 to 9")
        else:
            if grid_choice > 9 or grid_choice < 1:
                print("Enter a whole number between 1 to 9")
            else:
                break

    boards = {
        1: [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        2: [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        3: [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        4: [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        5: [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        6: [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        7: [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        8: [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        9: [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    }

    mini_board = {
        1: " ",
        2: " ",
        3: " ",
        4: " ",
        5: " ",
        6: " ",
        7: " ",
        8: " ",
        9: " "
    }

    def board_lines(board):
        return [
            f"_{board[0]}__|_{board[1]}__|_{board[2]}__",
            f"_{board[3]}__|_{board[4]}__|_{board[5]}__",
            f" {board[6]}  | {board[7]}  | {board[8]}  "
        ]

    def show_board(board):
        print(f"""
    _{board[0]}__|_{board[1]}__|_{board[2]}__
    _{board[3]}__|_{board[4]}__|_{board[5]}__
    {board[6]}  | {board[7]}  | {board[8]}  
    """)

    def entire():
        b9 = board_lines(boards[9])
        b1 = board_lines(boards[1])
        b2 = board_lines(boards[2])
        b3 = board_lines(boards[3])
        b4 = board_lines(boards[4])
        b5 = board_lines(boards[5])
        b6 = board_lines(boards[6])
        b7 = board_lines(boards[7])
        b8 = board_lines(boards[8])


        print(f"{b1[0]}    {b2[0]}    {b3[0]}")
        print(f"{b1[1]}    {b2[1]}    {b3[1]}")
        print(f"{b1[2]}    {b2[2]}    {b3[2]}\n")
        print(f"{b4[0]}    {b5[0]}    {b6[0]}")
        print(f"{b4[1]}    {b5[1]}    {b6[1]}")
        print(f"{b4[2]}    {b5[2]}    {b6[2]}\n")
        print(f"{b7[0]}    {b8[0]}    {b9[0]}")
        print(f"{b7[1]}    {b8[1]}    {b9[1]}")
        print(f"{b7[2]}    {b8[2]}    {b9[2]}")

    def check_win(board_number, board):

        global boards

        if board[0] == board[1] == board[2] and board[0] != " ":
            if board[0] == "X":
                print(f"{p1} (X) has won board {board_number}")
                mini_board[board_number] = "X"
                boards[board_number] = ["X", "X", "X", "X", "X", "X", "X", "X", "X"]
                return
            else:
                print(f"{p2} (O) has won board {board_number}")
                mini_board[board_number] = "O"
                boards[board_number] = ["O", "O", "O", "O", "O", "O", "O", "O", "O"]
                return

        if board[3] == board[4] == board[5] and board[3] != " ":
            if board[3] == "X":
                print(f"{p1} (X) has won board {board_number}")
                mini_board[board_number] = "X"
                boards[board_number] = ["X", "X", "X", "X", "X", "X", "X", "X", "X"]
                return
            else:
                print(f"{p2} (O) has won board {board_number}")
                mini_board[board_number] = "O"
                boards[board_number] = ["O", "O", "O", "O", "O", "O", "O", "O", "O"]
                return

        if board[6] == board[7] == board[8] and board[6] != " ":
            if board[6] == "X":
                print(f"{p1} (X) has won board {board_number}")
                mini_board[board_number] = "X"
                boards[board_number] = ["X", "X", "X", "X", "X", "X", "X", "X", "X"]
                return
            else:
                print(f"{p2} (O) has won board {board_number}")
                mini_board[board_number] = "O"
                boards[board_number] = ["O", "O", "O", "O", "O", "O", "O", "O", "O"]
                return

        if board[0] == board[3] == board[6] and board[0] != " ":
            if board[0] == "X":
                print(f"{p1} (X) has won board {board_number}")
                mini_board[board_number] = "X"
                boards[board_number] = ["X", "X", "X", "X", "X", "X", "X", "X", "X"]
                return
            else:
                print(f"{p2} (O) has won board {board_number}")
                mini_board[board_number] = "O"
                boards[board_number] = ["O", "O", "O", "O", "O", "O", "O", "O", "O"]
                return

        if board[1] == board[4] == board[7] and board[1] != " ":
            if board[1] == "X":
                print(f"{p1} (X) has won board {board_number}")
                mini_board[board_number] = "X"
                boards[board_number] = ["X", "X", "X", "X", "X", "X", "X", "X", "X"]
                return
            else:
                print(f"{p2} (O) has won board {board_number}")
                mini_board[board_number] = "O"
                boards[board_number] = ["O", "O", "O", "O", "O", "O", "O", "O", "O"]
                return

        if board[2] == board[5] == board[8] and board[2] != " ":
            if board[2] == "X":
                print(f"{p1} (X) has won board {board_number}")
                mini_board[board_number] = "X"
                boards[board_number] = ["X", "X", "X", "X", "X", "X", "X", "X", "X"]
                return
            else:
                print(f"{p2} (O) has won board {board_number}")
                mini_board[board_number] = "O"
                boards[board_number] = ["O", "O", "O", "O", "O", "O", "O", "O", "O"]
                return

        if board[0] == board[4] == board[8] and board[0] != " ":
            if board[0] == "X":
                print(f"{p1} (X) has won board {board_number}")
                mini_board[board_number] = "X"
                boards[board_number] = ["X", "X", "X", "X", "X", "X", "X", "X", "X"]
                return
            else:
                print(f"{p2} (O) has won board {board_number}")
                mini_board[board_number] = "O"
                boards[board_number] = ["O", "O", "O", "O", "O", "O", "O", "O", "O"]
                return

        if board[2] == board[4] == board[6] and board[2] != " ":
            if board[2] == "X":
                print(f"{p1} (X) has won board {board_number}")
                mini_board[board_number] = "X"
                boards[board_number] = ["X", "X", "X", "X", "X", "X", "X", "X", "X"]
                return
            else:
                print(f"{p2} (O) has won board {board_number}")
                mini_board[board_number] = "O"
                boards[board_number] = ["O", "O", "O", "O", "O", "O", "O", "O", "O"]
                return

    game_running = True

    def check_full_win():

        global game_running

        counter = 0

        if mini_board[1] == mini_board[2] == mini_board[3] and mini_board[1] != " " and mini_board[1] != "D":
            print("GAME OVER")
            if mini_board[1] == "X":
                print(f"{p1} (X) was the winner")
            else:
                print(f"{p2} (O) was the winner")
            game_running = False
            return

        if mini_board[4] == mini_board[5] == mini_board[6] and mini_board[4] != " " and mini_board[4] != "D":
            print("GAME OVER")
            if mini_board[4] == "X":
                print(f"{p1} (X) was the winner")
            else:
                print(f"{p2} (O) was the winner")
            game_running = False
            return

        if mini_board[7] == mini_board[8] == mini_board[9] and mini_board[7] != " " and mini_board[7] != "D":
            print("GAME OVER")
            if mini_board[7] == "X":
                print(f"{p1} (X) was the winner")
            else:
                print(f"{p2} (O) was the winner")
            game_running = False
            return

        if mini_board[1] == mini_board[4] == mini_board[7] and mini_board[7] != " " and mini_board[7] != "D":
            print("GAME OVER")
            if mini_board[7] == "X":
                print(f"{p1} (X) was the winner")
            else:
                print(f"{p2} (O) was the winner")
            game_running = False
            return

        if mini_board[2] == mini_board[5] == mini_board[8] and mini_board[8] != " " and mini_board[8] != "D":
            print("GAME OVER")
            if mini_board[8] == "X":
                print(f"{p1} (X) was the winner")
            else:
                print(f"{p2} (O) was the winner")
            game_running = False
            return

        if mini_board[3] == mini_board[6] == mini_board[9] and mini_board[9] != " " and mini_board[9] != "D":
            print("GAME OVER")
            if mini_board[9] == "X":
                print(f"{p1} (X) was the winner")
            else:
                print(f"{p2} (O) was the winner")
            game_running = False
            return

        if mini_board[1] == mini_board[5] == mini_board[9] and mini_board[9] != " " and mini_board[9] != "D":
            print("GAME OVER")
            if mini_board[9] == "X":
                print(f"{p1} (X) was the winner")
            else:
                print(f"{p2} (O) was the winner")
            game_running = False
            return

        if mini_board[3] == mini_board[5] == mini_board[7] and mini_board[7] != " " and mini_board[7] != "D":
            print("GAME OVER")
            if mini_board[7] == "X":
                print(f"{p1} (X) was the winner")
            else:
                print(f"{p2} (O) was the winner")
            game_running = False
            return
        
        for i in range(1, 10):
            if mini_board[i] != " ":
                counter = counter + 1
                if counter == 9:
                    print("GAME OVER")
                    print("No one won, the game ended in a draw")
                    game_running = False
                    return


    current_player = "X"
    current_board = grid_choice
    new_board = False
    while game_running:
        
        while new_board == True:
            try:
                grid_choice = int(input("> "))
            except ValueError:
                print("Enter a whole number between 1 to 9")
            else:
                if grid_choice > 9 or grid_choice < 1:
                    print("Enter a whole number between 1 to 9")
                elif mini_board[grid_choice] != " ":
                    print("That board had already been won or drawn. Choose another.")
                else:
                    current_board = grid_choice
                    new_board = False
                    break

        print(f"\nBoard: {current_board}")

        show_board(boards[current_board])

        print(blank)

        print(f"\n{current_player}'s turn")

        while True:
            try:
                spot = int(input("> "))
            except ValueError:
                print("Enter a whole number between 1 to 9")
            else:
                if spot > 9 or spot < 1:
                    print("Enter a whole number between 1 to 9")
                    print(blank)

                elif boards[current_board][spot-1] != " ":
                    print("That spot is already taken")
                    print(blank)
                    print(current_board)
                
                else:
                    boards[current_board][spot - 1] = current_player
                    check_win(current_board, boards[current_board])
                    if mini_board[current_board] == " ":
                        if " " not in boards[current_board]:
                            print("This board has been drawn")
                            mini_board[current_board] = "D"
                    show_board(boards[current_board])
                    check_full_win()
                    current_board = spot
                    if mini_board[current_board] != " ":
                        print(f"That board has already been filled by {mini_board[current_board]}. You get to choose any board that you want.")
                        new_board = True
                    if current_player == "X":
                        current_player = "O"
                    else:
                        current_player = "X"
                    break

        print("Type 1 to see the entire board or type anything else to skip")
        all = input("> ")
        if all == "1":
            print("\n")
            entire()

    #print("Caleb was here")

#=================================================================================================
#=====================================graphical game now==========================================
#=================================================================================================

pygame.init()
WIDTH = 900
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mega Tic Tac Toe")

running = True
while running:
    screen.fill((255, 255, 255))

    pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 900), 10)
    pygame.draw.line(screen, (0, 0, 0), (600, 0), (600, 900), 10)
    pygame.draw.line(screen, (0, 0, 0), (0, 300), (900, 300), 10)
    pygame.draw.line(screen, (0, 0, 0), (0, 600), (900, 600), 10)

    for x_offset in (0, 300, 600):
        pygame.draw.line(screen, (0, 0, 0), (100 + x_offset, 0), (100 + x_offset, 300), 5)
        pygame.draw.line(screen, (0, 0, 0), (200 + x_offset, 0), (200 + offset, 300), 5)
        
        #pygame.draw.line(screen, (0, 0, 0), (700 + offset, 0), (700 + offset, 300), 5)
        #pygame.draw.line(screen, (0, 0, 0), (800 + offset, 0), (800 + offset, 300), 5)

        pygame.draw.line(screen, (0, 0, 0), (0, 100 + offset), (300, 100 + offset), 5)
        pygame.draw.line(screen, (0, 0, 0), (0, 200 + offset), (300, 200 + offset), 5)

    for y_offset in (-300, 0, 300):
        pygame.draw.line(screen, (0, 0, 0), (400 + offset, 0), (400 + offset, 300), 5)
        pygame.draw.line(screen, (0, 0, 0), (500 + offset, 0), (500 + offset, 300), 5)


    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()