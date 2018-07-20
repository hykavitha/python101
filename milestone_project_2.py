import sys

movie_ids = []
uids= []

def read_bytes(file_obj):
	str = file_obj.read(10)
	print ("Read String is : ", str)


def read_lines(file_obj):
	lines = file_obj.readlines()
	print(type(lines))
	
def read_lines_for(file_obj):
	lines = file_obj.readlines()
	i = 0
	for line in lines:
		print(type(line))
		print (line)
		words = line.split("\t")
		print(words)
		words [3] = words[3].replace("\n", '')
		print(words)
		uids.append (words[0])
		i += 1
		if i ==10:
			break
		 

def process_data():
#todo, this processes each line and cleans

def convert_time_stamp():
	return datetime

def uniq_id_analysis():

	returns uid, mid



def ratings_analysis():
	return 

def top_ratings_movies ():



def main(path):
	fo = open(path, 'r')
	print(type(fo))
	#read_bytes(fo)
	#read_lines(fo)
	read_lines_for(fo)
	fo.close()



if __name__ == "__main__": 
	arg_len = len(sys.argv [1:])
	print(arg_len)
	if (arg_len <1):
		print("ERROR\t:exitting...... arguments passed")
		sys.exit()
	print("calling main function")
	main(sys.argv[1])	
