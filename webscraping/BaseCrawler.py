class BaseCrawler:

    def __init__(self):
        pass

    def fetch(self):
        #this does fetching
        print("fetch")

    def printToFile(self, file_name, data):
        '''this print to a file passed as the object'''

        with open(file_name, 'wb') as f:
            f.write(data.body)
        print("writing into a file")