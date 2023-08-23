from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message
from keyboards.keyboards import sections_kb
from lexicon.lexicon_ru import LEXICON_RU

router: Router = Router()

# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=sections_kb)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=sections_kb)


# Этот хэндлер срабатывает на возврат к разделам
@router.message(Text(text=LEXICON_RU['back']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['sections'], reply_markup=sections_kb)

