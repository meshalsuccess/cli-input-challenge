"""
This is only called when there are more than one operator.

Procedure:
1- we need to know how many operations are there and that is figured out through operators.
2- remove all spaces and create a main string that has all terms in order to organize them and add space after each term in between.
3- look for operator, priority: *, /, -. +
4- break the main string into 3 parts: Str1 = [ : first char of priority operation], Str2 = [last char of priority operation + 1 : ], 
current = [first char of priority operation: last char of priority operation +1].

5- perform calculations on the current string and send it to challenge.
6- re-create the string with str1 + current answer + str 2.
7- This will have a bug that we can solve later, we need an end condition

"""