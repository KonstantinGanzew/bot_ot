import logging
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from loader import dp
import keybords.inline.choice_buttons as key
import keybords.inline.callback_datas as call_datas
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
import erp
from bd.sql import db_start, create_profile, edit_profile
from aiogram.dispatcher.filters.state import StatesGroup, State

class Observer(StatesGroup):

    photo = State()
    description = State()

# Кнопка старт, аутентифицирует человека, отправляет клавиатуру
@dp.message_handler(Command('start'))
async def show_menu(message: Message):
    #if erp.get_id_erp(message.from_user.id) == 'ok':
    text = 'Концепция бота проста – дело каждого сотрудника находить риски вокруг себя, то есть ситуации где что-то Может пойти не так, и отправлять фото или описание опасности в систему. За каждую «пойманную» опасность сотруднику будут начисляться баллы, которые он сможет обменять на брендированные товары или другие бонусы.'
    await message.answer(text, reply_markup=key.menu_keyboard)
    await create_profile(message.from_user.id)

# Перенаправляет по меню наблюдатель
@dp.callback_query_handler(call_datas.menu_callback.filter(item_menu="observer"))
async def menu_observer(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('Выявление любых опасностей вокруг себя (во время выполнения работ, в офисе или вне его)', reply_markup=key.observer_keyboard)
    await call.answer()

# Подменю наблюдатель, територия вне офисса
@dp.callback_query_handler(call_datas.observer_callback.filter(item_observer='territory_street'))
async def menu_observer(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('территория, улица (это пространство вне офисного здания – парковка, наружная территория, служебные постройки)', reply_markup=key.territory_street_keyboard)
    await call.answer()

# Подменю наблюдатель, територия офисса
@dp.callback_query_handler(call_datas.observer_callback.filter(item_observer='premises_office'))
async def menu_observer(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('помещение, офис (это пространство внутри офисного здания – любое помещение в здании)', reply_markup=key.premises_office_keyboard)
    await call.answer()

# Подменю наблюдатель, вне офиса
@dp.callback_query_handler(call_datas.observer_callback.filter(item_observer='out_of_work'))
async def menu_you_can_slip(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('вне работы (в данный раздел сотрудник будет проваливаться если заметил нарушение не нашими сотрудниками и не на нашей территории, например, по пути домой)', reply_markup=key.out_of_work_keyboard)
    await call.answer()

# Подменю наблюдатель, територия офисса
@dp.callback_query_handler(call_datas.observer_callback.filter(item_observer='back'))
async def menu_observer(call: CallbackQuery, callback_data: dict):
    text = 'Концепция бота проста – дело каждого сотрудника находить риски вокруг себя, то есть ситуации где что-то Может пойти не так, и отправлять фото или описание опасности в систему. За каждую «пойманную» опасность сотруднику будут начисляться баллы, которые он сможет обменять на брендированные товары или другие бонусы.'
    logging.info(f'call = {callback_data}')
    await call.message.edit_text(text, reply_markup=key.menu_keyboard)
    await call.answer()


# Назад из пункта територия вне офисса
@dp.callback_query_handler(call_datas.territory_street_callback.filter(item_territory_street='back'))
async def menu_observer(call: CallbackQuery, callback_data: dict):
    text = 'Выявление любых опасностей вокруг себя (во время выполнения работ, в офисе или вне его)'
    logging.info(f'call = {callback_data}')
    await call.message.edit_text(text, reply_markup=key.observer_keyboard)
    await call.answer()


# Назад из пункта територия офисса
@dp.callback_query_handler(call_datas.premises_office_callback.filter(item_premises_office='back'))
async def menu_observer(call: CallbackQuery, callback_data: dict):
    text = 'Выявление любых опасностей вокруг себя (во время выполнения работ, в офисе или вне его)'
    logging.info(f'call = {callback_data}')
    await call.message.edit_text(text, reply_markup=key.observer_keyboard)
    await call.answer()


# Назад из пункта вне офисса
@dp.callback_query_handler(call_datas.out_of_work_callback.filter(item_out_of_work='back'))
async def menu_observer(call: CallbackQuery, callback_data: dict):
    text = 'Выявление любых опасностей вокруг себя (во время выполнения работ, в офисе или вне его)'
    logging.info(f'call = {callback_data}')
    await call.message.edit_text(text, reply_markup=key.observer_keyboard)
    await call.answer()

# Подменю наблюдатель, територия вне офисса
@dp.callback_query_handler(call_datas.territory_street_callback.filter(item_territory_street='you_can_slip'))
async def menu_observer(call: CallbackQuery, callback_data: dict):
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('Прикрепи фото')
    await Observer.photo.set()
    await call.answer()

@dp.message_handler(content_types=['photo'], state = Observer.photo)
async def complaint(message: Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    
    print(message)
    await message.reply('Отправь описание')
    await Observer.next()

@dp.message_handler(state = Observer.description)
async def complaint_desc(message: Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['desc'] = message.text
        print(data)
    await state.finish()