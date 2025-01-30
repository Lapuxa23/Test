from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

home_router = Router()


class HomeworkForm(StatesGroup):
    name = State()
    homework_number = State()
    github_link = State()


@home_router.message(F.text == "/homework")
async def start_homework(message: Message, state: FSMContext):
    await state.set_state(HomeworkForm.name)
    await message.answer("Введите ваше имя:")


@home_router.message(HomeworkForm.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(HomeworkForm.homework_number)
    await message.answer("Введите номер домашки (от 1 до 8):")


@home_router.message(HomeworkForm.homework_number, F.text.regexp(r"^[1-8]$"))
async def process_homework_number(message: Message, state: FSMContext):
    await state.update_data(homework_number=message.text)
    await state.set_state(HomeworkForm.github_link)
    await message.answer("Введите ссылку на GitHub:")


@home_router.message(HomeworkForm.github_link, F.text.startswith("https://"))
async def process_github_link(message: Message, state: FSMContext):
    data = await state.get_data()
    data["github_link"] = message.text
    await message.answer(f" Домашка сохранена!\n\n"
                         f" Имя: {data['name']}\n"
                         f" Номер домашки: {data['homework_number']}\n"
                         f" GitHub: {data['github_link']}")
    await state.clear()
