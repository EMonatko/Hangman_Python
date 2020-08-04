#### ALL FUNCTIONS!
#
def Reset_func():
    attempts = 0
    max_attempts = 4
    letters_used = []
    hidden = []
    return attempts, max_attempts, letters_used, hidden
	
#
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

#
def Secret_word(num):
    word = ["Dictionary", "Crocodile", "Refrigerator", "Garden", "Translator"]

    return word[num], len(word)

#
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

#
def Error_Geuss_Letter(letter_guessed, secret_word, number_of_tries):
    abc = "abcdefghijklmnopqrstuvwxyz"
    e1 = False
    e3 = False
    letter_guessed = letter_guessed.lower()
    is_any_error = is_valid_input(letter_guessed)

    if is_any_error:
        if letter_guessed in secret_word.lower():
            is_any_error = False
        elif letter_guessed in abc:
            number_of_tries = number_of_tries
        else:
            number_of_tries = number_of_tries - 1

    elif not is_any_error:
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

#
def is_valid_input(letter_guessed):
    abc = "abcdefghijklmnopqrstuvwxyz"
    if letter_guessed in abc:
        state = True
    else:
        state = False

    return state

#
def is_valid_input(letter_guessed):
    abc = "abcdefghijklmnopqrstuvwxyz"
    if letter_guessed in abc:
        state = True
    else:
        state = False

    return state

#

#