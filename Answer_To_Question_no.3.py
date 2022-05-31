class A(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "Name: " + str(self.name)

class B(A):
    def __init__(self,name,age):
        A.__init__(self,name)
        self.age = age
    def __str__(self):
        return "Age: " + str(self.age)+ ", " + A.__str__(self)

b1 = B("Bench",19)
print(b1.__str__())
