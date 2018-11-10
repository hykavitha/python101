class calculator:

    a = 100 # 1
    b = 200 # 2

    def __init__(self, a, b):
        print(" ***** BEFORE INIT ****** \nself.a is {} \nself.b is {}".format(self.a, self.b))

        self.a = a
        self.b = b
        print(" ***** AFTER INIT ****** \nself.a is {} \nself.b is {}".format(self.a, self.b))


    def add(self):
        print("--------- INSIDE ADD ---------")
        print(" ***** GLOBAL VARIABLe****** \nself.a is {} \nself.b is {}".format(self.a, self.b))

        return self.a + self.b;


# calling class without creating the instance.
c1 = calculator(1,2)
c2 = calculator(10, 20)

print(" ***** OUTSIDE CLASS ****** \nself.a is {} \nself.b is {}".format(c1.a, c1.b))

print("After adding: ", c1.add())

print("--------c2--------")

print(" ***** OUTSIDE CLASS ****** \nself.a is {} \nself.b is {}".format(c2.a, c2.b))

print("After adding: ", c2.add())


