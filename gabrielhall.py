#Functions Reuse Exercise
#Write a function named "rect_area" that computes the area of a rectangle. This function will take 2 parameters - length and width.
#Write a second function named "rect_surface_area" that calls the first function - "rect_area" - to
#compute the surface area of a rectangular solid.  This function will take three parameters - length, width and height.
#The main program will call the "rect_surface_area" with three parameters length, width and height.
#the user input to the program will be three integers - length, width and height of a rectangular solid.
#The program will print the length, width and height as input and the surface area of the entire rectangular solid.

# CS 16X Git Assignment

# Project requires TWO functions:
# 1. rect_area (length, width) which will return the area of a rectangle
# 2. rect_solid_area (length, width, height) which will return the area of a solid rectangular object

# The following four lines are just there to make the code work without errors until functions are added

def rect_area(length, width):
    return length * width

def rect_solid_area(length, width, height):
    return 2 * (rect_area(length,width)+rect_area(width,height)+rect_area(length,height))


# Request the dimension of a solid rectangular object
length = int(input("Enter the length of the the object as in integer: "))
width = int(input("Enter the width of the the object as in integer: "))
height = int(input("Enter the height of the the object as in integer: "))

shape_area = rect_area(length, width)
surface_area = rect_solid_area(length, width, height)

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", surface_area)
print("Shape Area = ", shape_area)