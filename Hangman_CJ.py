#hangman_CJ
#
#Carlitos CK
#

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
    return letter

def display_board(solved):
    print(solved)

def show_result():
    print("Are you a robot??")
    
def play():
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    
    strikes = 0
    limit = 6
    
    display_board(solved)

    while solved != puzzle:
        letter = get_guess()

        if letter not in puzzle:
            pass
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)
        
    show_result()
    
    
play()

