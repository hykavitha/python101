class Student:  

   def __init__(self, rollno, name):
      self.rollno = rollno  
      self.name = name  
   def displayStudent(self):  
      print "rollno : ", self.rollno,  ", name: ", self.name  

emp1 = Student(121, "Ajeet")  
emp2 = Student(122, "Sonoo")  
emp1.displayStudent()  
emp2.displayStudent() 
