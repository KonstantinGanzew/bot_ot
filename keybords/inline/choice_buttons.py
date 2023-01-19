from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import keybords.inline.callback_datas as key

back_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        
    ]
)

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Наблюдатель', callback_data=key.menu_callback.new(item_menu='observer')),
        ],
        [
            InlineKeyboardButton(text='Охотник', callback_data=key.menu_callback.new(item_menu='hunter')),
        ],
        [
            InlineKeyboardButton(text='Сколько у меня баллов', callback_data=key.menu_callback.new(item_menu='how_many_points')),
        ],
        [
            InlineKeyboardButton(text='Обменять баллы', callback_data=key.menu_callback.new(item_menu='redeem_points')),
        ],
        [
            InlineKeyboardButton(text='Рейтинг лучших', callback_data=key.menu_callback.new(item_menu='rating_of_the_best')),
        ],
    ]
)

observer_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Территория, улица', callback_data=key.observer_callback.new(item_observer='territory_street')),
        ],
        [
            InlineKeyboardButton(text='Помещение, офис', callback_data=key.observer_callback.new(item_observer='premises_office')),
        ],
        [
            InlineKeyboardButton(text='Вне работы', callback_data=key.observer_callback.new(item_observer='out_of_work')),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data=key.observer_callback.new(item_observer='back')),
        ],
    ]
)

territory_street_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Можно поскользнуться, споткнуться', callback_data=key.territory_street_callback.new(item_territory_street='you_can_slip')),
        ],
        [
            InlineKeyboardButton(text='Можно удариться', callback_data=key.territory_street_callback.new(item_territory_street='can_be_hit')),
        ],
        [
            InlineKeyboardButton(text='Что-то может упасть на голову', callback_data=key.territory_street_callback.new(item_territory_street='fall_on_your_head')),
        ],
        [
            InlineKeyboardButton(text='Можно провалиться', callback_data=key.territory_street_callback.new(item_territory_street='out_of_work')),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data=key.territory_street_callback.new(item_territory_street='back')),
        ],
    ]
)
