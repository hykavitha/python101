import sys
pgm = sys.argv[0]
print("The first argument by default is : ", pgm)
arguments = sys.argv[1:]
count = len(arguments)
print("The length of sys args is {} ".format(count))
arguments [0] = int(arguments[0])
print(type(arguments[0]))
