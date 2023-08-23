from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU


# ------- Создаем клавиатуру с разделами -------

# Создаем кнопки с ответами согласия и отказа
sections_buttons: list[KeyboardButton] = [
    KeyboardButton(text=LEXICON_RU['section_1']),
    KeyboardButton(text=LEXICON_RU['section_2']),
    KeyboardButton(text=LEXICON_RU['section_3']),
    KeyboardButton(text=LEXICON_RU['section_4']),
    KeyboardButton(text=LEXICON_RU['section_5'])
    ]

# Инициализируем билдер для клавиатуры с разделами
sections_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Распаковываем список в методом add
sections_kb_builder.add(*sections_buttons)

# Добавляем кнопки в билдер с параметром поочередно по 2 и по 1 в рядах
sections_kb_builder.adjust(2, 1, repeat=True)

# Создаем клавиатуру с разделами
sections_kb = sections_kb_builder.as_markup(
    resize_keyboard=True,
    input_field_placeholder='Выберите раздел'
)


# ------- Создаем кнопку "Назад" -------
back_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['back'])


# ------- Создаем клавиатуру с вопросами первого раздела -------

# Создаем кнопки клавиатуры первого раздела
section_1_buttons: list[KeyboardButton] = [
    KeyboardButton(text=LEXICON_RU['question_1_1']),
    KeyboardButton(text=LEXICON_RU['question_1_2']),
    KeyboardButton(text=LEXICON_RU['question_1_3']),
    back_button
    ]

# Инициализируем билдер для клавиатуры первого раздела
section_1_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Распаковываем список в методом add
section_1_kb_builder.add(*section_1_buttons)

# Добавляем кнопки в билдер с параметром поочередно по 2 и по 1 в рядах
section_1_kb_builder.adjust(2, 1, 1, repeat=True)

# Создаем клавиатуру первого раздела
section_1_kb = section_1_kb_builder.as_markup(resize_keyboard=True)



# ------- Создаем клавиатуру с вопросами второго раздела -------

# Создаем кнопки клавиатуры второго раздела
section_2_buttons: list[KeyboardButton] = [
    KeyboardButton(text=LEXICON_RU['question_2_1']),
    KeyboardButton(text=LEXICON_RU['question_2_2']),
    KeyboardButton(text=LEXICON_RU['question_2_3']),
    KeyboardButton(text=LEXICON_RU['question_2_4']),
    back_button
    ]

# Инициализируем билдер для клавиатуры второго раздела
section_2_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Распаковываем список в методом add
section_2_kb_builder.add(*section_2_buttons)

# Добавляем кнопки в билдер с параметром по 2 в рядах
section_2_kb_builder.adjust(2, repeat=True)

# Создаем клавиатуру второго раздела
section_2_kb = section_2_kb_builder.as_markup(resize_keyboard=True)



# ------- Создаем клавиатуру с вопросами третьего раздела -------

# Создаем кнопки клавиатуры третьего раздела
section_3_buttons: list[KeyboardButton] = [
    KeyboardButton(text=LEXICON_RU['question_3_1']),
    KeyboardButton(text=LEXICON_RU['question_3_2']),
    back_button
    ]

# Инициализируем билдер для клавиатуры третьего раздела
section_3_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Распаковываем список в методом add
section_3_kb_builder.add(*section_3_buttons)

# Добавляем кнопки в билдер с параметром по 2 в рядах
section_3_kb_builder.adjust(2, repeat=True)

# Создаем клавиатуру третьего раздела
section_3_kb = section_3_kb_builder.as_markup(resize_keyboard=True)



# ------- Создаем клавиатуру с вопросами четвертого раздела -------

# Создаем кнопки клавиатуры четвертого раздела
section_4_buttons: list[KeyboardButton] = [
    KeyboardButton(text=LEXICON_RU['question_4_1']),
    KeyboardButton(text=LEXICON_RU['question_4_2']),
    KeyboardButton(text=LEXICON_RU['question_4_3']),
    KeyboardButton(text=LEXICON_RU['question_4_4']),
    KeyboardButton(text=LEXICON_RU['question_4_5']),
    KeyboardButton(text=LEXICON_RU['question_4_6']),
    back_button
    ]

# Инициализируем билдер для клавиатуры четвертого раздела
section_4_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Распаковываем список в методом add
section_4_kb_builder.add(*section_4_buttons)

# Добавляем кнопки в билдер с параметром поочередно по 2 и по 1 в рядах
section_4_kb_builder.adjust(3, repeat=True)

# Создаем клавиатуру четвертого раздела
section_4_kb = section_4_kb_builder.as_markup(resize_keyboard=True)



# ------- Создаем клавиатуру с вопросами пятого раздела -------

# Создаем кнопки клавиатуры пятого раздела
section_5_buttons: list[KeyboardButton] = [
    KeyboardButton(text=LEXICON_RU['question_5_1']),
    back_button
    ]

# Инициализируем билдер для клавиатуры пятого раздела
section_5_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Распаковываем список в методом add
section_5_kb_builder.add(*section_5_buttons)

# # Добавляем кнопки в билдер с параметром поочередно по 2 и по 1 в рядах
section_5_kb_builder.adjust(1, repeat=True)

# Создаем клавиатуру пятого раздела
section_5_kb = section_5_kb_builder.as_markup(resize_keyboard=True)
