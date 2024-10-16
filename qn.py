class Circle:
    def __init__(self,r):
        self.r=r

    def Area(self):
        print("area is ",3.14*self.r*self.r)

    def Perimeter(self):
        print("perimeter is ",2*3.14*self.r)

c1=Circle(5)
c1.Area()
c1.Perimeter()