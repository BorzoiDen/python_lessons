import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
MY_REF_LINK = 'https://dvmn.org/referrals/MQpyTnsrKoKZOAOCgDOKykyTDwDAbmzWHD5DVB2L/'
FRIEND_NAME = 'Аркадий'
MY_NAME = 'Денис'
FROM = 'borozenetsdn@yandex.ru'
TO = 'borozenetsdn@yandex.ru'
SUBJECT = 'Приглашение'
CONTENT_TYPE = 'text/plain; charset="UTF-8";'
TEXT = """Привет, %friend_name%!, %my_name% приглашает тебя на сайт %website%!

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
    ("%website%", MY_REF_LINK),
    ("%friend_name%", FRIEND_NAME),
    ("%my_name%", MY_NAME),
]

for replacement in REPLACEMENTS:
    TEXT = TEXT.replace(replacement[0], replacement[1])

letter = '''From: {0}
To: {1}
Subject: {2}
Content-Type: {3}

'''.format(FROM, TO, SUBJECT, CONTENT_TYPE) + TEXT
letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(LOGIN, PASSWORD)
server.sendmail(FROM, TO, letter)
server.quit()

