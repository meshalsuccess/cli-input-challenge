""" This is the challenge of making a command line that accepts whole numbers, fractions, and improper fractions and
performs addition, subtraction, division, and multiplication then return a whole number or a fraction if possible

First, I will implement a naive solution that makes the program works then I will work toward finding an optimal one
Steps:
1- take an input -- string 
2- find the operator -- has spaces around it
3- find the right side number and the left side number - relative to the operator
4- check the condition of each number, if it is whole, proper fraction, or improper fraction and solve it to become in form of x/x improper fraction
5- check the operation type as the calculation differes based on the operations
6- simplify the improper fractions to become proper ones before printing them to the user
"""

def cliChallenge(operation):
    """
    This is the main function that calls other helper funcions and returns the final answer as a string

    In this function, the numbers will be mostly strings not integers and when needed, the helper function will convert them to integers to ensure consistency.
    """
    operatorsList = ["*", "/", "+","-"] #since the operation are stricted to be only four operation, they are mentioned here
    ##2- find the operator --  Loop in the string till we find the operator that has a space before & after it and it is in the list
    operatorIdx = 1
    while operatorIdx < len(operation):
        if operation[operatorIdx -1] == " " and operation[operatorIdx +1] == " " and operation[operatorIdx] in operatorsList:
            usedOperator = operation[operatorIdx] #assigning the operator to usedOperator variables to be used later
            break #now operatorIdx is pointing to the operator
        operatorIdx +=1
    
    ##3- find the right side number and the left side number
    leftSide = operation[ : operatorIdx] #this will assign the entire elements of the string before the operator to the rightNum
    rightSide = operation[operatorIdx+1:  ] #this will assign the entire elements of the string after the operator to the leftNum

    ##4- check the condition of each number, if it is whole, proper fraction, or improper fraction and solve it, remove spaces
    rightNum =removingSpaces(rightSide)
    leftNum = removingSpaces(leftSide) #both right and left are spaceless now
    leftFinalNum = breakingNum(leftNum)
    rightFinalNum = breakingNum(rightNum) #string in the form of x/x

    ##5- check the operation type
    if usedOperator == '+':
        answerTuple = additionFunction(leftFinalNum, rightFinalNum)
        finalAnswer = str(answerTuple[0]) + '/' + str(answerTuple[1])
    elif usedOperator == '-':
        answerTuple = subtractionFunction(leftFinalNum, rightFinalNum)
        finalAnswer = str(answerTuple[0]) + '/' + str(answerTuple[1])
    return finalAnswer

#helper function to reduce redundant code. It takes a string and removes all the spaces from it
def removingSpaces(numToClean): 
    idx = 0
    cleanNum = "" #intialing an empty string to add to it the characters
    while idx < len(numToClean) :
        if numToClean[idx] == " ":
            idx +=1 #without this we will have an infinite loop
            continue #if the current pointer points at a space, then we ignore it and continue
        else:
            cleanNum += numToClean[idx] #adding to the rightNum empty string
            idx +=1 #preventing incrementing
    return cleanNum

def breakingNum(numToBreak):
    """
    
    Helper function that takes a string containing a fraction and returns a string of x/x.

    The function checks if the number is whole or not first then perform the calculations necessary.
    The '_' is the key.

    """
    if "_" in numToBreak: #if there is _ then we have a fraction and a whole number
        dividor = numToBreak.index('_') #since the _ sign is the dividor between whole number and fraction
        wholeNum = numToBreak[ : dividor]
        fraction = numToBreak[dividor+1 :] #the fraction is a string now in the form of x/x
        dividor = fraction.index('/')
        nom = fraction[ : dividor] #this will assign the characters before / to nom
        denom = fraction[dividor +1 : ] #this will assign the characters after / to denom
        num = convertToFraction(wholeNum, denom, nom) #pass them as strings, returns a string in the form of x/x improper fraction
        return num
    elif "_" not in numToBreak and "/" in numToBreak: #if we do not have _ and only /, that means we have a fraction already
        return numToBreak 
    else: #if there is not _ and no / but we have a number, that means it's a whole number or integer
        num = str(numToBreak) + '/' + str(1) #assigning 1 as a denom will help in calculations later
        return num

