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

base_tic_1 = """
____|____|____ 
____|____|____ 
    |    |     
"""

base_tic_2 = """
____|____|____ 
____|____|____ 
    |    |     
"""

base_tic_3 = """
____|____|____ 
____|____|____ 
    |    |     
"""

base_tic_4 = """
____|____|____ 
____|____|____ 
    |    |     
"""

base_tic_5 =  """
____|____|____ 
____|____|____ 
    |    |     
"""

base_tic_6 = """
____|____|____ 
____|____|____ 
    |    |     
"""

base_tic_7 = """
____|____|____ 
____|____|____ 
    |    |     
"""

base_tic_8 = """
____|____|____ 
____|____|____ 
    |    |     
"""

base_tic_9 = """
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
    print(f"\n {p1} goes first")
else:
    print(f"\n {p2} goes first")

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
    1: base_tic_1,
    2: base_tic_2,
    3: base_tic_3,
    4: base_tic_4,
    5: base_tic_5,
    6: base_tic_6,
    7: base_tic_7,
    8: base_tic_8,
    9: base_tic_9
}

print(boards[grid_choice])

print("Choose a spot or type 10 to get a guide")

while True:
    try:
        spot = int(input("> "))
    except ValueError:
        print("Enter a whole number between 1 to 9")
    else:
        if spot > 9 or spot < 1:
            print("Enter a whole number between 1 to 9")
        elif spot == 10:
            print("")
        else:
            break