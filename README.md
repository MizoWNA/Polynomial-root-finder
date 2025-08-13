# Polynomial Root Finder

A (Finally finished!) simple polynomial real root finder using Strum's Theorem, Bisection method, and Newton's Algorithm. First real python project, go easy!

# Why these methods?
Simply because they seemed the easiest and most fun to work with!
I couldve just used the bisection method and called it a day, but that didnt seem good enough to me, so i decided to also combie it with newton's method for better accuracy (and also more fun!)


# Currently Implemented

## polyTools
> A bunch of tools used to do polynomial arithmatic operations including multiplication, addition, subrtraction, and division remainders (Quotients are unused so not implemented), as well as other tools used to trim, padd, and find the derivative of a polynomial.

## Strum's Algorithm
> Finds the number of real roots a polynomial has using polyDivide and derive.
## Bisection
> Finds the interval every real root is in using Strum's Algorithm.
## Newton's Algorithm
> Using guesses in Bisection's intervals, finds all real roots of a polynomial.



# WIP
> Finally nothing left!
> Well, thats a lie. I'm hoping to improve this by also adding in a way to find the multiplicty of a root, as well as finding complex roots.

# Usage
Its stupidly simple, just run your polynomial, formatted like so:
> [coefeccient1, coeffecient2, coeffecient3, ...., constant]
> 
So a polynomial like this
> 3x^3 - 5x^2 + 4
>
would input like so:
> [3, -5, 0 ,4]
>
From there, just input that into the **newtonsMethod()** function in rootFinder.py along with a maximum iteration limit as its second argument.