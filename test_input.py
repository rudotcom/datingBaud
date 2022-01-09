from pymorphy2 import MorphAnalyzer
from grammeme import *

morph = MorphAnalyzer()


if __name__ == '__main__':

    phrase = [
        'включи теплый свет',
        'включи лампу на кухне в 8 часов',
        'давай включим радио чилаут',
        'позови товарища майора',
        'какая сейчас температура в ебенях',
        'какая завтра погода в лобаново',
        'что тяжелее 1.0 килограм ваты или килограм чугуна',
        'когда появились вирусы',
        'расскажи новости',
        'что происходит',
        'какой курс доллара',
    ]

    for text in phrase:
        print(text, '\n==============================================')

        for word in text.split(' '):
            word_grammemes = []
            p = morph.parse(word)[0]

            for gram in [anim, entity]:
                for g in gram:
                    if g in p.tag:
                        word_grammemes.append(gram[g])

            print(
                word,
                f'({p.normal_form})' if word != p.normal_form else '',
                p.tag, '\n  ',
                POS[p.tag.POS] if p.tag.POS else '',
                case[p.tag.case] if p.tag.case else '',
                tense[p.tag.tense] if p.tag.tense else '',
                mood[p.tag.mood] if p.tag.mood else '',
                number[p.tag.number] if p.tag.number else '',
                gender[p.tag.gender] if p.tag.gender else '', '\n    ',
                ' '.join(word_grammemes),
            )

        print('__________________________________________')
