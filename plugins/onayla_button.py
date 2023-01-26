from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
from plugins.dil import LAN


@Client.on_callback_query(filters.regex(r"onayla"))
async def _onaylama(bot, query):
    user = query.data.split()[1]
    await bot.send_message(
        Config.ETIRAF_CHANNEL,
        text=query.message.text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=LAN.ITIRAF_CHANNEL_TEXT_BUTTON,
                        url=f"https://t.me/{Config.BOT_USERNAME}",
                    )
                ]
            ]
        ),
    )
    await query.edit_message_caption(LAN.ITIRAF_ACCEPT)
    await bot.send_message(
        user,
        text=LAN.ITIRAF_OPEN_ACCEPT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=LAN.ITIRAF_CHANNEL_TEXT,
                        url=f"http://t.me/{Config.ITIRAF_CHANNEL}",
                    )
                ]
            ]
        ),
    )
