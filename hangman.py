# hangman game

guessWord = input("Enter a guess word (blank to quit): ")

# if word inserted is blank exit the program
if not guessWord:
    print("Empty Word!")
    exit()

# variable to hold number of guesses
numberofGuesses = 0
# container where we put the correct guesses
correctguesses = []
# container where we put the wrong guesses
wrongguesses = []
# container which includes all the guesses
allGuesses = []
# keep this for displaying at the end
originalGuessWord = guessWord

# until guessword is not empty ( everytime the user guesses correctly I replace the correct letters with blank, eventually guessWord becomes blank and while loop will be terminated
while(guessWord):

    # prompt user to guess a letter
    guessLetter = input("\n\nEnter a guess letter (blank to quit):")
    # every guess, we increment the guess count
    numberofGuesses = numberofGuesses + 1

    # if empty letter is guessed, exit the program
    if not guessLetter:
        print("Empty Letter!")
        exit()

    # if guess letter is longer than 1 letter
    if(len(guessLetter) > 1):
        print("Only enter a single letter")
        # stop execution and go back to the top of the loop
        continue

    # if letter is already guessed
    if guessLetter in allGuesses:
        print("Already guessed")
        continue

    # if correct letter is found in the word
    if guessLetter in guessWord:
        print (guessLetter,end=" ")
        print ("found")
        # store the correct guessed letter inside the below container
        correctguesses.append(guessLetter)
        # replace the correct letters with blanks
        guessWord = guessWord.replace(guessLetter,"")

    else:
        print(guessLetter,end=" ")
        print("not found")
        # store the wrong guessed letters inside the below container
        wrongguesses.append(guessLetter)

    # print report every time user makes a guess
    print("Correct Guesses so far: ",end=" ")
    print(correctguesses)
    print("Wrong Guesses so far: ",end=" ")
    print(wrongguesses)
    allGuesses.append(guessLetter)
    print("Guesses so far",end=" ")
    print(allGuesses)


# end of the game reached, print report
print("\n\n")
print("*** Results ***")
print ('Word: ' + originalGuessWord)
#print(originalGuessWord)
print("Match: ",end=" ")
print(correctguesses)
print("Unmatched: ",end=" ")
print(wrongguesses)
print("Guesses: ",end=" ")
print(numberofGuesses)
