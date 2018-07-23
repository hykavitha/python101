import sys

user_list = []
movie_list= []

uniq_user_id = {}
uniq_movie_id = {}



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
		process_data(i)
		i += 1
		if i ==10:
			break
		 

def process_data(i):
#todo, this processes each line and cleans
	string_list = line.split("\t")
        string_list [3] = string_list[3].replace("\n", '')
        build_list(string_list, i)
	return 

def convert_time_stamp():
	return ''

def uniq_id_analysis():
	return uid, mid



def ratings_analysis():
	return 

def top_ratings_movies ():
	return


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
