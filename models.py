import json
import pickle
import random
import subprocess
import os
import pyglet

import pyaudio
from vosk import Model, KaldiRecognizer
import settings
import face_recognition
from datetime import datetime, timedelta


class Face(object):
    class_instances = []
    remember_seconds = settings.remember_seconds
    selected = None
    height_of_selected = 0

    def __init__(self, name: str, encoding):
        self.encoding = encoding
        self.name = name
        self._last_seen = datetime.now() - timedelta(seconds=Face.remember_seconds)
        self.class_instances.append(self)

    def see_you(self):
        self._last_seen = datetime.now()
        print('see:', self.name)

    def hello(self):
        print(f'{random.choice(settings.PHRASES["hello"])}, {self.name}')
        Avatar.say(f'{random.choice(settings.PHRASES["hello"])}, {self.name}')

    @property
    def recently_seen(self):
        # True если было видимо меньше чем remember_seconds назад
        return (datetime.now() - self._last_seen).seconds < Face.remember_seconds

    @classmethod
    def by_encoding(cls, encoding):
        minimal_distance = 1
        for person in cls.class_instances:
            # if face_recognition.compare_faces([person.encoding], encoding):
            #     return person

            # Если совпадение не найдено, смотрим похоже ли лицо на лицо из класса
            face_distance = face_recognition.face_distance([person.encoding], encoding)

            if face_distance < minimal_distance:
                minimal_distance = face_distance
                closest_face = person

        if minimal_distance < 0.60:
            return closest_face


class Assistant:
    avatar = dict()  # Создаем словарь аватаров с ключем "ИМЯ"
    voice = 'Anna+CLB'
    speech_rate = 120
    speech_volume = 1

    @staticmethod
    def make_friends(encoding, name):
        # сохраняем кодировку в файл с именем лица
        face = Face(name, encoding)

        # переводим ndarray в формат для базы данных
        pickled_encoding = pickle.dumps(encoding)
        # Вставляем данные в таблицу
        settings.cursor.execute(f"INSERT INTO faces VALUES (?, ?)", (name, pickled_encoding))
        settings.conn.commit()
        Avatar.say(f'Приятно познакомиться, {name}')

    @staticmethod
    def confirm(copy_that):
        if copy_that in random.choice(settings.PHRASES['positive'] + ['моё']):
            return True

    @staticmethod
    def play_wav(src):
        wav_file = settings.ROOT_DIR + r'/static/wav/' + src + '.wav'
        try:
            alert = pyglet.media.load(wav_file)
            alert.play()
        except FileNotFoundError:
            print('Файл не найден:', wav_file)


class Avatar(Assistant):

    def __init__(self, voice, name, speech_rate=90, speech_volume=1):
        self.voice = voice
        self.speech_rate = speech_rate
        self.speech_volume = speech_volume
        self.name = name
        Avatar.avatar[name] = self

    def say(self, text):
        stream.stop_stream()
        shell = f'echo "{text}" | RHVoice-client -s {self.voice} | aplay'
        print(f'--> {text}')
        process = subprocess.Popen(shell, shell=True)
        process.communicate()
        process.poll()
        stream.start_stream()

    def listen(self):
        text = None
        while not text:
            stream.start_stream()
            data = stream.read(4000, exception_on_overflow=False)
            if len(data) == 0:
                return False

            if recognizer.AcceptWaveform(data):
                text = json.loads(recognizer.Result())['text']
                stream.stop_stream()

                for name in list(Avatar.avatar.keys()):
                    if text.startswith(name):
                        avatar = Avatar.avatar[name]
                        text = text.replace(name, '')
                        return [text, avatar]

                return text


class Context:
    slots = []
    form = {}

    def __init__(self, text):
        # self.intent, self.slots = find_intent_and_slots(text)
        # self.form = get_intent_form()
        """
        TODO: решить, как определять тип слота и его наличие в тексте !!!
        """
        ...

    def add(self, text):
        # добавить текст в слот, если соответствует типу
        ...


# Voice model settings
model_path = os.path.join(settings.ROOT_DIR, settings.voice_model_name)
if not os.path.exists(model_path):
    print(
        "Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as "
        "'model' in the current folder.")
    exit(1)

model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()
