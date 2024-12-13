# სწორი პაროლი
correct_password = "my_secret_password"

# მომხმარებლის პაროლის შეყვანა
user_password = input("Enter your password: ")

# სანამ შეყვანილი პაროლი არ იქნება სწორი
while user_password != correct_password:
    print("Incorrect password, please try again.")
    user_password = input("Enter your password: ")

# სწორად შეყვანილი პაროლი
print("Correct password entered!"