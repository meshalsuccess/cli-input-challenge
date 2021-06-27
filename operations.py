"""

This script has the operations' functions.

Since we are using fractions, the operations performed are not straight forward.

"""

from helperFunctions import findingNom, multiplyer, LCM, returnString

def operationFunctionSelector(leftFinalNum, rightFinalNum, usedOperator):
    """
    Operation Selector selects the operation type based on operator determined in the challenge script.

    """
    if usedOperator == '+':
        answerTuple = additionFunction(leftFinalNum, rightFinalNum)
        
    elif usedOperator == '-':
        answerTuple = subtractionFunction(leftFinalNum, rightFinalNum)
        
    elif usedOperator == '*':
        answerTuple = multiplicationFunction(leftFinalNum, rightFinalNum)
       
    elif usedOperator == '/':
        answerTuple = divisionFunction(leftFinalNum, rightFinalNum)
        
    finalAnswer = returnString(answerTuple[0], answerTuple[1])  
    return finalAnswer

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

def multiplicationFunction(left, right):
    """

    The multiplication function multiplies noms together and denoms together.

    """
    #the left and right numbers are strings in the form of x/x
    left = findingNom(left)
    right = findingNom(right)
    leftNom, leftDenom = left[0], left[1] #integers
    rightNom, rightDenom = right[0], right[1] #integers
    answerNom = leftNom * rightNom #multiplying noms 
    answerDenom = leftDenom * rightDenom #multiplying denoms
    return answerNom, answerDenom

def divisionFunction(left, right):
    """

    The division function flips the right side then multiplies noms together and denoms together.

    """
    #the left and right numbers are strings in the form of x/x
    left = findingNom(left)
    right = findingNom(right)
    leftNom, leftDenom = left[0], left[1] #integers
    rightNom, rightDenom = right[1], right[0] #integers
    if rightDenom < 0 and rightNom > 0:
        rightDenom = abs(rightDenom)
        rightNom *= -1
    answerNom = leftNom * rightNom #multiplying noms 
    answerDenom = leftDenom * rightDenom #multiplying denoms
    return answerNom, answerDenom