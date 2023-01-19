import logging
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from loader import dp
import keybords.inline.choice_buttons as key
import keybords.inline.callback_datas as call_datas
import erp


@dp.message_handler(Command('start'))
async def show_menu(message: Message):
    if erp.get_id_erp(message.from_user.id) == 'ok':
        text = 'Концепция бота проста – дело каждого сотрудника находить риски вокруг себя, то есть ситуации где что-то Может пойти не так, и отправлять фото или описание опасности в систему. За каждую «пойманную» опасность сотруднику будут начисляться баллы, которые он сможет обменять на брендированные товары или другие бонусы.'
    await message.answer(text, reply_markup=key.menu_keyboard)


@dp.callback_query_handler(call_datas.menu_callback.filter(item_menu="observer"))
async def menu_observer(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('Выявление любых опасностей вокруг себя (во время выполнения работ, в офисе или вне его)', reply_markup=key.observer_keyboard)

@dp.callback_query_handler(call_datas.observer_callback.filter(item_observer='territory_street'))
async def menu_observer(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'call = {callback_data}')
    await call.message.edit_text('Дальше что-то должно происходить?)', reply_markup=key.observer_keyboard)