from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message
from keyboards.keyboards import section_1_kb, \
    section_2_kb, section_3_kb, section_4_kb, section_5_kb
from lexicon.lexicon_ru import LEXICON_RU

router: Router = Router()

# Этот хэндлер срабатывает на выбор первого раздела
@router.message(Text(text=LEXICON_RU['section_1']))
async def process_section_answer(message: Message):
    await message.answer(text=LEXICON_RU['section_answer'], reply_markup=section_1_kb)


# Этот хэндлер срабатывает на выбор второго раздела
@router.message(Text(text=LEXICON_RU['section_2']))
async def process_section_answer(message: Message):
    await message.answer(text=LEXICON_RU['section_answer'], reply_markup=section_2_kb)


# Этот хэндлер срабатывает на выбор третьего раздела
@router.message(Text(text=LEXICON_RU['section_3']))
async def process_section_answer(message: Message):
    await message.answer(text=LEXICON_RU['section_answer'], reply_markup=section_3_kb)


# Этот хэндлер срабатывает на выбор четвертого раздела
@router.message(Text(text=LEXICON_RU['section_4']))
async def process_section_answer(message: Message):
    await message.answer(text=LEXICON_RU['section_answer'], reply_markup=section_4_kb)


# Этот хэндлер срабатывает на выбор пятого раздела
@router.message(Text(text=LEXICON_RU['section_5']))
async def process_section_answer(message: Message):
    await message.answer(text=LEXICON_RU['section_answer'], reply_markup=section_5_kb)