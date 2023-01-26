from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    InputMediaAnimation,
)
from config import Config
from plugins.dil import LAN


@Client.on_message(filters.command(["start"], ["/", "!"]))
async def start(_, msg: Message):
    await _.send_animation(
        chat_id=msg.chat.id,
        animation=f"https://te.legra.ph/file/2ec7302acc70ea68d7ad3.gif",
        caption=LAN.BOT_START.format(msg.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=LAN.BOT_ITIRAF_BUTTON_1, callback_data="etiraf_button"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text=LAN.BOT_ITIRAF_BUTTON_2,
                        url=f"http://t.me/{Config.ITIRAF_UPDATE_CHANNEL}",
                    ),
                    InlineKeyboardButton(
                        text=LAN.BOT_ITIRAF_BUTTON_3,
                        url=f"http://t.me/{Config.ITIRAF_CHANNEL}",
                    ),
                ],
            ]
        ),
    )
    await _.send_message(
        chat_id=Config.LOG_DATABASE,
        text=LAN.LOG_DATABASE.format(msg.from_user.first_name),
    )
    print(f"{msg.from_user.first_name} start etdi")


@Client.on_callback_query(filters.regex("etiraf_button"))
async def cb_info(bot: Client, query: CallbackQuery):
    await query.edit_message_media(
        media=InputMediaAnimation(
            f"https://te.legra.ph/file/796e259cd8d37c4f85d32.gif"
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=LAN.BUTTON_OPEN, callback_data="etiraf_aciq"
                    ),
                    InlineKeyboardButton(
                        text=LAN.BUTTON_ANON, callback_data="etiraf_gizli"
                    ),
                ]
            ]
        ),
    )
    await query.edit_message_caption(
        caption=LAN.ITIRAF_CHOOSE,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=LAN.BUTTON_OPEN, callback_data="etiraf_aciq"
                    ),
                    InlineKeyboardButton(
                        text=LAN.BUTTON_ANON, callback_data="etiraf_gizli"
                    ),
                ]
            ]
        ),
    )


@Client.on_callback_query(filters.regex(r"kapat"))
async def _onaylama(bot, query):
    await bot.send_message(
        Config.LOG_SILINMIS, text=LAN.ITIRAF_SILINDI.format(query.from_user.mention)
    )
    await bot.send_message(Config.LOG_SILINMIS, text=query.message.text)
    await query.edit_message_caption(
        LAN.ITIRAF_SILINDI_ADMINS.format(query.from_user.mention)
    )
    user = query.data.split()[1]
    await bot.send_message(user, text=LAN.ITIRAF_KABUL_EDILMEDI)
