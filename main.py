import logging
import sys
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import BotCommand
from aiogram.utils.i18n import I18n, FSMI18nMiddleware
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from redis.asyncio import Redis

from bot.handlers import routers
from config import BotConfig

TOKEN = BotConfig.TOKEN

WEB_SERVER_HOST = BotConfig.WEB_SERVER_HOST
WEB_SERVER_PORT = BotConfig.WEB_SERVER_PORT

WEBHOOK_PATH = BotConfig.WEBHOOK_PATH
WEBHOOK_SECRET = BotConfig.WEBHOOK_SECRET
BASE_WEBHOOK_URL = BotConfig.BASE_WEBHOOK_URL


async def on_startup(dispatcher: Dispatcher, bot: Bot) -> None:
    commands = [
        BotCommand(command="start", description="Starts the bot."),
        BotCommand(command="lang", description="Changes the language of the bot."),
    ]
    await bot.set_my_commands(commands)
    dispatcher.include_router(routers)
    # WEBHOOK
    # await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}", secret_token=WEBHOOK_SECRET, drop_pending_updates=True)


async def on_shutdown(bot: Bot) -> None:
    await bot.delete_my_commands()
    # DELETE WEBHOOK
    # await bot.delete_webhook()


async def main() -> None:
    storage = RedisStorage(redis=Redis())
    dp = Dispatcher(storage=storage)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    i18n = I18n(path="locales", default_locale='en')
    dp.update.outer_middleware(FSMI18nMiddleware(i18n))

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)  # POLLING

    # WEBHOOK
    # app = web.Application()
    # webhook_requests_handler = SimpleRequestHandler(
    #     dispatcher=dp,
    #     bot=bot,
    #     secret_token=WEBHOOK_SECRET,
    # )
    # webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    #
    # setup_application(app, dp, bot=bot)
    #
    # web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # main()
    asyncio.run(main())  # POLLING
