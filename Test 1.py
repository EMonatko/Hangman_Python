def Reset_func():
    attempts = 0
    max_attempts = 4
    letters_used = []
    hidden = []
    return attempts, max_attempts, letters_used, hidden


def Logo():
    hangman_logo = print("""
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                        |____/                       
    """)

    return


def Secret_word(num):
    word = ["Dictionary", "Crocodile", "Refrigerator", "Garden", "Translator"]

    return word[num], len(word)


def print_hangman(num_of_tries):
    if num_of_tries < 0:
        num_of_tries = 0
    elif num_of_tries == 0:
        return (print("""
        (    x-------x )
        (    |         )
        (    |         )
        (    |         )
        (    |         )
        (    |         )
        """))

    elif num_of_tries == 1:
        return (print("""
        (    x-------x )
        (    |       | )
        (    |       0 )
        (    |         )
        (    |         )
        (    |         )
        """))

    elif num_of_tries == 2:
        return (print("""
        (    x-------x )
        (    |       | )
        (    |       0 )
        (    |       | )
        (    |         )
        (    |         )
        """))

    elif num_of_tries == 3:
        return (print("""
        (    x-------x  )
        (    |       |  )
        (    |       0  )
        (    |      /|\ )
        (    |          )
        (    |          )
        """))

    elif num_of_tries == 4:
        return (print("""
        (    x-------x  )
        (    |       |  )
        (    |       0  )
        (    |      /|\ )
        (    |      /   )
        (    |          )
        """))

    elif num_of_tries == 5:
        return (print("""
        (    x-------x  )
        (    |       |  )
        (    |       0  )
        (    |      /|\ )
        (    |      / \ )
        (    |          )
        """ "\n\n\n GAME OVER"))

    else:
        print(" !!!!!!!!!!!!!!!!!!!!!!!! \n !!!!!Out of options!!!!! \n !!!!!!!!!!!!!!!!!!!!!!!!")


def Error_Geuss_Letter(letter_guessed, secret_word, number_of_tries):
    abc = "abcdefghijklmnopqrstuvwxyz"
    e1 = False
    e3 = False
    letter_guessed = letter_guessed.lower()
    is_any_error = is_valid_input(letter_guessed)

    if is_any_error == True:
        if letter_guessed in secret_word.lower():
            is_any_error = False
        elif letter_guessed in abc:
            number_of_tries = number_of_tries
        else:
            number_of_tries = number_of_tries - 1

    elif len(letter_guessed) != 1:
        number_of_tries -= 1
        if len(letter_guessed) == 0:
            e3 = True
        for j in range(len(letter_guessed)):
            if letter_guessed[j].lower() in abc:
                e1 = True
            else:
                e3 = True
        if e3:
            print("E2 - Symbol\s error "
                  "please try again.")
        elif e1:
            print("E1 - Multiple letters error  "
                  "please try again.")
        elif e1 and e3:
            print("E3 - Letter\s & Symbol\s error "
                  "please try again.")

    return letter_guessed, is_any_error, number_of_tries

def is_valid_input(letter_guessed):

    abc = "abcdefghijklmnopqrstuvwxyz"
    if letter_guessed in abc:
        state = True
    else:
        state = False

    return state


def check_valid_input(letter_guessed, old_letters_guessed):

    return

def main():
    # Main Parameters:
    attempts, max_attempts, letters_used, hidden = Reset_func()
    index = 0
    # Show game logo
    Logo()
    # Setup the word and hidden list
    word, list_num = Secret_word(index)
    word_backup = word
    for character in word:
        hidden.append("_")                      #I need add a fun?

    # loop until either the player has won or lost
    isGameOver = False
    while not isGameOver:

        # display the current board, guessed letters, and attempts remaining
        print(f"Life:  {max_attempts - attempts}")
        print(f"The current word is: {hidden}")
        print_hangman(attempts)
        # ask the player for a character
        letterGuessed = input("Please guess a letter: ")
        #check_valid_input(letter_guessed, old_letters_guessed)
        letters_used += letterGuessed
        hidden.append("_")
        print('\n\n')
        # Special case if WHOLE word is correct
        if letterGuessed.lower() == word_backup.lower():
            print("Great Job!"
                  "You guessed correctly! the word is: ", word_backup)
            print("You used the following letters:\n", letters_used)
            word = list(word)
            for i in range(len(word_backup)):
                hidden[i] = word[i]
                word[i] = "_"

            # Wrong case/ one letter
        if not (word == list(word)):
            letterGuessed, error, attempts = Error_Geuss_Letter(letterGuessed, word, attempts)
        print("You used the following letters:\n", letters_used)
        if not error:
            if letterGuessed in word.lower():

                # if the player guessed correct, show all matched letters and print message
                print(f"You guessed correctly! {letterGuessed} is in the word")
                for i in range(len(word)):
                    character = word[i]
                    if character.lower() == letterGuessed:
                        hidden[i] = word[i]
                word_temp = word.lower()
                word = word_temp.replace(letterGuessed, '_')
        else:
            # if player guessed wrong, print failure message and increment attempts
            print(f"You guessed wrong! {letterGuessed} is NOT in the word")
            attempts += 1
        print("Used letters: \n")
        letters_used
        # if the player has won print a win message and stop looping
        if all("_" == char for char in word):
            print_hangman(attempts)
            print("Congrats, you won! \n ")
            choice = input("Do you want to try another word? Y/N: ")
            while not (choice.lower() == 'n') and not (choice.lower() == 'y'):
                choice = input('Do you want to try another word? Y/N: ')
            if choice.lower() != 'n' or choice.lower() != 'y':
                if choice.lower() == 'y':
                    print("\nGuess the Next word\n")
                    index += 1
                    if index < list_num - 1:
                        word, list_num = Secret_word(index)
                        attempts = 0
                        hidden = []
                        word_backup = word
                        letters_used_index = 0
                        for character in word:
                            hidden.append("_")

                    else:
                        print("You are a champion!!"
                              "You guessed all words :) ")
                        isGameOver = True

                elif choice.lower() == 'n':
                    print("Thanks for playing see you next time :) ")
                    isGameOver = True

        # if the player has lost, print failing and stop looping
        if attempts >= max_attempts:
            print_hangman(attempts + 1)
            print("You lost, rest in peace!")
            isGameOver = True


if __name__ == "__main__":
    main()
