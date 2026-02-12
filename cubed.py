class Apple:
    def __init__(self,c,s,t,w):
        self.color=c
        self.size=s
        self.tall=t
        self.weight=w
    def quality(self):
        return self.size*self.tall*self.weight

a=Apple('red',10,20,300)
q=a.quality()
print(q)

import math as m
class Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*m.pi

c=Circle(5)
print(c.area())

class Triangle:
    def __init__(self,bottom,hight):
        self.bottom=bottom
        self.hight=hight
    def area(self):
        return self.bottom*self.hight/2

triangle1=Triangle(3,6)
print(triangle1.area())

class Hexagon:
    def __init__(self,p):
        self.perimeter=p
    def calculate_perimeter(self):
        return self.perimeter*6

h1=Hexagon(5)
print(h1.calculate_perimeter())
