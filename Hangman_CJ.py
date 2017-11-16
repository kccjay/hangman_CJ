#hangman_CJ
#
#Carlitos CK
#
def splash():
    print("               _________")
    print("              |         |")
    print("              |         |")
    print("              |         |")
    print("              |         o")
    print("              |        /|")
    print("              |         ^")
    print("              |         ")
    print("              |")
    print("______________|__________________")
    print()

def end():
    print("##################################")
    print("#                                #")
    print("#     The Creator Carlitos       #")
    print("#             11/16              #")
    print("##################################")
    
def get_puzzle():
    return "mario"

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    letter = input("Guess a letter: ")
    if letter.isalpha():
        return letter
    else:
        return print("*Not a letter")

def display_board(solved):
    print(solved)

def show_result(puzzle, guesses):
    if puzzle == guesses:
        print()
        print("Are you a robot??")
        print()
    else:
        print()
        print("Try harder come on!")
        print()
    
def play():
    splash()
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    
    body_parts = 0
    human = 6
    
    display_board(solved)

    while solved != puzzle and body_parts < human:
        letter = get_guess()
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)

        body_parts += 1
        
    show_result(puzzle, guesses)
    end()
    

play()

