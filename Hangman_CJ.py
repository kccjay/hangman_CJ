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
    solved = get_solved 
    
play()

