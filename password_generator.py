import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print ("Welcome to password generator")
letter = int(input("Enter how many letters you need in password "))
number = int(input("Enter how many number you need in password "))
symbol = int(input("Enter how many character you need in password "))

passwd = []   #password list
password = ""  #password string
for char in range(0,letter):
    passwd.append(random.choice(letters))
for char in range(0,number):
    passwd.append(random.choice(numbers))
for char in range(0,symbol):
    passwd.append(random.choice(symbols))
random.shuffle(passwd)                    #shuffles the password it is a random function
for i in passwd:
    password = password + i
print(f"Your password is : {password}")









