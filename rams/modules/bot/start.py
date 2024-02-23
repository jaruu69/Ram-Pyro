# if you can read this, this meant you use code from Geez | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez | Ram Team
import random
from rams import app
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from config import ID_OWNER as owner 

@app.on_callback_query()
def pmowner(client, callback_query):
    user_id = owner
    message = "Halo Owner Ngentod!!!!"
    client.send_message(user_id, message)
    client.answer_callback_query(callback_query.id, text="Message sent")

ramslogo = [
    "https://telegra.ph//file/d751a68b025dd75e06cb0.png",
]

alive_logo = random.choice(ramslogo)

@app.on_message(filters.command("start") & filters.private)
async def start(app, message):
    chat_id = message.chat.id
    file_id = alive_logo
    caption = "halo nak anjing, saya asisten Jar-Pyro\njangan cari yang spesial dari saya.\n\n**Pesan Dari ==>** [✨JAR - UBOT✨](https://github.com/zarszs/Ram-Pyro)"
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("𝗦𝘂𝗽𝗽𝗼𝗿𝘁", url="https://t.me/JarSuprot"),
            InlineKeyboardButton("𝗢𝘄𝗻𝗲𝗿", url="https://t.me/utits"),
        ],
    ])

    await app.send_photo(chat_id, file_id, caption=caption, reply_markup=reply_markup)
