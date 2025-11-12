#Write a program to calculate the
# area of a circle given its radius using the formula
#  area=pie*r^2    (Take pie as 3.14)

#i/p = r = float
#o/p= > string
# Logic building formula
# Step 1
# figure out the input and output first
# input->datatype-> r-> float
# pi=3.14
#power-> pow or ** -> any
#o/p= string-> float - area ,print area
#step2
#rough logic = area = 3.14 *(pow r,2)
#step 3
radius = float(input("Enter the radius of a circle\n "))
print(radius)
area = 3.14 *(pow(radius, 2))
print("area of the circle is_>" ,area)
#String data formating
print(f"Area of the circle {area}")
