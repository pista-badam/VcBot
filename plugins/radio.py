from pyrogram import Client, filters
from pyrogram.types import Message
from utils.vc import mp, RADIO
from config import Config
from helpers.decs import authorized_users_only
STREAM_URL=Config.STREAM_URL
ADMINS=authorized_users_only

@Client.on_message(filters.command("radio") & filters.user(ADMINS))
async def radio(client, message: Message):
    if 1 in RADIO:
        await message.reply_text("**Radio is already playing. Do /stopradio to stop existing radio and Try Again!**")
        return
    await mp.start_radio()
    await message.reply_text(f"**Radio Started :**  <code>{STREAM_URL}</code>")

@Client.on_message(filters.command("stopradio") & filters.user(ADMINS))
async def stop(_, message: Message):
    if 0 in RADIO:
        await message.reply_text("**Radio is already disconnected. There's nothing to stop!**")
        return
    await mp.stop_radio()
    await message.reply_text("**Radio Ended Successfully!**")
