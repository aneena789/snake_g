class Car:
    def __init__(self,type):
        self.type=type

    def start(self):
        print("car started")

    def stop(self):
        print("car stopped")


class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)

c1=ToyotaCar("prius","electric")
print(c1.type)
