# სწორი მომხმარებლის სახელი და პაროლი
correct_username = "admin"
correct_password = "my_secret_password"

# მომხმარებლის შეყვანა
user_username = input("შეიყვანეთ თქვენი სახელი: ")
user_password = input("შეიყვანეთ თქვენი პაროლი: ")

# სანამ შეყვანილი მომხმარებლის სახელი და პაროლი არ იქნება სწორი
while user_username != correct_username or user_password != correct_password:
    print("სახელი ან პაროლი არასწორია, სცადეთ ისევ.")
    user_username = input("შეიყვანეთ თქვენი სახელი: ")
    user_password = input("შეიყვანეთ თქვენი პაროლი: ")

# სწორად შეყვანილი მომხმარებლის სახელი და პაროლი
print("სწორი სახელი და პაროლი შეიყვანეთ!"