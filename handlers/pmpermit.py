from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hello This Is My Music Assistance Id Dont Spam Owner 👿@S_4_SAHIL_Official 👿 😈#𝐒𝐀𝐇𝐈𝐋 𝐈𝐅 𝐘𝐎𝐔 𝐓𝐇𝐈𝐍𝐊 𝐘𝐎𝐔 𝐀𝐑𝐄 𝐁𝐀𝐃 𝐓𝐇𝐀𝐍 𝐈 𝐀𝐌 𝐘𝐎𝐔𝐑 𝐃𝐀𝐃💥😈 @S_4_SAHIL_Hacker")
  return                        
