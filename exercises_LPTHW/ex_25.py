


def main():
  fo = open("foo.txt", "wb")
  print "Name of the file: ", fo.name
  print "Closed or not : ", fo.closed
  print "Opening mode : ", fo.mode
  print "Softspace flag : ", fo.softspace


  # Open a file
  fo = open("foo.txt", "r+")
  str = fo.read(10);
  print "Read String is : ", str



  # Check current position
  position = fo.tell();
  print "Current file position : ", position

  # Reposition pointer at the beginning once again
  position = fo.seek(0, 0);
  str = fo.read(10);
  print "Again read String is : ", str
  # Close opend file
  fo.close()

    
if __name__== "__main__":
  main()
