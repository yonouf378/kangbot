# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from telethon import events
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.tagall")
async def _(event):
    if event.fwd_from:
        return
    mentions = "@tagall"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()

CMD_HELP.update({
        "tagall": 
        ".tagall \
          \nUsage: Tag all member in ur groups.\n"
    })
