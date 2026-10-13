import random
import time

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
p1 = input("Player 1: ")
print("\nWhat is Player 2's name?")
p2 = input("Player 2: ")

print("\nChoosing who goes first...")
time.sleep(2)

first =random.randint(1, 2)
if first == 1:
    print(f"\n {p1} goes first and will be X")
else:
    print(f"\n {p2} goes first and will be X")

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

b1 = board_lines(boards[1])

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

game_running = True
current_player = "X"
current_board = grid_choice

while game_running:
    print(f"\nBoard: {current_board}")

    show_board(boards[current_board])

    print(blank)

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
                show_board(boards[current_board])
                current_board = spot
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