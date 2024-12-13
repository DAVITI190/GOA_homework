# მომხმარებლის შეყვანა
number = int(input("შეიყვანეთ რიცხვი: "))

# ინიციალიზაცია
factorial = 1
count = number

# while ციკლი ფაქტორიალის დასათვლად
while count > 0:
    factorial *= count
    count -= 1

# შედეგის დაბეჭდვა
print(f"რიცხვი {number}-ის ფაქტორიალი არის {factorial}."