#	Find the Prime Factors of  600851475143
#	Prime factors of 13195 are 5,7,13, 29
#
#	Loop thru odd numbers until square root of 600851475143
#		check if the number is prime
#		if yes, check modulo division leads to 0
#		if no, continue

import math
#math.sqrt(x)

def is_prime(prime):
	n_max = int(math.sqrt(prime))
	n_max += 1
	for n in range(3, n_max, 2):
		if ( n_max % n == 0 ):
	            return 0
        	else:
            		continue
	return 1

number = 600851475143
number = 13195
n = 3
nmax = int(math.sqrt(number))
#print nmax

for n in range(3, nmax, 2):
    
#	If this number modulo divides the given number		
	if(   number % n == 0 ):    
#	If this number is a prime number
	       if (is_prime(n)):
			print n, " is a divisor of ", number



