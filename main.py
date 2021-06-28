from challenge import cliChallenge
import time
print("Script Starting!\nFraction Calculator! \nPlease, type your number in one of the following forms:\nSimple Fraction and Improper Fractions: x/x\nWhole Numbers: x\nWhole with Fractions: x_x/x")
time.sleep(1)
print("For negative number: Add the negative sign to the numbers without spaces in the form: -x_x/x\nNumbers and operators should be seperated by spaces, one or more")
time.sleep(1)
print("In case of an error, a message will printed in the screen\n'please enter the number in the right format' means the format of the number is incorrect so please, check the number and retry again")
time.sleep(1)
print("'Illegal Operation' means that an illegal mathematical operation was being performed such as dividing by zero\n\n")
time.sleep(1)
print("to stop the script type EXIT")


while True:
    time.sleep(0.5)
    userInput = input("Please enter your operation below \n")
    try:
        if userInput.lower() == 'exit':
            print("Script ended by User!")
            time.sleep(1)
            break
    except:
        continue
    possibleAnswer = cliChallenge(userInput)
    if possibleAnswer == False:
        time.sleep(1)
        print("try again!")
        continue
    else:
        time.sleep(1)
        print("answer = " + possibleAnswer)