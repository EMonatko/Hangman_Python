def Letter_Guessed():
    "gives an input to guessed letter"
    guess_a_letter = input("Guess a letter:  ")
    guess_a_letter = guess_a_letter.lower()
    print("You chose", guess_a_letter)
    return guess_a_letter


def is_valid_input(letter_guessed):
    "Erorrs that can occur during wrong input If there there correct input it will lower the capital letter"
    i = len(letter_guessed)
    ASCII = ord(letter_guessed[i - 1])
    value_status="False"
    #print("ASCII =", ASCII, "Len i =", i)
    if i > 1 and (64 < ord(letter_guessed[i - 1]) < 91 or 96 < ord(
            letter_guessed[i - 1]) < 123):  ##Checking if there more than two letters
        letter_guessed = print("E1")  # Two letters error
        letter_guessed = bool(letter_guessed)

    elif i > 1 and 0 < ASCII < 65 or 90 < ASCII < 97 or ASCII > 122:  # ASCII Symbols numbers
        letter_guessed = print("E3")  # Symbol Error
        letter_guessed = bool(letter_guessed)

    elif i < 2 and 0 < ASCII < 65 or 90 < ASCII < 97 or ASCII > 122:  # ASCII Symbols numbers:
        letter_guessed = print("E2")  # Symbol Error
        letter_guessed = bool(letter_guessed)

    elif i == 1 and 96 < ord(letter_guessed[i - 1]) < 123:  ##Checking if there more than two letters
        letter_guessed = letter_guessed.lower()

    return letter_guessed

def check_valid_input(letter_guessed, old_letters_guessed):
    old_letters_guessed(letter_guessed)
    num=len(old_letters_guessed)
    for num_of_letters in num
    if letter_guessed==num_of_letters
        print('This letter has been used /n Please try again.')
        letter_guessed='False'
    else
        print('Guess another letter')
        letter_guessed = 'True'


def main():
    print("def main")
    old_letters_guessed=[];

    for num in range(5)
    letter_guessed=Letter_Guessed()
    letter_guessed=is_valid_input(letter_guessed)
    valid_input=check_valid_input(letter_guessed, old_letters_guessed)
    print(letter_guessed)
if __name__ == "__main__":
    main()
