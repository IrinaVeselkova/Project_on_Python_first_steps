import random


def is_valid(number):
    if number.isdigit() and 1<=int(number)<=100:
        return True
    else:
        return False


num = random.randint(1, 100)
print("-" * 40)
print("Добро пожаловать в числовую угадайку")
print("-" * 40)

number = input("Введите число от 1 до 100: ")

while is_valid(number) != True:
    number = input("А может быть все-таки введем целое число от 1 до 100? => ")


while is_valid(number) == True:
    if int(number) < num :
        number = input("Ваше число меньше загаданного, попробуйте еще разок => ")
        while is_valid(number) != True:
            number = input("А может быть все-таки введем целое число от 1 до 100? => ")
    elif int(number) > num :
        number = input("Ваше число больше загаданного, попробуйте еще разок => ")
        while is_valid(number) != True:
            number = input("А может быть все-таки введем целое число от 1 до 100? => ")
    elif int(number) == num: break
print("-" * 40)
print("Вы угадали, поздравляем!")
print("-" * 40)
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
print("-" * 40)
