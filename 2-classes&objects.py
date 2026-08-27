
class person:
    name = "shohel"
    age = 19   
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# a= person()
# b= person()
# c= person()
# a.name = "shakil"
# a.age = 20
# # print(a.name,a.age)
# b.name = "shakl"
# b.age = 10
# a.info()
# b.info()
# c.info()

#__init__ is a constructor in python which is used to initialize the object of a class. It is called automatically when an object of a class is created. It is used to initialize the attributes of the class.
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

a= person("shakil",20)
b= person("shakl",10)
c= person("sakil",15)

a.info()
b.info()
c.info()