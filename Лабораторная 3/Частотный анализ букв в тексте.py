# TODO  Напишите функцию count_letters
str_ = ""
def count_letters(text):
    text = text.lower()
    dict_ = dict()
    global str_
    for letter_ in text:
        if letter_.isalpha():
            str_ += letter_
    for i in str_:
        dict_[i] = str_.count(i)
    # print(dict_)
    # print(len(str_))
    return dict_
# TODO Напишите функцию calculate_frequency
def calculate_frequency(frequency_letters):
    dict_2 = {}
    for key in frequency_letters:
        frequency_letter = frequency_letters.get(key) / len(str_)
        dict_2[key] = frequency_letter
    # print(dict_2)
    return dict_2


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
dict_1 = count_letters(main_str)
calculate_frequency(dict_1)
# TODO Распечатайте в столбик букву и её частоту в тексте
for i in calculate_frequency(dict_1):
    fr_ = calculate_frequency(dict_1).get(i)
    print(f"{i}: {fr_:.2f}")
