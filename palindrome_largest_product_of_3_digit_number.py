#Problem 4:
#
# A palindromic number reads the same both ways. 
#Largest palindrome which is product of 
# two 2-digit numbers is 9009 = 91   99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(num):
        s = str(num)
        s_reverse = s[::-1]
        if s == s_reverse:
            return True
            
##   this gives me 906609  =  993 X 913            
#for a in range(999, 900,  -1):
#    for b in range(999, 900,  -1):
#        product = a*b
#        #print product, " = ",  a, "X", b
#       # print product
#        if isPalindrome(product) == True:
#            print "found", product, " = ",  a, "X", b
#            exit
            
#   this does not gives me 906609  =  993 X 913, Why     
# It gives   found 580085  =  995 X 583 ...


print("Prints palindrome no. which is product of 2 numbers ")
max_digit = int(input("Please enter how many digits should each number have?"))

max = 10**max_digit - 1
max_a = 0
max_b = 0
print max

#for a in range(999,100, -1):
#  for b in range(999,100,-1):

for a in range(max, 900,  -1):
    for b in range(max,900,  -1):
#        if (b == 913):
#            print "b = ",  b, "a = ", a
#        else:
#            continue    
	product = a*b
       #print product, " = ",  a, "X", b
       # print product
        if isPalindrome(product) == True:
            if product > max:
               # print "found", product, " = ",  a, "X", b
                max = product
                max_a = a
                max_b = b
                exit
            
print max_a, " *", max_b,"=", max
