import math
i = 0
print('================================')
print(' Welcome to the Area Calculator')
print('================================')
print('Enter the shape according to the number')
print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')

while True:
    s = int(input('Which Shape: '))

    if s == 1:
        h = int(input("What's the height:"))
        b = int(input("What's the base:"))
        A = (h * b) / 2
        print("The Area of the triangle is", A)
    elif s == 2:
        l = int(input("What's the length:"))
        w = int(input("What's the width:"))
        A = l * w
        print("The Area of the rectangle is", A)
    elif s == 3:
        l  = int(input("What is the length of one side: "))
        A = l ** 2
        print("The Area of the square is", A)
    elif s == 4:
        r = int(input("What is the radius of the circle: "))
        A = math.pi * (r ** 2)
        print("The Area of the circle is", A)

    elif s == 5:
        exit()
    else:
        print("Invalid option. Please enter a number between 1 and 5.")
        i += 1
        if i == 5:
            print("Dont waste my time")
            exit()


            


