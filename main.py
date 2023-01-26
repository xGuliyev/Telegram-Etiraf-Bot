from config import Config
from pyrogram import Client, idle
from pyromod import listen

app = Client(
    ":memory:",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins"),
)

if __name__ == "__main__":
    app.start()
    uname = app.get_me().username
    print(f"@{uname} başladı!")
    idle()
    app.stop()
    print("Bot dayandı!")
