#Assesment_1_pr_01
a=int(input("Enter First Number "))
b=int(input("Enter Second Number "))
c=int(input('''Enter Choice:
            1.Add
            2.Sub
            3.Mul
            4.Div\n'''))
if c==1:
    print("Sum of", a ,"and", b ,"is", a+b)
elif c==2:
    print("Difference of",a,"and",b,"is",a-b)
elif c==3:
    print("Product of",a,"and",b, "is",a*b)
elif c==4:
    print("Quotient of",a,"and",b,"is",a/b)
else:
    print("Invalid Choice")

