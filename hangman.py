def inputString():
    str = input("Please enter a word to be guessed\nthat does not contain ? or white space: ").strip()
    while (str.find("?") != -1) or (str.find(" ") != -1):
        str = input("Please enter a word to be guessed\nthat does not contain ? or white space: ").strip()
    return str.lower()
def hangman(wordToGuess):
    emptyString = ""
    hangman = [emptyString, ''' |''', 
    ''' |
 0''', 
    ''' |
 0
 |''', 
    ''' |
 0
/|''', 
    ''' |
 0
/|\\''', 
    ''' |
 0
/|\\
/''', 
    ''' |
 0
/|\\
/ \\''']
    
    activeGuess = "?" * len(wordToGuess)
    
    wrongGuesses = 0
    
    usedLetters = ""
    
    
    while (wrongGuesses < 7) and (activeGuess != wordToGuess):
        
        print("So far you have guessed:", ', '.join(usedLetters.split()))
        print(activeGuess)
        guess = input("Please enter your next guess: ").lower().strip().lstrip()
        
        while (guess == "") or (guess in usedLetters) or (len(guess) != 1):
            if (guess == ""):
                print("You must enter a guess.")
            if (guess in usedLetters):
                print("You already guessed the character:", guess)
            if (len(guess) != 1):
                print("You can only guess a single character")
            guess = input("Please enter your next guess: ").lower()
        usedLetters += guess + " "
        
        if(guess in wordToGuess):
            newActiveGuess = ""
            for letter in range(len(wordToGuess)):
                if (guess == wordToGuess[letter]):
                    newActiveGuess += guess
                else:
                    newActiveGuess += activeGuess[letter]
            activeGuess = newActiveGuess
            print(hangman[wrongGuesses])
        else:
            wrongGuesses += 1
            print(hangman[wrongGuesses])
    if wrongGuesses == 7:
        print("You failed to guess the secret word: " + wordToGuess)
    else:
        print("You correctly guessed the secret word")

hangman(inputString())
        
        