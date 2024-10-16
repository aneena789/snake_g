class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary


    def showDetails(self):
        print(self.role)
        print(self.department)
        print(self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","electronics",75000)

e1=Employee("supervisor","hr",20000)
e1.showDetails()

e2=Engineer()
e2.showDetails()