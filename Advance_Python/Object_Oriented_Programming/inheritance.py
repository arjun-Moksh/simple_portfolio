# class BaseClass:
#     x = 5
#     y = 10
#     def my_method(self):
#         print("Hello World from BaseClass")`

#     def my_method_2(self, num):
#         print(num)

# class DerivedClass(BaseClass):
#     z = 15
#     def my_method(self):
#         print("Hello World from DerivedClass")
#     def my_method_3(self):
#         print("Hello World from DerivedClass")

# obj1 = BaseClass()
# obj1.my_method()
# obj1.my_method_2(100)

# obj2 = DerivedClass()
# obj2.my_method()
# obj2.my_method_2(700)









class quadriLateral:
    def __init__(self, a, b, c, d): #obj1,10,20,30,40
        self.side1=a  #self.side1=10  #=>obj1.side1=10
        self.side2=b
        self.side3=c
        self.side4=d
    # def init(self,a,b,c,d):
    #     self.side1=a  #self.side1=10  #=>obj1.side1=10
    #     self.side2=b
    #     self.side3=c
    #     self.side4=d

    def perimeter(self):
        p=self.side1 + self.side2 + self.side3 + self.side4
        print("perimeter=",p)

# obj1 = quadriLateral()
# obj1.init(10,20,30,40)
# obj1.perimeter()


obj1 = quadriLateral(10,20,30,40) #=>quadriLateral.__init__(obj1, 10,20,30,40)
obj1.perimeter()
class rectangle(quadriLateral):
    def __init__(self, a, b):
        super().__init__(a, b, a, b)
        #quadriLateral.__init__(self,a,b,a,b)

    def area(self):
        a=self.side1 * self.side2
        print("area=",a)

r1 = rectangle(10,20)
r1.perimeter()
r1.area()
class square(quadriLateral):
    def __init__(self, a):
        super().__init__(a, a, a, a)
        #quadriLateral.__init__(self,a,a,a,a)

    def area(self):
        a=self.side1 ** 2
        print("area=",a)

# r1=rectangle(10, 20)
# r1.perimeter()
# r1.area()

s1=square(10)
s1.perimeter()
s1.area()
