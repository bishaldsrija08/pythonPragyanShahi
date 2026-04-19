# WAP to calcualte araa of rectangle, circle, square, trianlge
"""
Hint: 
1. Area of rectangle = length * breadth
2. Area of circle = 3.14 * radius * radius
3. Area of square = side * side
4. Area of triangle = 0.5 * base * height
"""

# Your job is to calculate the area of the shape based on user input. You can use if-else statements to determine which shape the user wants to calculate the area for, and then prompt them for the necessary dimensions. Finally, you can print out the calculated area to the user.

shape = input("Enter the shape (rectangle, circle, square, triangle): ")

if shape == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    area = length * breadth
    print(f"The area of the rectangle is: {area}")
elif shape == "circle":
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * radius * radius
    print(f"The area of the circle is: {area}")
elif shape == "square":
    side = float(input("Enter the side length of the square: "))
    area = side * side
    print(f"The area of the square is: {area}")
    
elif shape == "triangle":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")
    
else:
    print("Invalid shape entered. Please enter rectangle, circle, square, or triangle.")