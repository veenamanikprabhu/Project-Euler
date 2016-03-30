# Find difference between sum of squares of first 100 numbers and the square of
# their sum

print "Python sript to show the difference of \
	Sum of squares of first 100 numbers \
	square of sum of first 100 numbers"


print "\n*********Sum of Squares**********"
sum = 0
limit = int(raw_input("Plz enter the limit:"))

for i in range(1,limit+1,1):
	print "Square of ",i, " = ",  (i*i) 
	sum = sum + (i * i)
	print "sum of squares till",i," is ", sum
print "Sum of Square numbers from 1 to ", limit," = ", sum
sum
print "\n*********Square of sums....********"

sum = limit*(limit+1)/2
print "Sum of numbers from 1 to ",limit," = ", sum


square_of_sum = (limit*(limit+1)/2)**2
print "Square of Sum from 1 to ", limit," = ",square_of_sum
diff =  square_of_sum - sum
print "difference of Square of Sum  and Sum of Square numbers = ", diff
