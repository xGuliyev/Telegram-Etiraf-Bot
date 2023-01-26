from pyrogram import Client, filters
from main import app
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)
from config import Config
from plugins.dil import LAN


@Client.on_callback_query(filters.regex("etiraf_aciq"))
async def etiraf_aciq(bot: Client, query: CallbackQuery):
    await query.message.delete()
    chat_id = query.message.chat.id
    await bot.send_animation(
        chat_id, animation=f"https://te.legra.ph/file/90eb83c88e4b5b93d2d69.gif"
    )
    etiraf_mesaj = await bot.ask(chat_id, LAN.ITIRAF_YAZ)
    while True:
        if etiraf_mesaj.text.startswith("/"):
            etiraf_mesaj = await bot.ask(
                query.from_user.id, text=LAN.ITIRAF_YAZ_ZAMAN, timeout=30
            )
        elif etiraf_mesaj.text.lower() == "cancel":
            await etiraf_mesaj.reply(LAN.ITIRAF_CANCEL)
            break
        else:
            await bot.send_message(
                chat_id,
                text=LAN.ITIRAF_GONDERILDI.format(
                    query.from_user.mention, etiraf_mesaj.text
                ),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text=LAN.ITIRAF_CHANNEL_TEXT,
                                url=f"https://t.me/{Config.ITIRAF_CHANNEL}",
                            )
                        ]
                    ]
                ),
            )
            await bot.send_message(
                Config.LOG_ADMINS,
                text=LAN.ITIRAF_GONDERILDI_ADMIN_OPEN.format(
                    query.from_user.mention, query.from_user.id
                ),
            )
            await bot.send_message(
                Config.LOG_ADMINS,
                text=LAN.ITIRAF_GONDERILDI_OPEN_MESAJ.format(
                    query.from_user.mention, etiraf_mesaj.text
                ),
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text=LAN.ITIRAF_GONDER,
                                callback_data=f"onayla {query.from_user.id}",
                            ),
                            InlineKeyboardButton(
                                text=LAN.ITIRAF_SIL,
                                callback_data=f"kapat {query.from_user.id}",
                            ),
                        ]
                    ]
                ),
            )
            break
    print(f"{query.from_user.first_name} açıq etiraf yazdı")
