import sqlite3
import os

voice_model_name = 'model_big'
AVATAR_NAME = 'Неваляшка'
remember_seconds = 7200


# ######## CAMERA ########
#       Получить ссылку на вебкамеру (#0 - камера по умолчанию)
image_source = 0
#       Получить ссылку на IP камеру
# camera_ip = '192.168.1.15'
# image_source = f'rtsp://{camera_ip}/live/ch00_1'

PHRASES = {
    'hello': ['Здравствуй', 'Привет', 'Как дела', 'рада тебя видеть'],
    'make_friends': [f'Меня зовут {AVATAR_NAME}, а тебя?', 'Как тебя зовут?',
                     f'Давай познакомимся. Меня зовут {AVATAR_NAME}, а тебя?'],
    'come_closer': ['Подойди поближе пожалуста', 'Ближе, не бойся', 'Ближе', 'Чуть ближе'],
    'my_name_is': ['а меня', 'меня', 'зовут', 'моё имя', 'меня звать', ],
    'your_name_is': ['тебя зовут', 'твое имя', '', ],
    'is_your_name': ['правильно?', 'я правильно услышала?', 'так?', 'это верно?'],
    'positive': ['верно', 'правильно', 'да', 'конечно', 'безусловно', 'права', 'так', 'всё'],
}

conn = sqlite3.connect('faces.sqlite3')
cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE faces (name text, encoding BLOB)")
    conn.commit()
except:
    ...

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
