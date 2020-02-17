class rectangle():
    def __init__(self,length,breadth,price):
        self.length=length
        self.breadth=breadth
        self.price=price
    def perimeter(self):
        return 2*(self.length + self.breadth)
    def area(self):
        return self.length*self.breadth
    def totcost(self):
        return self.area()*self.price
x=int(input("enter the length: "))
y=int(input("enter the breadth: "))
z=int(input("enter the price per sqm:"))
a=rectangle(x,y,z)
peri=a.perimeter()
area=a.area()
cost=a.totcost()
print("perimeter of rectangle: ",peri)
print("area of rectangle: ",area)
print("total cost for rectangle: ",cost)
