# Polynomial Root Finder

A WIP simple polynomial real root finder using Strum's Theorem and Newton's Algorithm.


# Currently Implemented

## polyTools
> A bunch of tools used to do polynomial arithmatic operations including multiplication, addition, subrtraction, and division remainders (Quotients are unused so not implemented), as well as other tools used to trim, padd, and find the derivative of a polynomial.

# Helper Functions

#### toSuperscript:
> Turns problematic syntax like:
> 1x^4-1x^2-12x+4
> Into beautiful text like:
> 1x⁴ - 1x² - 0.3333333333333333x + 4


#### printHelper:
> Debug tool used to proofread function outputs.


# WIP Functions

#### Strum's Algorithm
> Finds the number of real roots a polynomial has using polyDivide and derive.
#### Slicer
> Finds the interval every real root is in using Strum's Algorithm.
#### Newton's Algorithm
> Using guesses in Slicer's intervals, finds all real roots of a polynomial.