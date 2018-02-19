factorial = 1
x = input ("Enter a positive integer: ")
for x in range (x, 1, -1):
    factorial = x * factorial
print "The factorial of",x,"is",factorial,"."
