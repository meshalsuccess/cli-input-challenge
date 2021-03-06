"""
This script has the helping function needed.

"""
import math
import challenge
#helper function to reduce redundant code. It takes a string and removes all the spaces from it
def removingSpaces(numToClean): 
    """
    This function takes a string and returns it spaceless.

    Checks for each character and if a space exists, it removes. The main purpose is to have a final string that represents a number regardless if it is a fraction or not.
    """
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
    
    Helper function that takes a Spaceless string containing a number and returns a string of x/x.

    The function checks if the number is whole or not first then perform the calculations necessary.
    The '_' is the key.
    If the number is a whole number, a denom of value 1 will assigned to it

    """
    if "_" in numToBreak: #if there is _ then we have a fraction and a whole number
        dividor = numToBreak.index('_') #since the _ sign is the dividor between whole number and fraction
        wholeNum = numToBreak[ : dividor]
        fraction = numToBreak[dividor+1 :] #the fraction is a string now in the form of x/x
        dividor = fraction.index('/')
        nom = fraction[ : dividor] #this will assign the characters before / to nom
        denom = fraction[dividor +1 : ] #this will assign the characters after / to denom
        return convertToFraction(wholeNum, denom, nom) #pass them as strings, returns a string in the form of x/x improper fraction

    elif "_" not in numToBreak and "/" in numToBreak: #if we do not have _ and only /, that means we have a fraction already
        return numToBreak 
    else: #if there is not _ and no / but we have a number, that means it's a whole number or integer
        #num = returnString(numToBreak, 1) #assigning 1 as a denom will help in calculations later
        return returnString(numToBreak, 1)


def convertToFraction(wholeNum, denom, nom):
    """
    Helper function that takes a strings and returns improper function.

    It uses the mathematical formula of creating improper functions.
    """    
    denom, nom, wholeNum = int(denom), int(nom), int(wholeNum) #changing the types of strings to integers
    if wholeNum > 0:
        newNom = wholeNum * denom + nom
    else:
        newNom = abs(wholeNum) * denom + nom
        newNom *= -1
    fraction = returnString(newNom, denom) # now we have an IMPROPER fraaction that is the equivelant of x_x/x
    return fraction

def findingNom(fraction):
    """
    Helper function that takes a string in the from of x/x and seperates the nom and denom and returns them as integers in a tuple.

    """
    dividor = fraction.index('/') #the / is the dividor sign
    nom = fraction[ : dividor]
    denom = fraction[dividor+1 : ]
    return int(nom), int(denom)

def LCM(leftDenom, rightDenom):
    if leftDenom > rightDenom:
        highest = leftDenom
    elif rightDenom > leftDenom:
        highest = rightDenom
    else:
        return 1
    while True:
        try:
            if highest % leftDenom == 0 and highest % rightDenom == 0:
                break
            highest +=1
        except:
            print("Illegal Operation")
            return False
    return highest

def multiplyer(leftDenom,rightDenom, lcm):
    """
    
    Helper function that balances the left and right noms.

    It does that by finding how much the denoms had to by multiplied so the noms get multiplied similarly. Often, the values are different and it is important to balance
    each fraction for later calculations.

    """
    try:
        leftMultiplyer = lcm//leftDenom
        rightMultiplyer = lcm//rightDenom
        return leftMultiplyer, rightMultiplyer
    except:
        return False
def simplify(fraction):
    """
    Helper function that simplifies a fraction if it is improper and returns a string.

    """
    num = findingNom(fraction)
    nom, denom = num[0], num[1]
    #checking to see if we can cancel both -ve values otherwise, while loop below will be infinite
    if nom < 0 and denom < 0:
        nom, denom = abs(nom), abs(denom)
    
    if nom == denom:
        return 1 
    
    elif abs(nom) < denom and math.gcd(abs(nom), denom) == 1: #sometimes we can have nom with abs higher than denom which means we need to simplify further
        if nom == 0:
            return '0'
        finalFraction = returnString(nom, denom)
        return finalFraction
    GCF = math.gcd(abs(nom),abs(denom)) #the reason for using abs here is difinition, we cannot find gcd for -ve and +ve
    nom //= GCF #reducing both nom and denom by dividing them by gcd. this save a lot of time and we will reach simple fraction faster
    denom //= GCF

    if denom == 1: #after dividing by gcf we might find have a denom ==1 like 10/5
        return nom
    elif denom == 0:
        print("Illegal Operation")
        return False
    wholeNum = 0
    while abs(nom) > denom: #this is tricky because if the user divides by -ve value in the cli, we need to make sure the final answer is the simplist we account for it here
        wholeNum += 1
        if nom >0: #if the nom is +ve, then we have no issues subtracting
            nom -= denom
        else: #if it is not, we should add till the abs is small than denom.
            nom += denom

    if wholeNum != 0: #if we did not loop after dividing by gcd, that means we already had a proper fraction but not simple and simplified it by dividing by gfd
        finalAnswer = returnString(nom, denom, wholeNum)
    else:
        finalAnswer = returnString(nom, denom)
    return finalAnswer

def returnString(nom, denom, wholeNum = None):
    """
    Helper function that takes nom and denom and returns a fraction.

    """
    if wholeNum == None:
        finalAnswer = str(nom) + '/' + str(denom)
        
    else:
        if nom < 0:
            finalAnswer = '-' + str(wholeNum) + '_' + str(abs(nom)) + '/' + str(denom)
        else:
            finalAnswer = str(wholeNum) + '_' + str(nom) + '/' + str(denom)   
    return finalAnswer

def checkIfValid(num):
    """
    Helper function that checks if the numbers entred by the user are in the valid format.

    """
    if num[0] == '/':
        print("Illegal Operation")
        return None
    elif '/' in num:
        try:
            lastChar = int(num[-1])
            beforeChar = int(num[num.index('/') -1])
            return 1
        except:
            print("please enter the number in the right format")
            return None
    elif '_' in num and '/' not in num:
        print("please enter the number in the right format")
        return None
    elif '_' not in num and '/' not in num:
        return 1

def operationPrioritySolver(operation, operator):
    '''
    The way to solve it is to look for the second space from both sides of the operator
    then put them all together and call the challenge sovler
    the return form that will be what we need to replace the current operation with and then
    go on and do that again
    
    '''
    idx = 0
    while idx < len(operation) -1:
        if operation[idx] == operator and operation[idx - 1] == ' ' and operation[idx +1] == ' ':
            break
        idx +=1

    #intiating both indexes to point at the spaces in both sides of the operator
    leftSpaceIdx, rightSpaceIdx = idx -2, idx +2
    #the left index will find the first space to the left of the operator
    while leftSpaceIdx > 0:
        if operation[leftSpaceIdx] == ' ':
            break
        leftSpaceIdx -=1
    #the right index will find the first space to the right of the operator
    while rightSpaceIdx < len(operation):
        if operation[rightSpaceIdx] == ' ':
            break
        rightSpaceIdx += 1
    
    #creating a string with the operation
    currentOperation = challenge.cliChallenge(operation[leftSpaceIdx : rightSpaceIdx])#now we have an operation
    newCleanOperation = operation[ : leftSpaceIdx] + currentOperation + operation[rightSpaceIdx : ]
    return newCleanOperation  