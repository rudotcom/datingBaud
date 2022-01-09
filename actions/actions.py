import random

from config import INTENT
from intents import get_intent_by_latent
from models import Avatar
from pymorphy2 import MorphAnalyzer

morph = MorphAnalyzer()

avatar_femme = Avatar(voice='Anna+CLB', name='неваляшка', speech_rate=90, speech_volume=1)
avatar_masc = Avatar(voice='aleksandr', name='товарищ майор', speech_rate=90, speech_volume=1)
avatars = list(Avatar.avatar.keys())
name = avatars[0]
avatar = Avatar.avatar[name]


def commit_action(context):
    if 'replies' in INTENT[context.intent].keys():
        reply = random.choice(INTENT[context.intent]['replies'])
        avatar.say(reply)
    # Выполнить действие intent со slots
    # context.intent, context.slots
    if 'action' in INTENT[context.intent].keys():
        ...


def specify_slot(context):
    # Сверить форму с имеющимися слотами
    # context.form, context.slots
    # найти отсутствующие slots и задать уточнение из интента
    missing_slot = ''
    request = INTENT[context.intent]['slots'][missing_slot]
    avatar.say(request)


def perform_or_specify(context):
    """
    если слотов не хватает, сохранить контекст и задвать уточняющий вопрос
    если слотов хватает, контекст обнулить и выполнить действие
    """
    form = context.form
    if all(form):
        commit_action(context)
    else:
        specify_slot(context)
        return context


def find_intent_and_slots(text):
    intent = get_intent_by_latent(text)
    pass


def get_intent_form():
    form = []
    return form
