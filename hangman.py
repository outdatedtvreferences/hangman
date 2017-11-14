# Hangman
# David B.

def get_puzzle():
    return "hangman"

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
    print("You Win!")

def show_credits():
    print("This awesome game was created by David Burton")

def play_again():
    pass
    
def play():
    puzzle = get_puzzle
    guesses = ""
    solved = get_solved(puzzle, guesses)

    strinkes = 0
    limit = 6

    print(solved)

    while solved != puzzle:
        letter += get_guess()

        if letter not in puzzle:
            strikes += 1
            print("strikes: " + strikes)

        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)

    show_result()
    play()

    play()
