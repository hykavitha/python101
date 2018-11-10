class FileOperations:
    fo = None
    filename = None
    # all the data
    input_lines = []

    unique_users =[ ]
    unique_movies =[ ]
    ratings_analysis =[ ]



    def __init__(self, filename):
        self.filename = filename
        print("filename is : " ,self.filename)
        self.fo= None


    def openFile(self):
        # Open a file
        self.fo = open(self.filename, "r")
        # print ("Name of the file: ", self.fo.name)

    def closeFile(self):
        return self.fo.close()


    def read(self):
        """read function reads data into a string"""
        v = self.fo.read()
        print(type(v))
        print("read function reads data into a string")

    def read_10(self):
        v = self.fo.read(10)
        print(type(v))
        print(len(v))
        print("read function reads data into a string")

    def  get_input_list(self):
        line = self.fo.readline()
        while(line):
            # print("appending this line : " , line)
            line = line.split("\t")
            self.input_lines.append(line)
            line = self.fo.readline()

        print(len(self.input_lines))
        print(self.input_lines [0])

        #movie id
        print(self.input_lines[0][0])

        #user id
        print(self.input_lines[0][1])

        #ratings
        print(self.input_lines[0][2])

        #timestamp
        print(self.input_lines[0][3])


    def get_local_time(self, ts):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))


    # def get_uniq_users(self):
    #     ##todo build the list
    #     for loop on input_list
    #     return self.uniq_users

    # def get_unique_users(self):

class_obj  = FileOperations("/Users/KaviAnu/python101_kavi/u_data_100.txt")

# class_obj.openFile()
# class_obj.read()
# class_obj.closeFile()
#
#
# class_obj.openFile()
# class_obj.read_10()
# class_obj.closeFile()


class_obj.openFile()
class_obj.get_input_list()
class_obj.closeFile()
