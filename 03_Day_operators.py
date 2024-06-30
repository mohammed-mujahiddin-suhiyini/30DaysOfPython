age = 22
height = 5.24
complex_number = 1+1j
#Area of triangle
base = print(int(input("Please enter a base of your choice:")))
height = print(int(input("Please enter a height of your choice:")))
area = 0.5 * base * height
print("The area of the triangle is ",area)
#perimeter of triangle
side_a = int(input("Enter the length of side A:> "))
side_b = int(input("Enter the length of side B:> "))
side_c = int(input("Enter the length of side C:> "))
print("The perimeter of the triangle is ", side_a+ side_b + side_c)
#Area and Perimeter of rectangle
length = int(input("What is the length of the rectangle? "))
width = int(input("What is the width of the rectangle? "))
print("The area of the rectangle is ",length * width)
print("The perimeter of the rectangle is ",2 *(length*width))
#Area and Circumference of a circle
radius = int(input("What is the radius of the circle? "))
from math import *
print("The area of this circle is",pi*(radius**2))
print("The circumference of this circle is",pi*2*radius) 
#slope,x-intercept and y intercept of y=2x-2