import math

radius = 15 

for y in range(-radius, radius + 1):
    for x in range(-2 * radius, 2 * radius + 1):
        dist = math.sqrt((x / 2)*2 + y*2)
        angle = math.atan2(y, x)

        
        if abs(dist - radius) < 1.5 + 0.8 * math.cos(6 * angle):
            print("*", end="")
        else:
            print(" ", end="")


