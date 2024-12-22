
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

number = int(input("შეიყვანეთ რიცხვი: "))

if 0 <= number < len(my_list):
    print(my_list[number])
elif -len(my_list) <= number < 0:
    print(, my_list[number])
else:
    print("არასწორი ინდექსი.")





# მოცემული სია
list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# სიის გადავლა და ელემენტების დამუშავება
for element in list1:
    multiplied = element * 2
    divided = element / 2
    print(f"ელემენტი {element} გამრავლებული 2-ზე: {multiplied}, გაყოფილი 2-ზე: {divided}")