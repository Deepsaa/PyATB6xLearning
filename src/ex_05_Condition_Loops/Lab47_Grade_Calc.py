#Grade Calculator
#Write a program that calculate and display the letter grade
#For a given numerical score(Ex.a,b,c,d or f)
#Based on the following grade scale
#A:90-100
#B:80-89
#C:70-79
#D:60-69
#F:0-59
#Logic building formula
#1-> user input->score->int
#2->output->string->A,B

score = int(input("Enter the score: ").strip())
if score >100 or score<=-1:
    print("❌ You are a superman!,you cant get a grade")
else:
    if score >= 90 and score <= 100:
        print("Your grade is A")
    elif score >= 80 and score <= 90:
        print("Your grade is B")
    elif score >= 70 and score <= 80:
        print("Your grade is C")
    elif score >= 60 and score <= 70:
        print("Your grade is D")
    else:
        print("Your grade is F")