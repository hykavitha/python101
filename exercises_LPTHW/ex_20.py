
True and True
1 == 1 and 2 == 2

x = True
y = False

# Output: x and y is False
print('x and y is',x and y)

# Output: x or y is True
print('x or y is',x or y)

# Output: not x is False
print('not x is',not x)

Membership operators

a = True
b = False
print(('a and b is',a and b))
print(('a or b is',a or b))
print(('not a is',not a))

x = 4
y = 8
list = [1, 2, 3, 4, 5 ];
if ( x in list ):
   print("Line 1 - x is available in the given list")
else:
   print("Line 1 - x is not available in the given list")
if ( y not in list ):
   print("Line 2 - y is not available in the given list")
else:
   print("Line 2 - y is available in the given list")
   


Operators Summary:
#Arithmetic Operators
x= 4	
y= 5
print x + y

#Comparison Operators
x = 4
y = 5
print('x > y  is',x>y)

#Assignment Operators
num1 = 4
num2 = 5
print ("Line 1 - Value of num1 : ", num1)
print ("Line 2 - Value of num2 : ", num2)

#compound assignment operator
num1 = 4
num2 = 5
res = num1 + num2
res += num1
print ("Line 1 - Result of + is ", res)

#Logical Operators
a = True
b = False
print('a and b is',a and b)
print('a or b is',a or b)
print('not a is',not a)

#Membership Operators
x = 4
y = 8
list = [1, 2, 3, 4, 5 ];
if ( x in list ):
   print "Line 1 - x is available in the given list"
else:
   print "Line 1 - x is not available in the given list"
if ( y not in list ):
   print "Line 2 - y is not available in the given list"
else:
   print "Line 2 - y is available in the given list"

#Identity Operators
x = 20
y = 20
if ( x is y ):
	print "x & y  SAME identity"
y=30
if ( x is not y ):
	print "x & y have DIFFERENT identity"

#Operator precedence
v = 4
w = 5
x = 8
y = 2
z = 0
z = (v+w) * x / y;   
print "Value of (v+w) * x/ y is ",  z
