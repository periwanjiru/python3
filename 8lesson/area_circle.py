import math
def area_circle(radius):
    radius = int(radius)
    area = math.pi * radius * radius
    return  area
user_radius =input("what is the radius of the the circle?:")
calculated_area = area_circle(user_radius)
print("The area of the circle with radius {} is {}".format(user_radius,calculated_area))

    