#helper function that converts decimal into fraction
def convertToFraction(wholeNum, denom, nom):
    
    denom, nom, wholeNum = int(denom), int(nom), int(wholeNum) #changing the types of strings to integers
    newNom = wholeNum * denom + nom
    fraction = str(newNom) + '/' + str(denom) # now we have an improper fraaction that is the equivelant of x_x/x
    return fraction

def findingNom(fraction):
    """
    Helper function that takes a string in the from of x/x and seperates the nom and denom and returns them as integers in a tuple.

    """
    dividor = fraction.index('/') #the / is the dividor sign
    nom = fraction[ : dividor]
    denom = fraction[dividor+1 : ]
    return int(nom), int(denom)

def additionFunction(left, right):
    """
    The addition function performs addition to fractions only.

    Steps:
    a) if the denom of both are equal, then it adds the noms
    b) if the denoms are not equal, then it finds the Least Common Multiple and multiplies are noms and denoms then adds noms together
    c) returns a tuple of integers nom,denom format

    """
    #the left and right numbers are strings in the form of x/x
    left = findingNom(left)
    right = findingNom(right)
    leftNom, leftDenom = left[0], left[1] #integers
    rightNom, rightDenom = right[0], right[1] #integers
    
    #Step a:
    if leftDenom == rightDenom:
        answerNom = leftNom + rightNom
        answerDenom = leftDenom
    else: #Step b:
        multiplyerTuple = multiplyer(leftDenom, rightDenom, LCM(leftDenom, rightDenom)) #calling helping functions to find multiplyers, integers
        leftMultiplyer, rightMultiplyer = multiplyerTuple[0], multiplyerTuple[1]
        leftNom *= leftMultiplyer
        leftDenom *= leftMultiplyer
        rightNom *= rightMultiplyer
        rightDenom *= rightMultiplyer #now all denoms are equal and the noms were multiplied to have the fractios balanced
        answerNom = leftNom + rightNom #adding noms to solve for addition
        answerDenom = leftDenom
    return answerNom, answerDenom

def subtractionFunction(left, right):
    """
    The subtraction function performs subtraction used to fractions only.

    Steps:
    a) if the denom of both are equal, then it subtract the noms
    b) if the denoms are not equal, then it finds the Least Common Multiple and multiplies are noms and denoms then subtract noms in the order left - right
    c) returns a tuple of integers nom,denom format

    """
    #the left and right numbers are strings in the form of x/x
    left = findingNom(left)
    right = findingNom(right)
    leftNom, leftDenom = left[0], left[1] #integers
    rightNom, rightDenom = right[0], right[1] #integers

    #Step a:
    if leftDenom == rightDenom:
        answerNom = leftNom - rightNom
        answerDenom = leftDenom
    else: #Step b:
        multiplyerTuple = multiplyer(leftDenom, rightDenom, LCM(leftDenom, rightDenom)) #calling helping functions to find multiplyers, integers
        leftMultiplyer, rightMultiplyer = multiplyerTuple[0], multiplyerTuple[1]
        leftNom *= leftMultiplyer
        leftDenom *= leftMultiplyer
        rightNom *= rightMultiplyer
        rightDenom *= rightMultiplyer #now all denoms are equal and the noms were multiplied to have the fractios balanced
        answerNom = leftNom - rightNom #subtracting noms to solve for subtraction
        answerDenom = leftDenom
    return answerNom, answerDenom

def LCM(leftDenom, rightDenom):
    if leftDenom > rightDenom:
        highest = leftDenom
    elif rightDenom > leftDenom:
        highest = rightDenom
    else:
        return 1
    while True:
        if highest % leftDenom == 0 and highest % rightDenom == 0:
            break
        highest +=1
    return highest

def multiplyer(leftDenom,rightDenom, lcm):
    leftMultiplyer = lcm//leftDenom
    rightMultiplyer = lcm//rightDenom
    return leftMultiplyer, rightMultiplyer

print(cliChallenge(" 1_5/7  -    5"))