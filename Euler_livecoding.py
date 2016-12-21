__author__ = 'kaihami'

"""
Euler Project:

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

import time

start_1 = time.time()

#brute force...

n = 1000

sum_1 = sum([i for i in xrange(0, 1000) if (i % 3 == 0 or i % 5 == 0)])

elapsed_1 = time.time() - start_1

print "Result: %s in %s seconds" % (sum_1, elapsed_1)

#RESULT: 233168, total time: 0.00086

#Using Sets:

start_2 = time.time()

sum3 = set(xrange(0, n, 3)) # all 3
sum5 = set(xrange(0, n, 5)) # all 5

sum_2 = sum(sum3.union(sum5))

elapsed_2 = time.time() - start_2

print "Sets: Result %s in %s seconds" % (sum_2, elapsed_2)

#RESULT: 233168, total time: 0.00096

#Using a more efficient approach.

#Since the sum of all numbers from 1 to n is (n * (n+1))/2.
#Sum of all numbers multiple of 3 is:
#(3 + 6 + ... + 999) then: 3 * (m * (m+1))/2
#and for all numbers multiple of 5... 5 * (m * (m+1)) /2
#Where m = (n-1)/k, which k is the number in our case 1, 3 or 5
#But if we sum all numbers multiple of 3 or 5 we will sum all multiples of 15.
# therefore we have to substract multiples of 15 from the sum of all 3 and all 5

def sum_factor(n, k):
    m = (n-1)//k #k is 3, 5 or 15
    return (k * m *(m+1))/2

start_3 = time.time()

sum_of_all_3 = sum_factor(n, 3)

sum_of_all_5 = sum_factor(n, 5)

sum_of_all_15 = sum_factor(n, 15)

sum_3 = sum_of_all_3 + sum_of_all_5 - sum_of_all_15

elapsed_3 = time.time() - start_3

print "Result %s in %s seconds" % (sum_3, elapsed_3)

#Same result but it was faster than the first and second method.

#We can test all 3 methods in Hacker rank!
