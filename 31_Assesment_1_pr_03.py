import random
count=0
random_number = random.randint(1, 100)
a=(random_number)
print(a)

while True:
    b=int(input("please guess a number."))
    count+=1
    if(b>99 or b<1):
        print("Your guess is out of range.")
    elif (b+15<=a):
        print("Your guess is too low.")
    elif (b-15>=a):
        print("Your guess is too high.")
    
    else:
        print("you are near, try again.")

    if (b==a):
        print("Congratulations! You guessed correct.")
        print("You guessed in", count, "attempts.")
        break