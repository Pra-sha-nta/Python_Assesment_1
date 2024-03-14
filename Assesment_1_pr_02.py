# 33_Assesment_1_pr_02
a = int(input("Enter marks in 1st subject: "))
b = int(input("Enter marks in 2nd subject: "))
c = int(input("Enter marks in 3rd subject: "))
d = int(input("Enter marks in 4th subject: "))


if a < 40 or b < 40 or c < 40 or d < 40:
    print("Sorry! You failed. Better luck next time")
else:
    percentage = ((a + b + c + d) / 400) * 100

    if percentage >= 80:
        print("Awesome! You scored grade A+")
    elif percentage >= 70:
        print("Good. You scored grade A")
    elif percentage >= 60:
        print("You scored grade A-") 
    elif percentage >= 50:
        print("You scored grade B")
    elif percentage >= 40:
        print("You scored grade B-")
    else:
        print("Sorry! You failed. Better luck next time")
