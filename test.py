# #format print
# print(f"Hello World %d%d" % (5,5))

# x = 1
# z = 1.0
# y = "string"
# x = True
# print(str(x) + y)
# print(x/z) #implicit casting
def fun(a):
    print(a)

x = [] #list
x = list()
x = [1,2,3]
x.append(4)
x += [5]
# x.insert(0,6)
# fun(len(x))
# i = 0
# while i < len(x):
#     print(x[i])
#     i+=1
#ORM object relational model
# for i in range(1,len(x),2):
#     print(x[i])

x = dict()
x = {}
x = {
    "key":"value",
    "key2":1,
    "key3":True
}
x["key4"]=[1,2,3]
x[1]={}
x[1][fun]="x" #legal python code
# x.setdefault("key5","new")
# x.setdefault("key5","awesome")
# for word in somelist:
#     count = x.get(word,0)
#     count+=1
#     x[word]=count
# x["key3"](x["key2"])

y = (1,2,3,4,5,6) #tuples
# z = (1,2,3,4,5,6)
x[y]= "awesome"
# fun(y+z)
# x = -1
# if x > 5:
#     print("bob")
# elif x < 0:
#     print("alice")
# else:
#     print("False")
# try:
#     fun(y)
# except: #bad practice
#     print("something bad happened")
# finally:
#     print("I'm always happening")
    # print(e)

# We use the "class" operator to get a class
class Human:

    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    #class attribute
    age = 0

    def __init__(self, name):
        self.name = name

    def talk(self, msg):
        print(msg)
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    def about(self):
        print("%s is %d years old" % (self.name,self.age))

class Student(Human):

    def __init__(self, name, school):
        Human.__init__(self, name)
        self.school = school
    
    def about(self):
        print("%s is a student at %s and %d years old" % (
            self.name, 
            self.school, 
            self.age)
            )



x = Human("bob")
x.about()

y = Human("alice")
y.about()

z = Student("charles","chico state")
z.about()
