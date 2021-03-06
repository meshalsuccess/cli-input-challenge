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
7- Check if there are multiple operations. if there are multiple ones, call multiple operation function, else contine
"""
from helperFunctions import removingSpaces, breakingNum, simplify, checkIfValid
from operations import operationFunctionSelector
import multipleOperations
def cliChallenge(operation):
    """
    This is the main function that calls other helper funcions and returns the final answer as a string

    In this function, the numbers will be mostly strings not integers and when needed, the helper function will convert them to integers to ensure consistency.
    """
    usedOperatorList = [] #creating an empty list to add operators to and check if the length is > 1
    operatorsList = ["*", "/", "+","-"] #since the operation are stricted to be only four operation, they are mentioned here
    ##2- find the operator --  Loop in the string till we find the operator that has a space before & after it and it is in the list
    operatorIdx = 1
    while operatorIdx < len(operation)-1:
        if operation[operatorIdx -1] == " " and operation[operatorIdx +1] == " " and operation[operatorIdx] in operatorsList:
            temp = ' ' + operation[operatorIdx] + ' '
            usedOperatorList.append(temp) #appending the operators to the used operators list
            #break #now operatorIdx is pointing to the operator
        operatorIdx +=1
    #check if the length of the operators used is >1, if not continoue, if yes, call multiple helper function
    if len(usedOperatorList) == 1:
        usedOperator = usedOperatorList[0] #assigning the operation entered from user to UsedOperator
        ##3- find the right side number and the left side number
        operatorIdx = operation.index(usedOperatorList[0]) + 1 #reassigning the operatodIdx to become the exact index of the operator
        leftSide = operation[ : operatorIdx] #this will assign the entire elements of the string before the operator to the rightNum
        rightSide = operation[operatorIdx+1:  ] #this will assign the entire elements of the string after the operator to the leftNum

        ##4- check the condition of each number, if it is whole, proper fraction, or improper fraction and solve it, remove spaces
        rightNum =removingSpaces(rightSide)
        leftNum = removingSpaces(leftSide) #both right and left are spaceless now
        if checkIfValid(leftNum) == None or checkIfValid(rightNum) == None:
            return False
        leftFinalNum = breakingNum(leftNum)
        rightFinalNum = breakingNum(rightNum) #string in the form of x/x

        ##5- check the operation type
        finalAnswer = operationFunctionSelector(leftFinalNum, rightFinalNum, usedOperator)
        try:
            finalAnswer = simplify(finalAnswer)
            return str(finalAnswer) if finalAnswer != False else False
        except:
            return False

    elif len(usedOperatorList) > 1:
        return multipleOperations.multiOperation(operation, usedOperatorList)
    else:
        print("Please enter an operation or add spaces between numbers and operators")
        return False

#print(cliChallenge(" -36_1/2  /    -35"))