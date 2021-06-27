"""
This script has the helping function needed.

"""
import math
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
        num = convertToFraction(wholeNum, denom, nom) #pass them as strings, returns a string in the form of x/x improper fraction
        return num
    elif "_" not in numToBreak and "/" in numToBreak: #if we do not have _ and only /, that means we have a fraction already
        return numToBreak 
    else: #if there is not _ and no / but we have a number, that means it's a whole number or integer
        num = str(numToBreak) + '/' + str(1) #assigning 1 as a denom will help in calculations later
        return num


def convertToFraction(wholeNum, denom, nom):
    """
    Helper function that takes a strings and returns improper function.

    It uses the mathematical formula of creating improper functions.
    """    
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
    """
    
    Helper function that balances the left and right noms.

    It does that by finding how much the denoms had to by multiplied so the noms get multiplied similarly. Often, the values are different and it is important to balance
    each fraction for later calculations.

    """
    leftMultiplyer = lcm//leftDenom
    rightMultiplyer = lcm//rightDenom
    return leftMultiplyer, rightMultiplyer

def simplify(fraction):
    """
    Helper function that simplifies a fraction if it is improper and returns a string.

    """
    num = findingNom(fraction)
    nom, denom = num[0], num[1]

    if nom == denom:
        return 1
    elif nom < denom:
        if nom == 0:
            return 0
        finalFraction = str(nom) + '/' + str(denom)
        return finalFraction
    GCF = math.gcd(nom,denom)
    nom //= GCF
    denom //= GCF
    if denom == 1:
        return nom
    wholeNum = 0
    while nom > denom:
        wholeNum += 1
        nom -= denom

    finalAnswer = str(wholeNum) + '_' + str(nom) + '/' + str(denom) 
    return finalAnswer