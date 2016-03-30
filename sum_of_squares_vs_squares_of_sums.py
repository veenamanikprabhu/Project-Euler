# Find difference between sum of squares of first 100 numbers and the square of
# their sum

print "Python script to show the difference of \
	Sum of squares of first 100 numbers \
	square of sum of first 100 numbers"

sum = 0
for i in range(1,10,1):
	print "Square of ",i, " = ",  (i*i) 
	sum = sum + (i * i)
	print "sum of squares till",i," is ", sum
sum_of_squares = sum
print sum


