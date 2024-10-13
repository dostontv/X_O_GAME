from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils.i18n import gettext as _

from bot.handlers.buttons.inline import lang_btn

lang_router = Router()


@lang_router.message(Command('lang'))
async def chose_lang_handler(msg: Message):
    await msg.answer(_("🌍 Select a language"), reply_markup=lang_btn())


@lang_router.callback_query(F.data.startswith('l='))
async def select_handler(call: CallbackQuery, state: FSMContext):
    lang = call.data[2:]
    await state.update_data(locale=lang)
    await call.message.answer(_("✅ Language selected", locale=lang))
    await call.message.delete()
