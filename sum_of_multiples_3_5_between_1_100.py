#!/usr/bin/python

print "Summing multiples of 3 and 5 from 1 to 100";
#Learning: Newline is printed at the end of each print statement
sum = 0;
for i in range (1, 100, 1):
#Learning: Range excludes the last number, here it excludes 1000	
#	print i
#	if ( ! ( i % 3) | !(i%5))  # Doesn't work
#	| is OR
	if ( (i % 3 == 0 ) | ( i % 5 == 0) ):
		print "adding", i, "to ", sum, "becomes"
		sum = sum + i
		print sum


# New Block
print "Sum is ", sum
