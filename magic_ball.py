import random
import time

answers = [
    "Бесспорно",
    "Мне кажется - да",
    "Пока неясно, попробуй снова",
    "Даже не думай",
    "Предрешено",
    "Вероятнее всего",
    "Спроси позже",
    "Мой ответ - нет",
    "Никаких сомнений",
    "Хорошие перспективы",
    "Лучше не рассказывать",
    "По моим данным - нет",
    "Определённо да",
    "Знаки говорят - да",
    "Сейчас нельзя предсказать",
    "Перспективы не очень хорошие",
    "Можешь быть уверен в этом",
    "Да",
    "Сконцентрируйся и спроси опять",
    "Весьма сомнительно",
]
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос!')
print('-'*40)
name = input('Как тебя зовут? =>  ')
print('\nПривет,',name,'! Хочешь узнать ответ на свой воопрос? (жми любую клавишу  - если да и "н" - если нет)',sep='')
while input() not in ['n','н']:
    print('-'*40)
    input('Введите Ваш вопрос: ')
    print('-'*40)
    print('Сейчас я загляну в твоё будущее или прошлое, чтобы дать правильный ответ...', end='\n')
    time.sleep(4)
    print('-'*40)
    print(f'{name}, вот, что я Вам скажу....{random.choice(answers)}')
    print('-'*40)
    print(name,', хочешь узнать ответ еще на один воопрос? (жми любую клавишу  - если да и "н" - если нет)',sep='')

print('-'*40)
print('Возвращайся если возникнут вопросы!')
print('-'*40)
    
    
    
    
