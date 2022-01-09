POS = {
    'NOUN': 'имя существительное',  # хомяк
    'ADJF': 'имя прилагательное (полное)',  # хороший
    'ADJS': 'имя прилагательное (краткое)',  # хорош
    'COMP': 'компаратив',  # лучше, получше, выше
    'VERB': 'глагол (личная форма)',  # говорю, говорит, говорил
    'INFN': 'глагол (инфинитив)',  # говорить, сказать
    'PRTF': 'причастие (полное)',  # прочитавший, прочитанная
    'PRTS': 'причастие (краткое)',  # прочитана
    'GRND': 'деепричастие',  # прочитав, рассказывая
    'NUMR': 'числительное',  # три, пятьдесят
    'ADVB': 'наречие',  # круто
    'NPRO': 'местоимение-существительное',  # он
    'PRED': 'предикатив',  # некогда
    'PREP': 'предлог',  # в
    'CONJ': 'союз',  # и
    'PRCL': 'частица',  # бы, же, лишь
    'INTJ': 'междометие',  # ой
}
case = {
    'nomn': 'именительный',  # Кто? Что?	хомяк ест
    'gent': 'родительный',  # Кого? Чего?	у нас нет хомяка
    'datv': 'дательный',  # Кому? Чему?	сказать хомяку спасибо
    'accs': 'винительный',  # Кого? Что?	хомяк читает книгу
    'ablt': 'творительный',  # Кем? Чем?	зерно съедено хомяком
    'loct': 'предложный',  # О ком? О чём? и т.п.	хомяка несут в корзинке
    'voct': 'звательный',  # Его формы используются при обращении к человеку.	Саш, пойдем в кино.
    'gen2': 'второй родительный (частичный)',  # ложка сахару (gent - производство сахара); стакан яду (gent - нет яда)
    'acc2': 'второй винительный',  # записался в солдаты
    'loc2': 'второй предложный (местный)',
    # я у него в долгу (loct - напоминать о долге); висит в шкафу (loct - монолог о шкафе); весь в снегу (loct - писать о снеге)
}
number = {
    'sing': 'единственное число',  # хомяк, говорит
    'plur': 'множественное число',  # хомяки, говорят
}
gender = {
    'masc': 'мужской род',  # хомяк, говорил
    'femn': 'женский род',  # хомячиха, говорила
    'neut': 'средний род',  # зерно, говорило
}
anim = {
    'inan': 'неодушевленное',
    'anim': 'одушевленное',
}
tense = {  # категория времени
    'pres': 'настоящее время',
    'past': 'прошедшее время',
    'futr': 'будущее время',
}
entity = {
    'Name': 'имя',
    'Surn': 'фамилия',
    'Patr': 'отчество',
    'Geox': 'топоним',
    'Orgn': 'организация',
    'Trad': 'торговая марка',
}
mood = {
    # 'MOod': 'категория наклонения',
    'indc': 'изъявительное наклонение',
    'impr': 'повелительное наклонение',
}
grammeme = {
    'Abbr': 'аббревиатура',
    'Subx': 'возможна субстантивация',
    'Supr': 'превосходная степень',
    'Qual': 'качественное',
    'Apro': 'местоименное',
    'Anum': 'порядковое',
    'Poss': 'притяжательное',
    'V-ey': 'форма на -ею',
    'V-oy': 'форма на -ою',
    'Cmp2': 'сравнительная степень на по-',
    'V-ej': 'форма компаратива на -ей',
    'ASpc': 'категория вида',
    'perf': 'совершенный вид',
    'impf': 'несовершенный вид',
    #    'TRns':	'категория переходности',
    'tran': 'переходный',
    'intr': 'непереходный',
    'Impe': 'безличный',
    'Impx': 'возможно безличное употребление',
    'Mult': 'многократный',
    'Refl': 'возвратный',
    # 'PErs': 'категория лица',
    '1per': '1 лицо',
    '2per': '2 лицо',
    '3per': '3 лицо',
    # 'INvl': 'категория совместности',
    'incl': 'говорящий включён (идем, идемте)',
    'excl': 'говорящий не включён в действие (иди, идите)',
    # 'VOic': 'категория залога',
    'actv': 'действительный залог',
    'pssv': 'страдательный залог',
    'Infr': 'разговорное',
    'Slng': 'жаргонное',
    'Arch': 'устаревшее',
    'Litr': 'литературный вариант',
    'Erro': 'опечатка',
    'Dist': 'искажение',
    'Ques': 'вопросительное',
    'Dmns': 'указательное',
    'Prnt': 'вводное слово',
    'V-be': 'форма на -ье',
    'V-en': 'форма на -енен',
    'V-ie': 'форма на -и- (веселие, твердостию); отчество с -ие',
    'V-bi': 'форма на -ьи',
    'Fimp': 'деепричастие от глагола несовершенного вида',
    'Prdx': 'может выступать в роли предикатива',
    'Coun': 'счётная форма',
    'Coll': 'собирательное числительное',
    'V-sh': 'деепричастие на -ши',
    'Af-p': 'форма после предлога',
    'Inmx': 'может использоваться как одуш. / неодуш.',
    'Vpre': 'Вариант предлога ( со, подо, ...)',
    'Anph': 'Анафорическое (местоимение)',
    'Init': 'Инициал',
    'Adjx': 'может выступать в роли прилагательного',
    'Ms-f': 'колебание по роду (м/ж/с): кофе, вольво',
    'Hypo': 'гипотетическая форма слова (победю, асфальтовее)',
}
