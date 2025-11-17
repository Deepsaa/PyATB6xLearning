#Write aprogram to take a user age and
#Let him know he can go to the club
#21
#Logic Building Formula
#Step-1
#Input:age,int and output-string(can go to club or not)
#Step-2
#Rough Logic(Brute force)
"""
age>21 -> print can go
age<21 -> print can not go
"""
age = int(input("Enter age:\n "))
if age > 21:
    print("Yes you can go to the club")
else:
    print("No, you can't go to the club")