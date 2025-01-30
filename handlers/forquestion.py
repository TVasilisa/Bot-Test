from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from studenthw import start_router

from database import Database
from bot_config import database

start_router = Router()
send_router = Router()


class Question(StatesGroup):
    name = State()
    number = State()
    link = State()


@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer('Привет, друг')


@send_router.message(Command('homework'))
async def start_sending(message: types.Message, state: FSMContext):
    await message.answer("Укажите ваше имя:")
    await state.set_state(Question.name)


@send_router.message(Question.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer('Укажите номер домашнего задания:')
    await state.set_state(Question.number)


@send_router.message(Question.number)
async def process_number(message: types.Message, state: FSMContext):
    number = message.text
    await state.update_data(number=number)
    await message.answer('Отправьте ссылку на дз:')
    await state.set_state(Question.link)


@send_router.message(Question.link)
async def process_number(message: types.Message, state: FSMContext):
    link = message.text
    await state.update_data(link=link)
    await message.answer("Спасибо")
    data = await state.get_data()
    database.send_homework(data)
    print(data)
    await state.clear()