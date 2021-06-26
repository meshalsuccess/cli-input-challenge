""" This is the challenge of making a command line that accepts whole numbers, fractions, and improper fractions and
performs addition, subtraction, division, and multiplication then return a whole number or a fraction if possible

First, I will implement a naive solution that makes the program works then I will work toward finding an optimal one
Steps:
1- take an input -- string 
2- find the operator -- has spaces around it
3- find the right side number and the left side number - relative to the operator
4- check the condition of each number, if it is whole, proper fraction, or improper fraction and solve it
5- put right number, operator, left number together and look for an evaluation technique
6- the answer will be mostly float type, seperate whole and integer from each other, and return the fraction in the right format as a string
7- to convert a decimal to fraction, 
    7.1- multiply by accuracy decimals (3 decimals == 1000) 
    7.2- divide by accuracy to balance the number (without this the number will change)
    7.3- find the GCD between the nom and denom
    7.4- divide both nom and denom by GCD and we will have the simplist format
"""
import math

def cliChallenge(operation):
    #operation += " "
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
    rightFinalNum = breakingNum(rightNum) #now both are floats

    ##5- put right number, operator, left number together and look for an evaluation technique
    answer = eval(str(leftFinalNum) + usedOperator + str(rightFinalNum))

    ##6- return the fraction in the right format as a string -- since the format is x/x, it should be a string, 1st seperate the whole num from fraction
    ## then solve for fraction alone. if the whole num is not 0, return as x_x/x else return as x/x or x only
    wholeNumAns = int(answer) #this will round down always even if it is 9.999 will be 9
    decimealAns = answer - wholeNumAns #this will give us the decimal that should be converted into a fraction
    fraction = convertToFraction(decimealAns) #calling helper function
    finalAnswer = str(wholeNumAns) + "_" + fraction
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
    
    Helper function that takes a string containing a fraction and returns a float.

    The function checks if the number is whole or not first then perform the calculations necessary.
    The '_' is the key.

    """
    if "_" in numToBreak: #if there is _ then we have a fraction and a whole number
        dividor = numToBreak.index('_') #since the _ sign is the dividor between whole number and fraction
        wholeNum = numToBreak[ : dividor]
        fraction = numToBreak[dividor+1 :]
        num = int(wholeNum) + eval(fraction)
    elif "_" not in numToBreak and "/" in numToBreak: #if we have only / and no _ then we have a fraction only
        num = eval(numToBreak) #evaluating the fraction will make it a decimal number
    else: #if there is not _ and no / but we have a number, that means it's a whole number or integer
        num = int(numToBreak)
    return num

#helper function that converts decimal into fraction
def convertToFraction(numToConvert):
    nom = numToConvert * 1000 #adding the accuracy
    denom = 1000
    gcd = math.gcd(int(nom),denom)

    nom /= gcd
    denom /= gcd
    fraction = str(int(nom)) + "/" + str(int(denom))
    return fraction

print(cliChallenge(" 1  +    5_1/4"))