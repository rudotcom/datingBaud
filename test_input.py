from pymorphy2 import MorphAnalyzer
from grammeme import *
from intents import find_intent_and_slots

morph = MorphAnalyzer()


def describe(text):
    for word in text.split(' '):
        instance = morph.parse(word)

        for p in instance:
            word_grammemes = []
            for gram in [anim, entity]:
                for g in gram:
                    if g in p.tag:
                        word_grammemes.append(gram[g])

            print(
                word,
                f'({p.normal_form})' if word != p.normal_form else '',
                p.tag, ' --- ',
                POS[p.tag.POS] if p.tag.POS else '',
                case[p.tag.case] if p.tag.case else '',
                tense[p.tag.tense] if p.tag.tense else '',
                mood[p.tag.mood] if p.tag.mood else '',
                number[p.tag.number] if p.tag.number else '',
                gender[p.tag.gender] if p.tag.gender else '', ' -- ',
                ' '.join(word_grammemes),
            )

        print('__________________________________________')


if __name__ == '__main__':

    phrase = [
        'включи теплый свет в большой комнате ',
        'включи лампу на кухне в 8 часов',
        'включи радио чилаут',
        'позови если тебе не сложно товарища майора пожалуйста',
        'пошли товариша майора в лес',
        'какая будет в пятницу температура в патонге',
        # 'какая завтра погода в лобаново',
        # 'что тяжелее 1.0 килограм ваты или килограм чугуна',
        # 'когда появились вирусы',
        # 'расскажи новости',
        # 'что происходит',
        'какой был курс доллара вчера',
    ]

    for text in phrase:
        print(text)
        print('==============================================')
        print(find_intent_and_slots(text))
        print('==============================================')
        # print(describe(text))
