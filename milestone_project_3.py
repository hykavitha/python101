import sys

def read_lines_for(file_obj):
	lines = file_obj.read()
	i = 0
	for line in lines:
		print(type(line))
		print (line)
		#if i ==10:
		#	break

def main(path):
	fo = open(path, 'r')
	read_lines_for(fo)

	
if __name__ =='__main__':
	arg_len = len(sys.argv [1:])
	print(arg_len)
	if (arg_len <1):
		print("ERROR\t:exitting...... arguments passed")
		sys.exit()
	print("calling main function")
	main(sys.argv[1])
