from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router: Router = Router()


# ------- Хендлеры для вопросов первого раздела -------

# Этот хэндлер срабатывает на выбор первого вопроса в первом разделе
@router.message(Text(text=LEXICON_RU[f'question_1_1']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU[f'answer_1_1'])


@router.message(Text(text=LEXICON_RU[f'question_1_2']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU[f'answer_1_2'])


@router.message(Text(text=LEXICON_RU[f'question_1_3']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU[f'answer_1_3'])


# ------- Хендлеры для вопросов второго раздела -------

@router.message(Text(text=LEXICON_RU[f'question_2_1']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU[f'answer_2_1'])


@router.message(Text(text=LEXICON_RU[f'question_2_2']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU[f'answer_2_2'])


@router.message(Text(text=LEXICON_RU[f'question_2_3']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU[f'answer_2_3'])


@router.message(Text(text=LEXICON_RU[f'question_2_4']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU[f'answer_2_4'])


# ------- Хендлеры для вопросов третьего раздела -------

@router.message(Text(text=LEXICON_RU[f'question_3_1']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU[f'answer_3_1'])


@router.message(Text(text=LEXICON_RU[f'question_3_2']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU[f'answer_3_2'])


# ------- Хендлеры для вопросов четвертого раздела -------

@router.message(Text(text=LEXICON_RU[f'question_4_1']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU[f'answer_4_1'])


@router.message(Text(text=LEXICON_RU[f'question_4_2']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU[f'answer_4_2'])


@router.message(Text(text=LEXICON_RU[f'question_4_3']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU[f'answer_4_3'])


@router.message(Text(text=LEXICON_RU[f'question_4_4']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU[f'answer_4_4'])


@router.message(Text(text=LEXICON_RU[f'question_4_5']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU[f'answer_4_5'])


@router.message(Text(text=LEXICON_RU[f'question_4_6']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU[f'answer_4_6'])


# ------- Хендлеры для вопросов пятого раздела -------

@router.message(Text(text=LEXICON_RU[f'question_5_1']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU[f'answer_5_1'])


