from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import LEXICON_RU, LEXICON_SECTIONS


# Функция генерации клавиатуры с разделами
async def generate_sections_keyboard(width: int = 2):
    sections = list(LEXICON_SECTIONS.keys())
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for i, section in enumerate(sections):
        buttons.append(InlineKeyboardButton(text=section, callback_data=f"section_{i}"))

    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()


# Функция генерации клавиатуры с вопросами раздела
async def generate_questions_keyboard(section_name: str, section_num: int, width: int = 1):
    sections = LEXICON_SECTIONS
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    for i, question in enumerate(sections[section_name]):
        buttons.append(InlineKeyboardButton(text=question, callback_data=f"question_{section_num}_{i}"))

    buttons.append(InlineKeyboardButton(text=LEXICON_RU["back_to_sections"], callback_data="back_to_sections"))
    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()


# Функция генерации клавиатуры с кнопками "Вернуться к разделам" и "Назад"
async def generate_answer_keyboard(section_num: int):
    back_button = InlineKeyboardButton(
        text=LEXICON_RU["back_to_questions"], callback_data=f"back_{section_num}")
    back_to_sections_button = InlineKeyboardButton(
        text=LEXICON_RU["back_to_sections"], callback_data="back_to_sections")

    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[[back_button], [back_to_sections_button]])

    return keyboard
