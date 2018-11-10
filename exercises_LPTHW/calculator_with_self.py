class calculator:
    a = 100
    b = 200
    def add(self,a, b):
        self.a = a
        self.b = b

        print("--------- INSIDE CLASS ---------")
        print(" ***** LOCAL VARIABLe****** \na is {} \nb is {}".format(a, b))
        print(" ***** GLOBAL VARIABLe****** \nself.a is {} \nself.b is {}".format(self.a, self.b))

        return self.a + self.b;


# calling class without creating the instance.
c1 = calculator()
c2 = calculator()

print(" ***** OUTSIDE CLASS ****** \nself.a is {} \nself.b is {}".format(c1.a, c1.b))

print("After adding: ", c1.add(13, 20))

print("--------c2--------")

print(" ***** OUTSIDE CLASS ****** \nself.a is {} \nself.b is {}".format(c2.a, c2.b))

print("After adding: ", c2.add(1000, 2000))


