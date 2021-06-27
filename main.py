from challenge import cliChallenge

while True:
    userInput = input("Please enter your operation below \n")
    possibleAnswer = cliChallenge(userInput)
    if possibleAnswer == False:
        print("try again!")
        continue
    else:
        print(possibleAnswer)
        
    
    #print(cliChallenge(userInput))