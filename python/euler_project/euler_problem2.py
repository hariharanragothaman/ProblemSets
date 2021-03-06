"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

# 3,5,8,13

first_term = 1
second_term = 2
third_term = 0

limit = 0
result = 2

while limit < 4000000:
    third_term = second_term + first_term

    if third_term % 2 == 0:
        result = result + third_term

    first_term = second_term
    second_term = third_term

    limit = third_term

print "The result is:", result
