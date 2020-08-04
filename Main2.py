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
    print("Secret word")
    word = ["Dictionary", "Crocodile", "Refrigerator", "Garden", "Translator"]
    print("\n", word[num], "\n")
    hidden=[]
    for character in word[num]:
        hidden.append("_")
    print(hidden)
    attempts = 0
    max_attempts = 4

    return hidden , word[num] , attempts , max_attempts

def Error_Geuss_Letter(guess_a_letter, Faltie_counter, number_of_tries, index_letters_guessed, guessed_letters):
    print(index_letters_guessed)
    i = len(guess_a_letter)
    abc = 'abcdefghijklmnopqrstuvwxyz'
    temp = []

    if i == 1:
        Faltie_counter = False
        guess_a_letter.lower()

    elif (i != 1) and (Faltie_counter == False):
        for j in range(len(guess_a_letter)):
            if guess_a_letter[j].lower() in abc:
                temp.append(guess_a_letter[j].lower())
                e1 = True
                print("E1 - Two letters error ... "
                       "please try again.")
            else:
                temp.append(guess_a_letter[j].lower())
                e3 = True
                print("E3 - Letter\s & Symbol\s error ... "
                      "please try again.")

        if e3 == True:
            print("E2 - Symbol\s error "
                    "please try again.")
        elif e1 == True:
            print("E1 - Two letters error  "
                      "please try again.")
        elif e1 == True and e3 == True:
            print("E3 - Letter\s & Symbol\s error "
                    "please try again.")

        Faltie_counter = True
        print("Wrong input ..."
              " please try again")
    elif Faltie_counter == True:
        print("You have lost 1 attempt!")
        Faltie_counter = False
        number_of_tries -= 1
    for j in range(len(guess_a_letter)):
            temp.append(guess_a_letter[j].lower())
    temp = "".join(temp)
    guessed_letters.append(temp)
    print("here is all your attempts \n", guessed_letters)



    return guess_a_letter, Faltie_counter, number_of_tries, guessed_letters

def Pics(tries):
    if tries < 0:
        tries = 0
    elif tries == 0:
        return(print("""
        (    x-------x )
        (    |         )
        (    |         )
        (    |         )
        (    |         )
        (    |         )
        """))

    elif tries == 1:
        return(print("""
        (    x-------x )
        (    |       | )
        (    |       0 )
        (    |         )
        (    |         )
        (    |         )
        """))

    elif tries == 2:
        return(print("""
        (    x-------x )
        (    |       | )
        (    |       0 )
        (    |       | )
        (    |         )
        (    |         )
        """))

    elif tries == 3:
        return(print("""
        (    x-------x  )
        (    |       |  )
        (    |       0  )
        (    |      /|\ )
        (    |          )
        (    |          )
        """))

    elif tries == 4:
        return(print("""
        (    x-------x  )
        (    |       |  )
        (    |       0  )
        (    |      /|\ )
        (    |      /   )
        (    |          )
        """))

    elif tries == 5:
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

def Valid_letter(letterGuessed, word):

    if letterGuessed in word:
        # if the player guessed correct, show all matched letters and print message
        print(f"You guessed correctly! {letterGuessed} is in the word")
        for i in range(len(word)):
            character = word[i]
            if character == letterGuessed:
                hidden[i] = word[i]
                word[i] = "_"
    else:
        # if player guessed wrong, print failure message and increment attempts
        print(f"You guessed wrong! {letterGuessed} is NOT in the word")
        attempts += 1

        # if the player has won print a win message and stop looping
        if all("_" == char for char in word):
            print("Congrats, you won!")

    return()

def main():
    num = 0
    ## Logo function just for fun with function
    Logo()
    ##
    index_letters = 0
    hidden_word, word, number_of_tries, max_number_of_tries = Secret_word(num)
    out_of_guesses = False
    Faltie_counter = False  #if user try to bypass the system and put down his attempts
    guessed_letters = []
    while not out_of_guesses:
        print("You have", max_number_of_tries - number_of_tries, "attempts remaining\n")
        print("The current word is: "+ word)
        ## Calling the pics function
        Pics(number_of_tries)
        ##
        letterGuessed = input("Please guess a letter: ")
        #letterGuessed= '@@$@EWWDS'
        #print('\n')
        letterGuessed, Faltie_counter, number_of_tries, guessed_letters = Error_Geuss_Letter(letterGuessed, Faltie_counter, number_of_tries, index_letters, guessed_letters)
        index_letters += 1

        for i in range(len(word)):
            character = word[i]
            if character == letterGuessed:
                hidden[i] = word[i]
                word[i] = "_"

        if Faltie_counter == False:
            Valid_letter(letterGuessed, word)

if __name__ == "__main__":
    main()