
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 🎶 𝐁𝐨𝐭 \n𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 🥀 𝐕𝐩𝐬 💫𝐒𝐞𝐫𝐯𝐞𝐫 🌎 \n𝐅𝐞𝐞𝐥 ❤️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜 😎🤟 \n⭐𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 A๛4๛・AMAN XD ༆ YADAV JI ༻⍟↳𝐀𝐂𝐅 𝐅𝐈𝐆𝐇𝐓𝐄𝐑↰⍟

](https://t.me/Its_Hexor)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰𝗢𝘄𝗻𝗲𝗿❱", url="https://t.me/A_4_AMAN_offixial")
                  ],[
                    InlineKeyboardButton(
                        "❰𝗦𝘂𝗽𝗽𝗼𝗿𝘁🌎❱", url="https://t.me/A_4_AMAN_offixial"
                    ),
                    InlineKeyboardButton(
                        "❰𝗚𝗿𝗼𝘂𝗽🚩❱", url="https://t.me/A_4_AMAN_offixial"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❰𝗖𝗼𝗺𝗺𝗮𝗱𝘀🥀❱", url="https://telegra.ph/%EA%9C%B1%E1%B4%8D%E1%B4%8F%E1%B4%8B%E1%B4%87%CA%80-%E1%B4%8D%E1%B4%9C%EA%9C%B1%C9%AA%E1%B4%84-%CA%99%E1%B4%8F%E1%B4%9B-%E1%B4%84%E1%B4%8F%E1%B4%8D%E1%B4%8D%E1%B4%80%C9%B4%E1%B4%85%EA%9C%B1-08-29"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("Esport") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Acf 𝐌𝐮𝐬𝐢𝐜'𝐗 𝐎𝐧𝐥𝐢𝐧𝐞\n🌠ACF_𝐎𝐩 🥀**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗦𝘂𝗽𝗽𝗼𝗿𝘁❤️", url="https://t.me/ACF_FIGHTERR")
                ]
            ]
        )
   )
