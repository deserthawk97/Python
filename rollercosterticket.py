def ticket(n):
    if n > 120:
        print("Can ride the coster")
        age = int(input("Enter the age in CM \n"))
        if age > 18:
            print("The ticket price is $12")
        else:
            print("The ticket price is $7")
    else:
        print("Cannot ride roller")

height=int(input("Enter the height in CM \n"))

ticket(height)
