#multi-level inheritance
class Car:
    name = "Anonymous"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped")

class Toyotacar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(Toyotacar):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type


car1 = Fortuner("diesel")
car1.start()

#multiple inheritance
class A:
    varA = "welcome to the school"

class B:
    varB = "welcome to college"

class C(A, B):
    varC = "welcome to university"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)