from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import keybords.inline.callback_datas as key


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

premises_office_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Можно поскользнуться, споткнуться', callback_data=key.premises_office_callback.new(item_premises_office='you_can_slip')),
        ],
        [
            InlineKeyboardButton(text='Можно удариться', callback_data=key.premises_office_callback.new(item_premises_office='can_be_hit')),
        ],
        [
            InlineKeyboardButton(text='Можно упасть с высоты', callback_data=key.premises_office_callback.new(item_premises_office='fall_from_a_height')),
        ],
        [
            InlineKeyboardButton(text='Можно обжечься, загореться', callback_data=key.premises_office_callback.new(item_premises_office='you_can_get_burned')),
        ],
        [
            InlineKeyboardButton(text='Можно уколоться, порезаться', callback_data=key.premises_office_callback.new(item_premises_office='prick_cut')),
        ],
        [
            InlineKeyboardButton(text='Может придавить', callback_data=key.premises_office_callback.new(item_premises_office='can_crush')),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data=key.premises_office_callback.new(item_premises_office='back')),
        ],
    ]
)

out_of_work_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Неправильно ведутся работы', callback_data=key.out_of_work_callback.new(item_out_of_work='you_can_slip')),
        ],
        [
            InlineKeyboardButton(text='Небезопасное пространство', callback_data=key.out_of_work_callback.new(item_out_of_work='can_be_hit')),
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data=key.out_of_work_callback.new(item_out_of_work='back')),
        ],
    ]
)