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
    #attemps = input("Choose your attempts: ")
    attemps=7
    return attemps

def Category(num):
    print("Category")
    word = ["Dictionary", "Crocodile", "Refrigerator", "Garden", "Translator"]
    print("\n", word[num], "\n")

    return (word[num].lower())

def Error_Geuss_Letter(number_of_tries):
#Need to realese guess_a_letter from 'D'
    guess_a_letter = input("Enter you letter: ")
    #guess_a_letter='u'
    i = len(guess_a_letter)
    ASCII = ord(guess_a_letter[i - 1])
    # print("ASCII =", ASCII, "Len i =", i)
    if i > 1 and (64 < ord(guess_a_letter[i - 1]) < 91 or 96 < ord(
            guess_a_letter[i - 1]) < 123):  #   Checking if there more than two letters

        print("E1")  # Two letters error


    elif i > 1 and 0 < ASCII < 65 or 90 < ASCII < 97 or ASCII > 122 or ASCII==13:  # ASCII Symbols numbers
        print("E3")  # Symbol Error

    elif i < 2 and 0 < ASCII < 65 or 90 < ASCII < 97 or ASCII > 122:  # ASCII Symbols numbers:
        print("E2")  # Symbol Error

    elif i == 1 and (64 < ord(guess_a_letter[i - 1]) < 91 or 96 < ord(
            guess_a_letter[i - 1]) < 123):  #   Checking if there more than two letters
        guess_a_letter=guess_a_letter.lower()
    return(guess_a_letter)

def Pics(tries):

    if tries == 0:
        return (print("""
            (    x         )
            (    |         )
            (    |         )
            (    |         )
            (    |         )
            (    |         )
            """))

    elif tries == 1:
        return(print("""
        (    x-------x )
        (    |         )
        (    |         )
        (    |         )
        (    |         )
        (    |         )
        """))

    elif tries == 2:
        return(print("""
        (    x-------x )
        (    |       | )
        (    |       0 )
        (    |         )
        (    |         )
        (    |         )
        """))

    elif tries == 3:
        return(print("""
        (    x-------x )
        (    |       | )
        (    |       0 )
        (    |       | )
        (    |         )
        (    |         )
        """))

    elif tries == 4:
        return(print("""
        (    x-------x  )
        (    |       |  )
        (    |       0  )
        (    |      /|\ )
        (    |          )
        (    |          )
        """))

    elif tries == 5:
        return(print("""
        (    x-------x  )
        (    |       |  )
        (    |       0  )
        (    |      /|\ )
        (    |      /   )
        (    |          )
        """))

    elif tries == 6:
        return(print("""
        (    x-------x  )
        (    |       |  )
        (    |       0  )
        (    |      /|\ )
        (    |      / \ )
        (    |          )
        """ "\n\n\n GAME OVER"))

    else:
        print(" !!!!!!!!!!!!!!!!!!!!!!!! \n !!!!!Out of options!!!!! \n !!!!!!!!!!!!!!!!!!!!!!!!")

def Valid_letter(letter_guessed, word, index, res):

    # Initialising string
    #word = 'Dictionary'

    # Character to find
    #letter_guessed = "i"
    # printing initial string and character
#    print("initial_string : ", word, "\n character_to_find : ", letter_guessed[index])
    index1 = index - 1
    res_bool = letter_guessed[index1] in word
    if res_bool == True:
    # Using Naive Method

        for i in range(0, len(word)):
            if word[i] == letter_guessed[index1]:
                res[i] = letter_guessed[index1]
        print("Character {} is present at {}".format(letter_guessed[index1], str(res)))

    else:
        print("No such charater available in string")
    return(res, res_bool)

def main():

    number_of_tries = Logo()
    print("You have", number_of_tries, "tries \n")
    num = 0 #num of words
    word = Category(num)
    print("\n def main \n", word)
    res = ["_" for x in range(len(word))]
    i=1 #index
    tries = 0
    letter_guessed = []
    Pics(tries)
    while tries < number_of_tries:
        letter_guessed += Error_Geuss_Letter(number_of_tries)   #Check input errors and lower the letter
        print(letter_guessed)
        resault, bool =Valid_letter(letter_guessed, word, i, res)   #Check if the letter contains in the word and returns true or false value
        if bool == False:
            tries = tries + 1
            if tries == number_of_tries:
                answer = input("Do you want to try again? y/n\n")
                # Reset everything.
                i = 0
                tries = 0
                letter_guessed = []
                if answer == 'y':
                    print('Pass')
                    num = num + 1
                    word = Category(num)
                else:
                    print('Game Over')
                    break;
        i = i + 1
        Pics(tries)
        print(tries)


if __name__ == "__main__":
    main()