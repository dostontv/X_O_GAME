from aiogram import Router, F
from aiogram.enums import ChatType

from bot.handlers.private_handlers.lang import lang_router
from bot.handlers.private_handlers.start import start_router

private_routers = Router()

private_routers.include_routers(start_router, lang_router)
private_routers.message.filter(F.chat.type == ChatType.PRIVATE)
