# Code Challenge

This repo is the solution for a coding challenge to create a command line program that perform calculation on user input numbers

## Input Style

The user enters the numbers in the following format:
- X for whole number (e.g: 5)
- X/X for fractions (regardless proper or improper, e.g: 1/2)
- X_X/X for mixed numbers (e.g: 2_1/2 is 2 and half)

## Allowed operators

The scripts run only for four operators:
- addition (+)
- subtraction (-)
- multiplication (*)
- division (/)

## Explaining the Approach

The code was solved in two main steps:
- First the Naive approach to come up with a solution
- Second, optimizing and fixing the Naive solution for an optimal one

<br/>

### Naive Solution

The idea was to use a python built-in method (eval()). The solution worked but the final fraction was not the simplist fraction. Therefore, the naive solution had to be changed

### The Final Solution

The final solution was designed to use an elementry school technique of dealing with mixed numbers and fractions:
- First, we convert the mixed number into a fraction
- Secont, we perform our desired operations

<img src='https://i0.wp.com/www.cbsetuts.com/wp-content/uploads/2013/09/Equivalent-Fractions-fig7.png?fit=245%2C210&ssl=1'/>

source = www.cbsetuts.com

if the operation is addition or subtraction:
- Find the Least Common Multiple (LCM)
- Change both denominators to be LCM
- Balance numerators with the exact multiple

if the operation is multiplication:
- Straight forward multiply numerators together and denominators together

if the operation is division:
- flip the right term and multiply


## Limitations and Future Enhancement

The script only performs one operation currently. I added a file called 'multipleOperations.py' that has a naive approach to performing more than one operation. Here is a small walk throug:

- First, we get a clean operation. By clean, I mean only a single space between every term.
- Then, look for operators with higher priority and take the terms in the righ and the left of them. Call the challenge method as it can solve them without repeating the code.
- Replace the old clean operation with an updated one
- keep doing that until we have an answer

## Skills gained from the challenge

While solving this challenge, I found myself writing more try and except code blocks to handle errors without freezing the program. By far, this is the most I have used error handling. 
