import os
import sys

#primes.f95 is the file where your fortran functions and subroutines are stored
#then it is being converted in to a python module called "primes" which is followed by "-m" flag below
#once the function is compile, we can import it afterwards
os.system("python -m numpy.f2py -c primes.f95 -m primes")
#you can compile as many fortran scripts you want
print('Fortran file compiled, now beginning import')
import primes

if len(sys.argv)==3:
    #this portion is used if you are giving input from terminal
    num1=sys.argv[1]
    num2=sys.argv[2]
else:
    #this portion is used if you are giving values here itself
    num1=10
    num2=12
print("imported the compiled function")
print('here are the results')
print('-----------------------------------')
print(primes.sum2nums(num1,num2))