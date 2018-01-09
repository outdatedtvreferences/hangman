#Hangman
#By David Burton

import random
import math

name = input("What is your name?")
game_start = True
while game_start:
    language = input("Would you like to play in english or spanish " + name + "?")
    if str.lower(language) == "english":
        answer = input("Would you like to play the normal version where you guess the word or where somebody else enters the word for you " + name + "? Enter 'normal' or 'self'.")
        if str.lower(answer) == "normal":
            game_work = True
            while game_work:
                def get_puzzle():
                    words = ["Mario", "Samus", "Link", "Star Fox", "Pit"]
                    return str.lower(random.choice(words))

                def get_solved(puzzle, guesses):
                    solved = ""

                    for letter in puzzle:
                        if letter in guesses:
                            solved += letter
                        elif letter == " ":
                            solved += " "
                        else:
                            solved += "-"

                    return solved

                def get_guess():
                    while True:
                        letter = input("Guess a letter " + name + ": ")

                        if len(letter) == 1:
                            return letter
                        else:
                            print("I don't understand " + name + ". Please enter 1 character.")

                def display_board(solved, strikes, correct_guesses, incorrect_guesses):
                    print(solved)
                    print("Strikes: " + str(strikes))
                    print("Correct Guesses: " + str(correct_guesses))
                    print("Incorrect Guesses: " + str(incorrect_guesses))

                def beginning_splash_screen():
                    print("*************")
                    print("***WELCOME***")
                    print("*****TO*****")
                    print("***THE***")
                    print("****HANGMAN****")
                    print("****GAME*****")
                    print("*************")

                def end_splash_screen():
                    print("*************")
                    print("*****Bye*****")
                    print("*****See*****")
                    print("*****You*****")
                    print("**Again Soon**")
                    print("*************")
                    print("BY: DAVID BURTON")
                    print("COMPLETED: NOVEMBER 9")
                    
                def display_man(strikes):
                    if strikes == 0:
                        print(" _________")
                        print(" |        |")
                        print(" |")
                        print(" |")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 1:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 2:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |        |")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 3:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |       /|")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 4:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |       /|\ ")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 5:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |       /|\    ._.")
                        print(" |       /")
                        print(" |")
                        print(" |")
                        
                    else:
                        print(" _________             ______")
                        print(" |        |      |     |")
                        print(" |        0      |     |")
                        print(" |       /|\     |_____|_____")
                        print(" |       / \           |    |")
                        print(" |                     |    |")
                        print(" |                _____|    |")
                              
                def show_result(strikes):
                    if strikes < limit + 1:
                        print("You Win " + name + "!")
                    else:
                        print("You lose... Good try though " + name + "!")

                def show_credits():
                    print("Thanks for playing " + name + "! I'll see you next time!")

                def play_again():
                    while True:
                        decision = input("Would you like to play again " + name + "? (y/n) ")

                        if decision == 'y' or decision == 'yes':
                            return True
                        elif decision == 'n' or decision == 'no':
                            return False
                        else:
                            print("I don't understand " + name + ". Please enter 'y' or 'n'.")
                            
                def play(strikes, limit):
                    puzzle = get_puzzle()
                    guesses = ""
                    correct_guesses = ""
                    incorrect_guesses = ""
                    solved = get_solved(puzzle, guesses)

                    print(solved)

                    while solved != puzzle:
                        letter = get_guess()

                        if letter not in puzzle:
                            strikes += 1
                            incorrect_guesses += letter
                            if strikes == limit + 1:
                                break
                        else:
                            correct_guesses += letter
                        
                        guesses += letter
                        solved = get_solved(puzzle, guesses)
                        display_man(strikes)
                        display_board(solved, strikes, correct_guesses, incorrect_guesses)

                    show_result(strikes)
                beginning_splash_screen()

                strikes = 0
                limit = 6
                    
                playing = True

                while playing:
                    print("You have " + str(limit) + " tries.")
                    play(strikes, limit)
                    playing = play_again()

                end_splash_screen()
                show_credits()
                game_start = False
                game_work = False
        elif str.lower(answer) == "self":
            game_work = True
            while game_work:
                def get_puzzle():
                    word = input("Please get somebody to type in a word that they would like you to guess " + name + ". Turn your head away as they do so.... ")
                    return word
                def get_solved(puzzle, guesses):
                    solved = ""

                    for letter in puzzle:
                        if letter in guesses:
                            solved += letter
                        elif letter == " ":
                            solved += " "
                        else:
                            solved += "-"

                    return solved

                def get_guess():
                    while True:
                        letter = input("Guess a letter " + name + ": ")

                        if len(letter) == 1:
                            return letter
                        else:
                            print("I don't understand " + name + ". Please enter 1 character.")

                def display_board(solved, strikes, correct_guesses, incorrect_guesses):
                    print(solved)
                    print("Strikes: " + str(strikes))
                    print("Correct Guesses: " + str(correct_guesses))
                    print("Incorrect Guesses: " + str(incorrect_guesses))

                def beginning_splash_screen():
                    print("*************")
                    print("***WELCOME***")
                    print("*****TO*****")
                    print("***THE***")
                    print("****HANGMAN****")
                    print("****GAME*****")
                    print("*************")

                def end_splash_screen():
                    print("*************")
                    print("*****Bye*****")
                    print("*****See*****")
                    print("*****You*****")
                    print("**Again Soon**")
                    print("*************")
                    print("BY: DAVID BURTON")
                    print("COMPLETED: NOVEMBER 9")
                    
                def display_man(strikes):
                    if strikes == 0:
                        print(" _________")
                        print(" |        |")
                        print(" |")
                        print(" |")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 1:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 2:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |        |")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 3:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |       /|")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 4:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |       /|\ ")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 5:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |       /|\    ._.")
                        print(" |       /")
                        print(" |")
                        print(" |")
                        
                    else:
                        print(" _________             ______")
                        print(" |        |      |     |")
                        print(" |        0      |     |")
                        print(" |       /|\     |_____|_____")
                        print(" |       / \           |    |")
                        print(" |                     |    |")
                        print(" |                _____|    |")
                              
                def show_result(strikes):
                    if strikes < limit + 1:
                        print("You Win " + name + "!")
                    else:
                        print("You lose... Good try though " + name + "!")

                def show_credits():
                    print("Thanks for playing " + name + "! I'll see you next time!")

                def play_again():
                    while True:
                        decision = input("Would you like to play again " + name + "? (y/n) ")

                        if decision == 'y' or decision == 'yes':
                            return True
                        elif decision == 'n' or decision == 'no':
                            return False
                        else:
                            print("I don't understand " + name + ". Please enter 'y' or 'n'.")
                            
                def play(strikes, limit):
                    puzzle = get_puzzle()
                    for i in range(40):
                        print("")
                    beginning_splash_screen()
                    print("You have " + str(limit) + " tries.")
                    guesses = ""
                    correct_guesses = ""
                    incorrect_guesses = ""
                    solved = get_solved(puzzle, guesses)

                    print(solved)

                    while solved != puzzle:
                        letter = get_guess()

                        if letter not in puzzle:
                            strikes += 1
                            incorrect_guesses += letter
                            if strikes == limit + 1:
                                break
                        else:
                            correct_guesses += letter
                        
                        guesses += letter
                        solved = get_solved(puzzle, guesses)
                        display_man(strikes)
                        display_board(solved, strikes, correct_guesses, incorrect_guesses)

                    show_result(strikes)
                
                strikes = 0
                limit = 6
                    
                playing = True

                while playing:
                    play(strikes, limit)
                    playing = play_again()

                end_splash_screen()
                show_credits()
                game_start = False
                game_work = False
        else:
            print("I don't understand. Please enter 'normal' or self' " + name + ".")
    elif str.lower(language) == "spanish":
        answer = input("Would you like to play the normal version where you guess the word or where somebody else enters the word for you " + name + "? Enter 'normal' or 'self'.")
        if str.lower(answer) == "normal":
            game_work = True
            while game_work:
                def get_puzzle():
                    words = ["Mario", "Samus", "Link", "Star Fox", "Pit"]
                    return str.lower(random.choice(words))

                def get_solved(puzzle, guesses):
                    solved = ""

                    for letter in puzzle:
                        if letter in guesses:
                            solved += letter
                        elif letter == " ":
                            solved += " "
                        else:
                            solved += "-"

                    return solved

                def get_guess():
                    while True:
                        letter = input("Adivina una carta " + name + ": ")

                        if len(letter) == 1:
                            return letter
                        else:
                            print("No entiendo " + name + ". Por favor ingrese 1 caracter.")

                def display_board(solved, strikes, correct_guesses, incorrect_guesses):
                    print(solved)
                    print("Huelgas: " + str(strikes))
                    print("Conjeturas Correctas: " + str(correct_guesses))
                    print("Conjeturas Correctas: " + str(incorrect_guesses))

                def beginning_splash_screen():
                    print("*************")
                    print("**BIENVENIDO**")
                    print("******A******")
                    print("***HANGMAN***")
                    print("*************")

                def end_splash_screen():
                    print("*************")
                    print("*****ADIOS****")
                    print("******VER*****")
                    print("******TU*****")
                    print("**PROXIMA VEZ**")
                    print("*************")
                    print("DE: DAVID BURTON")
                    print("COMPLETO: NOVIEMBRE 9")
                    
                def display_man(strikes):
                    if strikes == 0:
                        print(" _________")
                        print(" |        |")
                        print(" |")
                        print(" |")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 1:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 2:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |        |")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 3:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |       /|")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 4:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |       /|\ ")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 5:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |       /|\    ._.")
                        print(" |       /")
                        print(" |")
                        print(" |")
                        
                    else:
                        print(" _________             ______")
                        print(" |        |      |     |")
                        print(" |        0      |     |")
                        print(" |       /|\     |_____|_____")
                        print(" |       / \           |    |")
                        print(" |                     |    |")
                        print(" |                _____|    |")
                              
                def show_result(strikes):
                    if strikes < limit + 1:
                        print("¡Tu Ganas!")
                    else:
                        print("Tu perdes... ¡Mejor suerte la próxima vez!")

                def show_credits():
                    print("¡Gracias por jugar! ¡Nos vemos la próxima vez!")

                def play_again():
                    while True:
                        decision = input("¿Te gustaría jugar de nuevo " + name + "? (y/n) ")

                        if decision == 'y' or decision == 'si':
                            return True
                        elif decision == 'n' or decision == 'no':
                            return False
                        else:
                            print("No entiendo " + name + ". Por favor ingrese 'y' o 'n'.")
                            
                def play(strikes, limit):
                    puzzle = get_puzzle()
                    guesses = ""
                    correct_guesses = ""
                    incorrect_guesses = ""
                    solved = get_solved(puzzle, guesses)

                    print(solved)

                    while solved != puzzle:
                        letter = get_guess()

                        if letter not in puzzle:
                            strikes += 1
                            incorrect_guesses += letter
                            if strikes == limit + 1:
                                break
                        else:
                            correct_guesses += letter
                        
                        guesses += letter
                        solved = get_solved(puzzle, guesses)
                        display_board(solved, strikes, correct_guesses, incorrect_guesses)
                        display_man(strikes)

                    show_result(strikes)
                beginning_splash_screen()

                strikes = 0
                limit = 6
                    
            playing = True

            while playing:
                print("Tu tienes " + str(limit) + " intentos.")
                play(strikes, limit)
                playing = play_again()

            end_splash_screen()
            show_credits()
            game_start = False
            game_work = False
        elif str.lower(answer) == "self":
            game_work = True
            while game_work:
                def get_puzzle():
                    word = input("Por favor, haga que alguien escriba una palabra que le gustaría que adivine " + name + ". Gire la cabeza de distancia, ya que lo hacen ...")
                    return word
                
                def get_solved(puzzle, guesses):
                    solved = ""

                    for letter in puzzle:
                        if letter in guesses:
                            solved += letter
                        elif letter == " ":
                            solved += " "
                        else:
                            solved += "-"

                    return solved

                def get_guess():
                    while True:
                        letter = input("Adivina una carta " + name + ": ")

                        if len(letter) == 1:
                            return letter
                        else:
                            print("No entiendo " + name + ". Por favor ingrese 1 caracter.")

                def display_board(solved, strikes, correct_guesses, incorrect_guesses):
                    print(solved)
                    print("Huelgas: " + str(strikes))
                    print("Conjeturas Correctas: " + str(correct_guesses))
                    print("Conjeturas Incorrectas: " + str(incorrect_guesses))

                def beginning_splash_screen():
                    print("*************")
                    print("**BIENVENIDO**")
                    print("*****A*****")
                    print("***HANGMAN***")
                    print("*************")

                def end_splash_screen():
                    print("*************")
                    print("*****ADIOS*****")
                    print("*****HASTA*****")
                    print("*****LA*****")
                    print("**PROXIMO**")
                    print("*************")
                    print("BY: DAVID BURTON")
                    print("COMPLETED: NOVEMBER 9")
                    
                def display_man(strikes):
                    if strikes == 0:
                        print(" _________")
                        print(" |        |")
                        print(" |")
                        print(" |")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 1:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 2:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |        |")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 3:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |       /|")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 4:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |       /|\ ")
                        print(" |")
                        print(" |")
                        print(" |")
                        
                    elif strikes == 5:
                        print(" _________")
                        print(" |        |")
                        print(" |        0")
                        print(" |       /|\    ._.")
                        print(" |       /")
                        print(" |")
                        print(" |")
                        
                    else:
                        print(" _________             ______")
                        print(" |        |      |     |")
                        print(" |        0      |     |")
                        print(" |       /|\     |_____|_____")
                        print(" |       / \           |    |")
                        print(" |                     |    |")
                        print(" |                _____|    |")
                              
                def show_result(strikes):
                    if strikes < limit + 1:
                        print("Tu Ganas" + name + "!")
                    else:
                        print("Tu perdidas... Mejor suerte la próxima vez " + name + "!")

                def show_credits():
                    print("Gracias por jugar " + name + "! Enfermo nos vemos la próxima vez!")

                def play_again():
                    while True:
                        decision = input("¿Te gustaría jugar de nuevo? " + name + "? (y/n) ")

                        if decision == 'y' or decision == 'si':
                            return True
                        elif decision == 'n' or decision == 'no':
                            return False
                        else:
                            print("No entiendo " + name + ". Por favor ingrese 'y' or 'n'.")
                            
                def play(strikes, limit):
                    puzzle = get_puzzle()
                    for i in range(40):
                        print("")
                    beginning_splash_screen()
                    print("Tu tenias " + str(limit) + " probas.")
                    guesses = ""
                    correct_guesses = ""
                    incorrect_guesses = ""
                    solved = get_solved(puzzle, guesses)

                    print(solved)

                    while solved != puzzle:
                        letter = get_guess()

                        if letter not in puzzle:
                            strikes += 1
                            incorrect_guesses += letter
                            if strikes == limit + 1:
                                break
                        else:
                            correct_guesses += letter
                        
                        guesses += letter
                        solved = get_solved(puzzle, guesses)
                        display_man(strikes)
                        display_board(solved, strikes, correct_guesses, incorrect_guesses)

                    show_result(strikes)
                
                strikes = 0
                limit = 6
                    
                playing = True

                while playing:
                    play(strikes, limit)
                    playing = play_again()

                end_splash_screen()
                show_credits()
                game_start = False
                game_work = False
        else:
            print("No entiendo, por favor ingrese 'normal' o 'self'.")
    else:
        print("I don't understand " + name + ", plase enter 'english' or 'spanish'.")
