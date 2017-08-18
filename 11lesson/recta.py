class Recta():
    def __init__(self,base,height):
        self.base=int(base)
        self.height = int(height)
        
    def area(self):
        return self.height * self.base
    def perimeter(self):
        return 2 * (self.height + self.base)
        
base = input("What is the base of your rectangle?:")
height = input ("What is the height of your recta?:")
recta = Recta(base,height)
print("The area of the recta is {} and its perimeter {}".format(recta.area(),recta.perimeter()))