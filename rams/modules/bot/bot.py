# if you can read this, this meant you use code from Geez Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez & Ram Team
import traceback
from sys import version as pyver
from pyrogram import __version__ as pyrover
from pyrogram import Client, filters
from pyrogram.errors import MessageDeleteForbidden
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client as client
from rams import CMD_HELP, app
from rams.split.data import Data
from rams.split.inline import cb_wrapper, paginate_help
from rams import ids as users
from config import BOT_VER, BRANCH, CMD_HANDLER as cmd
modules = CMD_HELP
branch = BRANCH

@Client.on_callback_query()
async def _callbacks(_, callback_query: CallbackQuery):
    query = callback_query.data.lower()
    bot_me = await app.get_me()
    if query == "helper":
        buttons = paginate_help(0, CMD_HELP, "helpme")
        await app.edit_inline_text(
            callback_query.inline_message_id,
            Data.text_help_menu,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif query == "close":
        if callback_query.from_user.id not in users:
           return
        await app.edit_inline_text(callback_query.inline_message_id, f"𝗝𝗮𝗿𝗣𝘆𝗿𝗼-𝗠𝗮𝘀𝘁𝗲𝗿 \n"
            "ㅤ⋙ sᴛᴀᴛᴜs : 𝗔𝗸𝘁𝗶𝗳!!! \n"
            f"ㅤㅤ⋙ ᴍᴏᴅᴜʟᴇs: </b> <code>{len(modules)} </code> \n"
            f"ㅤㅤ⋙ ᴠᴇʀsɪ ʙᴏᴛ: {BOT_VER} \n"
            f"ㅤㅤ⋙ ʙʀᴀɴᴄʜ: {branch} \n"
            f"ㅤㅤ⋙ ᴠᴇʀsɪ ᴘʏʀᴏ: </b> <code>{pyrover}</code>\n"
            f"ㅤㅤ⋙ ᴠᴇʀsɪ ᴘʏᴛʜᴏɴ: </b> <code>{pyver.split()[0]}</code>",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="❈ sᴜᴘᴘᴏʀᴛ ❈", url="t.me/jarsuprot"), InlineKeyboardButton(text="❈ ᴏᴡɴᴇʀ ❈", url="https://t.me/utits")], [InlineKeyboardButton(text="❈ ʙᴜᴋᴀ ʟᴀɢɪ ❈", callback_data="helper")]]
            ),
        )
        return
    elif query == "tutup":
        if callback_query.from_user.id not in users:
           return
        await app.edit_inline_text(callback_query.inline_message_id, "⋙ MENUTUP HELP ⋘",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="❈ ʙᴜᴋᴀ ʟᴀɢɪ ❈", callback_data="close")]]
            ),
        )
        return
    elif query == "close_help":
        if callback_query.from_user.id not in users:
           return
        await app.edit_inline_text(
            callback_query.inline_message_id,
            "**⋙ MENU TELAH DITUTUP ⋘**",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="⇕ ʙᴜᴋᴀ ʟᴀɢɪ ⇕", callback_data="reopen")], [InlineKeyboardButton(text="⇕ ᴛᴜᴛᴜᴘ ᴀᴊᴀ ⇕", callback_data="tutup")]]
            ),
        )
        return
    elif query == "closed":
        try:
            await callback_query.message.delete()
        except BaseException:
            pass
        try:
            await callback_query.message.reply_to_message.delete()
        except BaseException:
            pass
    elif query == "make_basic_button":
        try:
            bttn = paginate_help(0, CMD_HELP, "helpme")
            await app.edit_inline_text(
                callback_query.inline_message_id,
                Data.text_help_menu,
                reply_markup=InlineKeyboardMarkup(bttn),
            )
        except Exception as e:
            e = traceback.format_exc()
            print(e, "Callbacks")


@app.on_callback_query(filters.regex("ub_modul_(.*)"))
@cb_wrapper
async def on_plug_in_cb(_, callback_query: CallbackQuery):
    modul_name = callback_query.matches[0].group(1)
    commands: dict = CMD_HELP[modul_name]
    this_command = f"**《✧ {str(modul_name).upper()} ✧》**\n\n"
    for x in commands:
        this_command += f"**ᴄᴍᴅ:\n├⋟** `{str(x)}`\n**└⋟ Fungsi:** `{str(commands[x])}`\n\n"
    this_command += "© @JarSuprot | @uTits"
    bttn = [
        [InlineKeyboardButton(text="⇕ ʙᴀᴄᴋ ⇕", callback_data="reopen"), InlineKeyboardButton(text="⇕ ᴛᴜᴛᴜᴘ ⇕", callback_data="close")],
    ]
    reply_pop_up_alert = (
        this_command
        if this_command is not None
        else f"{module_name} No documentation has been written for the module."
    )
    await app.edit_inline_text(
        callback_query.inline_message_id,
        reply_pop_up_alert,
        reply_markup=InlineKeyboardMarkup(bttn),
    )


@app.on_callback_query(filters.regex("reopen"))
@cb_wrapper
async def reopen_in_cb(_, callback_query: CallbackQuery):
    buttons = paginate_help(0, CMD_HELP, "helpme")
    await app.edit_inline_text(
        callback_query.inline_message_id,
        Data.text_help_menu,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_callback_query(filters.regex("helpme_prev\((.+?)\)"))
@cb_wrapper
async def on_plug_prev_in_cb(_, callback_query: CallbackQuery):
    current_page_number = int(callback_query.matches[0].group(1))
    buttons = paginate_help(current_page_number - 1, CMD_HELP, "helpme")
    await app.edit_inline_text(
        callback_query.inline_message_id,
        Data.text_help_menu,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@app.on_callback_query(filters.regex("helpme_next\((.+?)\)"))
@cb_wrapper
async def on_plug_next_in_cb(_, callback_query: CallbackQuery):
    current_page_number = int(callback_query.matches[0].group(1))
    buttons = paginate_help(current_page_number + 1, CMD_HELP, "helpme")
    await app.edit_inline_text(
        callback_query.inline_message_id,
        Data.text_help_menu,
        reply_markup=InlineKeyboardMarkup(buttons),
    )
# kontol
