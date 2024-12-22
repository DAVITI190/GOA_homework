# Email
Email = input("Enter your Email:")

if Email == "****@**.***":
    print("great!")

while Email == "":
    print("you did not write it")
    Email = input("Enter your Email:")

# Password
Password = input("Enter your Password:")

while Password == "":
    print("you did not write it")
    Password = input("Enter your Password:")

# Enter your age
age = int(input("Enter your age: "))

if age >= 18:
    print("great!")

while age < 0:
    print("you havent been born yet!")
    age = input("Enter your age:")

else:
    print("you must be 18 years old !")
    age = input("Enter your age:")

# Enter Goa is beast!
x = input("Enter Goa is beast!:")

while x == "":
    print("you did not write it")
    x = input("Enter Goa is beast!:")

if x == "Goa is beast!":
    print("great! you are now signed up!")

else:
    print("you entered this wrong")