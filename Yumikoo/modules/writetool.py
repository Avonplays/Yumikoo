from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from Yumikoo import BOT_NAME, BOT_USERNAME
from Yumikoo import Yumikoo
import requests

@Yumikoo.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    text = (message.reply_to_message.text if message.reply_to_message else
            message.text.split(None, 1)[1])

    m = await message.reply_text("Please wait...,\n\nWriting your text...")

    write = requests.get(f"https://apis.xditya.me/write?text={text}").url

    caption = f"""
    sᴜᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘
    ✨ ᴡʀɪᴛᴛᴇɴ ʙʏ : [{BOT_NAME}](https://t.me/{BOT_USERNAME})
    🥀 ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : {message.from_user.mention}
    """

    await m.delete()
    await message.reply_photo(photo=write, caption=caption)

mod_name = "WʀɪᴛᴇTᴏᴏʟ"

help_message = """
ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴡʜɪᴛᴇ ᴘᴀɢᴇ ᴡɪᴛʜ ᴀ ᴘᴇɴ 🖊

❍ /write <ᴛᴇxᴛ> *:* ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.
"""
