#hangman_CJ
#
#Carlitos CK
#
def splash():
    print("               _________")
    print("              |_|_|_|_|_|")
    print("              |_|_|_|_|_|")
    print("              |_|_|_|_|_|")
    print("              |_|_|_|_|_|")
    print("              |_|_|_|_|_|")
    print("              |_________|")
    print("              |_________|")
    print("              |_________|")
    print("______________|_________|_________________")
    print()

def end():
    print("##################################")
    print("#                                #")
    print("#     The Creator Carlitos       #")
    print("#             11/16              #")
    print("##################################")
    
def get_puzzle():
    return "creator"

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    while True:
        letter = input("Guess a letter: ")
        if letter.isalpha():
            return letter
        else:
            print()
            print("*Not a letter*")
            print()

def display_board(solved, guesses, body_parts):
    print(str(solved) + " (" + str(guesses) + ") " + "*" + str(body_parts + 1) + "*")

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
    
    display_board(solved, guesses, body_parts)

    while solved != puzzle and body_parts < human:
        letter = get_guess()
        guesses += str(letter)
        solved = get_solved(puzzle, guesses)
        display_board(solved, guesses, body_parts)

        body_parts += 1
        
    show_result(puzzle, guesses)
    end()
    

play()

