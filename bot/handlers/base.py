from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from aiogram.utils.i18n import gettext as _

from bot.handlers.buttons.inline import current_chat_button, game_menu
from bot.handlers.utils import check_moves, moves, to_dict

main_router = Router()


@main_router.callback_query(F.data.startswith("game="))
async def game_callback_handler(query: CallbackQuery) -> None:
    data = await to_dict(query.data)
    move = data['y']
    user_id = data[move + '_id']
    query_user_id = str(query.from_user.id)
    if user_id == '?' and query_user_id not in (data['x_id'], data['o_id']):
        data[move + '_id'] = query_user_id
        user_id = data[move + '_id']
    if user_id == query_user_id:
        if data['y'] == 'o':
            txt = f"❌ {data['x_id']} 👈\n⭕️ {data['o_id']}"
            data['y'] = 'x'
        else:
            txt = f"❌ {data['x_id']}\n⭕️ {data['o_id']} 👈"
            data['y'] = 'o'
        data[move] = data[move][2:] + '_' + data['id']
        if data[move][0] != "?" and await check_moves(data[move]):
            user2_id = data[data['y'] + '_id']
            await query.bot.edit_message_reply_markup(inline_message_id=query.inline_message_id)
            await query.bot.edit_message_text(
                f"""
[{query.from_user.first_name}](tg://user?id=<{user_id}>) 🏆
[{user2_id}](tg://user?id=<{user2_id}>) 😢
{await moves(data)}""",
                inline_message_id=query.inline_message_id,
                reply_markup=current_chat_button(), parse_mode=ParseMode.MARKDOWN)
            return
        del data['id']

        await query.bot.edit_message_text(txt, inline_message_id=query.inline_message_id,
                                          reply_markup=await game_menu(**data))
    else:
        await query.answer(_("‼ It’s not your move."), True, cache_time=5)


@main_router.callback_query(F.data.startswith("invalid"))
async def invalid_handler(call: CallbackQuery) -> None:
    await call.answer(_("Already clicked 😢"), True)
