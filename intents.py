from pymorphy2 import MorphAnalyzer
from grammeme import *

morph = MorphAnalyzer()


def find_intent_and_slots(text):
    return find_intent_by_imperative(text) or \
           find_intent_by_question(text)


def find_intent_by_question(text):
    words = text.split(' ')
    question_word = None
    subject = []
    obj = []
    when = []
    location = []
    prep = None

    for i, word in enumerate(words):
        gram = morph.parse(word)
        for instance in gram:
            if 'Ques' in instance.tag or instance.normal_form in quest_words:
                question_word = instance.normal_form
                words.pop(i)
                break

    for i, word in enumerate(words):
        gram = morph.parse(word)

        for instance in gram:

            if 'PREP' in gram[0].tag:
                prep = word
                break

            if 'gent' in instance.tag:
                obj.append(instance.normal_form)
                break

            if 'nomn' in instance.tag:
                subject.append(instance.normal_form)
                break

            if prep:
                if 'accs' in instance.tag:
                    # TODO: ВЧЕРА не прокатывает
                    when.append(instance.normal_form)
                    break
                elif 'loct' in instance.tag:
                    location.append(instance.normal_form)
                    break

    context = {
        'interrogative': question_word,
        'subject': subject,
        'object': obj,
        'when': when,
        'location': location,
    }
    return context


def find_intent_by_imperative(text):
    imperative = None
    obj = []
    location = []

    words = text.split(' ')

    for i, word in enumerate(words):
        gram = morph.parse(word)
        if 'VERB' in gram[0].tag and 'impr' in gram[0].tag:
            # находим императив и удаляем из списка слов
            imperative = gram[0]
            words.pop(i)
            break

    if imperative:
        prep_loc = False
        prep = ''

        if 'tran' in imperative.tag:  # если императив переходный
            for i, word in enumerate(words):
                gram = morph.parse(word)

                for instance in gram:
                    # print(word, instance.tag)
                    if 'PREP' in gram[0].tag:
                        prep = word
                        if prep in prep_location:
                            prep_loc = True
                        break
                    if 'sing' in instance.tag and ('gent' in instance.tag or 'accs' in instance.tag):

                        if prep_loc:
                            location.append(instance.normal_form)
                        else:
                            obj.append(instance.normal_form)
                        break
                    if 'loct' in instance.tag and ('NPRO' not in instance.tag or 'NOUN' in instance.tag):
                        location.append(instance.normal_form,)
                        break

        context = {
            'imperative': imperative.normal_form,
            'objects': obj,
            'location': location,
        }
        return context


def get_intent_form():
    form = []
    return form



def get_intent_by_latent(text):
    pass


def prepend(word, preposition=None):
    if preposition:
        return preposition + ' ' + word
    else:
        return word
