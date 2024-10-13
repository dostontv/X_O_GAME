from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _

from bot.handlers.buttons.inline import main_button

start_router = Router()


@start_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    if not data.get('locale'):
        lang = message.from_user.language_code
        if lang in ('uz', 'en', 'ru'):
            await state.update_data(locale=lang)
    await message.answer(
        _("🖐 Hello, {name}!\n 🎮 To start the game, click the button below and select a chat.").format(
            name=message.from_user.full_name),
        reply_markup=main_button())
