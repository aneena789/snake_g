class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def average(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("the average is ",sum/3)

    @staticmethod
    def hello():
        print("hello")


s1=Student("harsh",[98,97,98])
s1.average()
s1.hello()