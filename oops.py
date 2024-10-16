class Student:
    college_name="college of engineering,trivandrum"
    def __init__(self,name,marks):
        self.name=name#obj attr>class attr
        self.marks=marks
        print("adding new student in database...")

    def hello(self):
        print("welcome student")

    def get_marks(self):
        print(self.name,"=",self.marks)



s1=Student("sanjesh",98)
print(s1.name,s1.marks)#name is an attribute
print(s1.college_name)
s1.hello()
s1.get_marks()



 