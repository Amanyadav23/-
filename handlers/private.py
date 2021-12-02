
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
😈DÛSRÔ SE JÂLNE WÂLE HÚM NHÎ ÂÚR HÛM PR MÂRNE WÂLE KÂM NHÎ  S๛4๛・SÂHIL๛YÂDÂV๛Ôfficiâl BÔLTÎ PÚBLÎC😈💥💥💖💖💖 @S_4_SAHIL_Official

(@S_4_SAHIL)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰𝗢𝘄𝗻𝗲𝗿❱", url="https://t.me/S_4_SAHIL_Official")
                  ],[
                    InlineKeyboardButton(
                        "❰𝗦𝘂𝗽𝗽𝗼𝗿𝘁🌎❱", url="https://t.me/A_4_AMAN_offixial"
                    ),
                    InlineKeyboardButton(
                        "❰𝗚𝗿𝗼𝘂𝗽🚩❱", url="https://t.me/S_4_SAHIL"
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
      await message.reply_text("""**😈S๛4๛・SÂHIL๛YÂDÂV๛Ôfficiâl 𝐌𝐮𝐬𝐢𝐜'𝐗 𝐎𝐧𝐥𝐢𝐧𝐞\n🌠S๛4๛・SÂHIL๛YÂDÂV๛Ôfficiâl 𝐎𝐩 🥀**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗦𝘂𝗽𝗽𝗼𝗿𝘁❤️", url="https://t.me/A_4_AMAN_Offixial")
                ]
            ]
        )
   )
