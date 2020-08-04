
guess_a_letter=input("Enter you letter: ")
i=len(guess_a_letter)
ASCII=ord(guess_a_letter[i-1])
print("ASCII =", ASCII, "Len i =", i)
if i>1 and (64 < ord(guess_a_letter[i-1]) < 91 or 96 < ord(guess_a_letter[i-1]) < 123): ##Checking if there more than two letters

    print("E1") #Two letters error

elif i>1 and 0 < ASCII < 65 or 90 < ASCII < 97 or ASCII > 122 :    #ASCII Symbols numbers
    print("E3")  # Symbol Error

elif i<2 and 0 < ASCII < 65 or 90 < ASCII < 97 or ASCII > 122 :    #ASCII Symbols numbers:
    print("E2")  # Symbol Error

elif i==1 and (64 < ord(guess_a_letter[i-1]) < 91 or 96 < ord(guess_a_letter[i-1]) < 123): ##Checking if there more than two letters
    guess_a_letter = guess_a_letter.lower()
    print("You chose", guess_a_letter)

