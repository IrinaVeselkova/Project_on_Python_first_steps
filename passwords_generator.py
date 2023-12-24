import random

def generate_password(len_password,char_password):
    s=''
    for _ in range(len_password):
        s=s+random.choice(char_password) 
    return s

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
chars=''
print('Добро пожаловать в программу для генерирования надежных паролей!')
print('-'*40)
count_pass = int(input('Введите количество паролей, которые необходимо создать: => '))
len_pass = int(input('Какой длины должен быть пароль? => '))
if input('Включать ли цифры в пароль?(да/нет)=> ').lower() in ['да','yes','y','д']:
    chars+=digits
if input('Включать ли прописные буквы в пароль?(да/нет)=> ').lower() in ['да','yes','y','д']:
    chars+=lowercase_letters
if input('Включать ли строчные буквы в пароль?(да/нет)=> ').lower() in ['да','yes','y','д']:
    chars+=uppercase_letters
if input('Включать ли символы в пароль?(да/нет)=> ').lower() in ['да','yes','y','д']:
    chars+=punctuation
if input('Исключать ли неоднозначные символы, такие как: il1Lo0O?(да/нет)=> ').lower() in ['да','yes','y','д']:
    for symbol in 'il1Lo0O':
        if symbol in chars: 
            chars = chars.replace(symbol,'')
            
print('-'*40)

for i in range(count_pass):
    
    print(f'Пароль №{i+1} => {generate_password(len_pass,chars)}')
    print('-'*40)

