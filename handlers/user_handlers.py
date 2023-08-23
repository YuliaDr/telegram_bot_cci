from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup
import keyboards.keyboards as kb
from lexicon.lexicon_ru import LEXICON_RU, LEXICON_SECTIONS

router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def start_command(message: Message):
    keyboard: InlineKeyboardMarkup = await kb.generate_sections_keyboard(2)
    await message.answer(LEXICON_RU["/start"], reply_markup=keyboard)


# Обработчик нажатий на кнопки разделов
@router.callback_query(lambda c: c.data.startswith('section_'))
async def process_callback_section(callback_query: CallbackQuery):
    # Получаем номер раздела из callback_data
    section_num = int(callback_query.data.split("_")[1])
    section_name = list(LEXICON_SECTIONS.keys())[section_num]

    # Создаем inline клавиатуру с вопросами и кнопкой "Назад"
    keyboard: InlineKeyboardMarkup = await kb.generate_questions_keyboard(section_name, section_num, 1)

    # Отправляем сообщение с вопросами
    await callback_query.message.edit_text(
        text=f"Раздел: {section_name}\nВыберите вопрос:",
        reply_markup=keyboard)


# Обработчик нажатий на кнопки вопросов
@router.callback_query(lambda c: c.data.startswith('question_'))
async def process_callback_question(callback_query: CallbackQuery):
    # Получаем номер раздела и номер вопроса из callback_data
    data = callback_query.data.split("_")
    section_num = int(data[1])
    question_num = int(data[2])

    section_name = list(LEXICON_SECTIONS.keys())[section_num]
    question = list(LEXICON_SECTIONS[section_name].keys())[question_num]
    answer = LEXICON_SECTIONS[section_name][question]

    # Создаем inline клавиатуру с кнопками "Вернуться к разделам" и "Назад"
    keyboard: InlineKeyboardMarkup = await kb.generate_answer_keyboard(section_num)

    # Отправляем сообщение с ответом и inline клавиатурой
    await callback_query.message.edit_text(
        text=f"{question}\n\n{answer}",
        reply_markup=keyboard)


# Обработчик нажатий на кнопки "Назад" и "Вернуться к разделам"
@router.callback_query(lambda c: c.data.startswith('back_'))
async def process_callback_back(callback_query: CallbackQuery):
    if callback_query.data == "back_to_sections":
        # Отправляем сообщение со списком разделов
        keyboard: InlineKeyboardMarkup = await kb.generate_sections_keyboard(2)

        await callback_query.message.edit_text(
            text=LEXICON_RU["sections"],
            reply_markup=keyboard)
    else:
        # Получаем номер раздела из callback_data
        section_num = int(callback_query.data.split("_")[1])

        # Отправляем сообщение со списком вопросов раздела
        section_name = list(LEXICON_SECTIONS.keys())[section_num]
        keyboard: InlineKeyboardMarkup = await kb.generate_questions_keyboard(section_name, section_num, 1)

        await callback_query.message.edit_text(
            text=f"Раздел: {section_name}\nВыберите вопрос:",
            reply_markup=keyboard)
