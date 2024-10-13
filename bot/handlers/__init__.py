from aiogram import Router

from bot.handlers.base import main_router
from bot.handlers.inline_queries.inline_query_ import inline_query_router
from bot.handlers.private_handlers import private_routers

routers = Router()

routers.include_routers(private_routers, main_router, inline_query_router)
