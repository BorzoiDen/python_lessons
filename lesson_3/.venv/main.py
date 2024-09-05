import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
ref_link = 'https://dvmn.org/referrals/MQpyTnsrKoKZOAOCgDOKykyTDwDAbmzWHD5DVB2L/'
friend_name = 'Аркадий'
sender_name = 'Денис'
letter_from = 'borozenetsdn@yandex.ru'
letter_to = 'borozenetsdn@yandex.ru'
subject = 'Приглашение'
content_type = 'text/plain; charset="UTF-8";'
text = """Привет, %friend_name%!, %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

REPLACEMENTS = [
    ("%website%", ref_link),
    ("%friend_name%", friend_name),
    ("%my_name%", sender_name),
]

for replacement in REPLACEMENTS:
    text = text.replace(replacement[0], replacement[1])

letter = '''From: {0}
To: {1}
Subject: {2}
Content-Type: {3}

'''.format(letter_from, letter_to, subject, content_type) + text
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(LOGIN, PASSWORD)
server.sendmail(letter_from, letter_to, letter)
server.quit()

