def area_circle(radius):
    area = 3.142 * int(radius)**2
    return(area)
radius = input("what is the radius?:")
area = area_circle(radius)
print(area)