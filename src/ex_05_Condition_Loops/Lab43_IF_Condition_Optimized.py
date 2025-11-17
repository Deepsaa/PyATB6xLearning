# Write aprogram to take a user age and
# Let him know he can go to the club
# 21
# Logic Building Formula
# Step-1
# Input:age,int and output-string(can go to club or not)
# Step-2
# Rough Logic(Brute force)
"""
age>21 -> print can go
age<21 -> print can not go
"""
age = int(input("Enter age:\n ").strip()) #Strips is used to  extra remove space from input function
if age <= 0 or age > 130:
    print("Enter a valid age")
else:

 if age >= 21:
    print("Yes you can go to the club")
 else:
    print("No, you can't go to the club")

#Step-4
#check for the edge cases
#We should consider edge cases such as
#Negative age or extremely high value -> program will break
#Non-numeric Input -ABC
#Age which is valid>130
#Step5
#Optimize the code
#Handle all the edge




    
    

