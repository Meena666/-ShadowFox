def pond_area(radius):
    pi = 3.14
    return pi*(radius**2)
def water_in_pond(area,water_per_sqmt):
    return area*water_per_sqmt
radius = 84
area = pond_area(radius)
water_per_sqmt = 1.4
total_water = water_in_pond(area,water_per_sqmt)
print("Area of the pond:",(area))
print("Total amount of water in the pond:",int(total_water))
