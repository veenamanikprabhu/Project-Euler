#!/usr/bin/python

print "Summing 1 to 1000";
#Learning: Newline is printed at the end of each print statement
sum = 0;
for i in range (1, 1000, 1):
#Learning: Range excludes the last number, here it excludes 1000	
	print i		
	sum = sum + i
	
# New Block
print "Sum is ", sum

