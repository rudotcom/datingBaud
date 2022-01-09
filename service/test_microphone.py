from models import Avatar, stream
from pymorphy2 import MorphAnalyzer
from grammeme import *

morph = MorphAnalyzer()
stream.start_stream()

avatar_femme = Avatar(voice='Anna+CLB', name='неваляшка', speech_rate=90, speech_volume=1)
avatar_masc = Avatar(voice='aleksandr', name='товарищ майор', speech_rate=90, speech_volume=1)

avatars = list(Avatar.avatar.keys())
name = avatars[0]
avatar = Avatar.avatar[name]

if __name__ == '__main__':

    while True:
        listened = avatar.listen()

        if type(listened) == list:
            text, avatar = listened
        else:
            text = listened

        morph_analysis = []

        for word in text.split(' '):
            word_grammemes = []
            p = morph.parse(word)[0]

            for gram in [anim, entity]:
                for g in gram:
                    if g in p.tag:
                        word_grammemes.append(gram[g])

            morph_analysis.append(' '.join([
                word, '.',
                f'\nначальная форма: {p.normal_form}.' if word != p.normal_form else '',
                '\n  ',
                POS[p.tag.POS] if p.tag.POS else '',
                case[p.tag.case] if p.tag.case else '',
                tense[p.tag.tense] if p.tag.tense else '',
                mood[p.tag.mood] if p.tag.mood else '',
                number[p.tag.number] if p.tag.number else '',
                gender[p.tag.gender] if p.tag.gender else '', '\n    ',
                ' '.join(word_grammemes), '.'
            ]))

        if text:
            morph_analysis = '\n'.join(morph_analysis)
            avatar.say(f'фраза: {text}')
            avatar.say('морфологический разбор')

            avatar.say(morph_analysis)
