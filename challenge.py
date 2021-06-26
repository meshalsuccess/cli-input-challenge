""" This is the challenge of making a command line that accepts whole numbers, fractions, and improper fractions and
performs addition, subtraction, division, and multiplication then return a whole number or a fraction if possible

First, I will implement a naive solution that makes the program works then I will work toward finding an optimal one
Steps:
1- take an input -- string 
2- find the operator -- has spaces around it
3- find the right side number and the left side number - relative to the operator
4- check the condition of each number, if it is whole, proper fraction, or improper fraction and solve it
5- put right number, operator, left number together and look for an evaluation technique
6- the answer will be mostly float type, seperate whole and integer from each other, and get the 
"""

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

    #5- put right number, operator, left number together and look for an evaluation technique
    answer = eval(str(leftFinalNum) + usedOperator + str(rightFinalNum))
    return answer

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

#helper function that takes a string containing a fraction and returns a float
def breakingNum(numToBreak):
    dividor = numToBreak.index('_') #since the _ sign is the dividor between whole number and fraction
    wholeNum = numToBreak[ : dividor]
    fraction = numToBreak[dividor+1 :]
    num = int(wholeNum) + eval(fraction)
    return num
print(cliChallenge("12_1/2   +    5_1/4"))