import sys

pgm_name = sys.argv[0]
print(pgm_name)

arguments = sys.argv[1:]
count = len(arguments)
print(arguments)

num = int(sys.argv[1]) 

if num > 0:
	print("positive")
elif  num < 0 : 
	print("negative")
else:
	print("00000")
 
