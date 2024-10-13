from aiogram import Bot, Router
from aiogram.types import InlineQuery, InlineQueryResultCachedSticker, InputTextMessageContent
from bot.handlers.buttons.inline import game_menu
from config import BotConfig

inline_query_router = Router()


@inline_query_router.inline_query()
async def inline_handler(query: InlineQuery, bot: Bot) -> None:
    # Kim ishlatayotgan bo'lsa kanalga jo'natib turadi
    # await bot.send_message(BotConfig.CHANNEL_ID, f'#id{query.from_user.id}\n' + str(query.model_dump_json(indent=5)))
    result = [
        InlineQueryResultCachedSticker(
            id='1',
            sticker_file_id='CAACAgIAAxkBAAEbBSxm0dUN_PiPu6KJNhMc47ZeAhVBnAACdgADC-I1Bh3j8PU2N9bKNQQ',
            input_message_content=InputTextMessageContent(message_text=f"❌ {query.from_user.id} 👈\n⭕️ ?"),
            reply_markup=await game_menu(x_id=str(query.from_user.id))
        ),
        InlineQueryResultCachedSticker(
            id='2',
            sticker_file_id='CAACAgIAAxkBAAEbGzZm3KwIPipDhxrltSfzfnSHjD6aOgACeAADC-I1BmUYUFTDFXAYNgQ',
            input_message_content=InputTextMessageContent(message_text=f"❌ ? 👈\n⭕️ {query.from_user.id}"),
            reply_markup=await game_menu(o_id=str(query.from_user.id))
        ),
    ]

    await query.answer(result, 5)
