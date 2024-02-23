import time
import importlib 
from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from rams import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots, app, ids
from rams.split.misc import create_botlog, git, heroku
from rams.modules import ALL_MODULES



MSG_ON = """
🔥 **JarPyro-Bot Menyala** 🔥
━───────╯⇕╰───────━
🤖 **Userbot Version -** `{}`
⚜️ prefixes: . - ! ? *
⌨️ **Ketik** `{}alive` **untuk Mengecheck Bot**
━───────╮⇕╭───────━
"""

async def main():
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module(f"rams.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            ids.append(bot.me.id)
            await bot.join_chat("daddyystore")
            await bot.join_chat("jarsuprot")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("rams").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("rams").info(f"JarPyro-Bot v{BOT_VER} [🔥 UDAH AKTIF NGENTOT! 🔥]")
    if not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("rams").info("Starting JarPyro-Bot")
    install()
    heroku()
    LOOP.run_until_complete(main())
