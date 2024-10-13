from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_button():
    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=_("🎮 Start the game"), switch_inline_query='')
            ]
        ]
    )
    return btn


def current_chat_button():
    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🔄", switch_inline_query_current_chat='')
            ]
        ]
    )
    return btn


async def game_menu(x_id="?", o_id="?", x="?_?_?", o="?_?_?", y='x'):
    """game=x_id=user_id=o_id=user_id=x=?_?_?=o=?_?_?=y=x or o=id=1...9"""
    btn = InlineKeyboardBuilder()
    btn.add(
        *[
            InlineKeyboardButton(
                text="   ❌   " if x.find(str(i)) != -1 else "   ⭕️   " if o.find(str(i)) != -1 else "   ⬜   ",
                callback_data=f"game=x_id={x_id}=o_id={o_id}=x={x}=o={o}=y={y}=id={i}" if (x + o).find(
                    str(i)) == -1 else "invalid"
            )
            for i in range(9)
        ])
    btn.adjust(3, repeat=True)
    return btn.as_markup()


def lang_btn():
    btn = InlineKeyboardBuilder()
    btn.add(
        *[
            InlineKeyboardButton(text="🇬🇧", callback_data='l=en'),
            InlineKeyboardButton(text='🇺🇿', callback_data='l=uz'),
            InlineKeyboardButton(text='🇷🇺', callback_data='l=ru')
        ])
    return btn.as_markup()


def button_video(txt):
    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🔗 Do\'stlarni taklif qilish', url=f'https://t.me/share/url?url={txt}')]
        ])
    return btn
