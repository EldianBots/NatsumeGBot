# This module is made by https://github.com/SOME-1HING/

"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# You are free to use this module. But don't delete this commented text. Thank you.

from Shikimori import dispatcher
from telegram import ParseMode
import Shikimori.modules.sql.chatbot_sql as sql
from telegram.ext import Filters, MessageHandler
import time

HENTAI_IMG = "https://telegra.ph/file/6d738a1d8ccd71a3813bd.jpg"

def hentai(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    chat_id = update.effective_chat.id
    is_kuki = sql.is_kuki(chat_id)
    if not is_kuki:
        return
    try:
        reply = """
__Remember Son , 3D is temporary 2D is eternal 
                                        ~ *Natsume*__
                                               """
        message.reply_photo( HENTAI_IMG, reply)

    except:
        reply = """
__Remember Son , 3D is temporary 2D is eternal 
                                        ~ *Natsume*__
                                               """
        message.reply_text(reply)

    time.sleep(5)


def natsume(update, context):
    message = update.effective_message
    user1 = message.from_user.first_name
    chat_id = update.effective_chat.id
    is_kuki = sql.is_kuki(chat_id)
    if not is_kuki:
        return
    reply = f"Ah stop calling me.. let me read douji- I mean biology in peace :'("
    message.reply_text(reply)
    
    time.sleep(5)

GDMORNING_HANDLER = MessageHandler(
    Filters.regex("(?i)(good morning|natsume)"), natsume, friendly="natsume", run_async = True
)
GDNIGHT_HANDLER = MessageHandler(
    Filters.regex("(?i)(hentai)"), hentai, friendly="hentai", run_async = True
)

dispatcher.add_handler(GDMORNING_HANDLER)
dispatcher.add_handler(GDNIGHT_HANDLER)