import os
import sys
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from Config import API, APD, STRING1, STRING2, STRING3, SUDO
import asyncio
a = API
b = APD
c = STRING1
d = STRING2
e = STRING3
f = "1754679580:AAEfvJCADfB4A7PJ7nPKr8WcJK5cvQabUyk"
idk = TelegramClient(StringSession(c), a, b)
bro = TelegramClient(StringSession(d), a, b)
fuck = TelegramClient(StringSession(e), a, b)
idk.start(bot_token = f)
bro.start(bot_token = f)
fuck.start(bot_token = f)
print("Booting Up The System")


@idk.on(events.NewMessage(incoming=True, pattern=".spam"))
@bro.on(events.NewMessage(incoming=True, pattern=".spam"))
@fuck.on(events.NewMessage(incoming=True, pattern=".spam"))
async def spam(e):
    if e.sender_id in SUDO:
        if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
            idk = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
            message = str(idk[1])
            counter = int(idk[0])
            await asyncio.wait([e.respond(message) for i in range(counter)])
            await e.delete()



@idk.on(events.NewMessage(incoming=True, pattern=".dspam"))
@bro.on(events.NewMessage(incoming=True, pattern=".dspam"))
@fuck.on(events.NewMessage(incoming=True, pattern=".dspam"))
async def dspam(e):
    if e.sender_id in SUDO:
        input_str = "".join(e.text.split(maxsplit=1)[1:])
        spamDelay = float(input_str.split(" ", 2)[0])
        counter = int(input_str.split(" ", 2)[1])
        spam_message = str(input_str.split(" ", 2)[2])
        for _ in range(counter):
            await e.respond(spam_message)
            await asyncio.sleep(spamDelay)


@idk.on(events.NewMessage(incoming=True, pattern=".mspam"))
@bro.on(events.NewMessage(incoming=True, pattern=".mspam"))
@fuck.on(events.NewMessage(incoming=True, pattern=".mspam"))
async def mspam(e):
    if e.sender_id in SUDO:
        input_str = "".join(e.text.split(maxsplit=1)[1:])
        counter = int(input_str.split(" ", 2)[0])
        reply_message = await e.get_reply_message()
        bro = reply_message.media
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, bro)



@idk.on(events.NewMessage(incoming=True, pattern=".ping"))
@bro.on(events.NewMessage(incoming=True, pattern=".ping"))
@fuck.on(events.NewMessage(incoming=True, pattern=".ping"))
async def ping(e):
    if e.sender_id in SUDO:
        start = datetime.now()
        xxx = "PINGING..."
        event = await e.reply(xxx, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"**PING PONG**: **{ms}**\n**BELLA CIAO**\n**TERA BAAP HU**")




@idk.on(events.NewMessage(incoming=True, pattern=".restart"))
@bro.on(events.NewMessage(incoming=True, pattern=".restart"))
@fuck.on(events.NewMessage(incoming=True, pattern=".restart"))
async def restart(e):
    if e.sender_id in SUDO:
        text = "RESTARTED, CHECK ME AFTER 2 MINUTES"
        await e.reply(text, parse_mode=None, link_preview=None )
        await idk.disconnect()
        await bro.disconnect()
        await fuck.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

@idk.on(events.NewMessage(incoming=True, pattern=".help"))
@bro.on(events.NewMessage(incoming=True, pattern=".help"))
@fuck.on(events.NewMessage(incoming=True, pattern=".help"))
async def help(e):
    if e.sender_id in SUDO:
       text = "Available Commands\n.spam\n.dspam\n.mspam\n.restart\n.ping"
       await e.reply(text, parse_mode=None, link_preview=None )
 
print("started sucessfully")
bro.run_until_disconnected()
fuck.run_until_disconnected()
idk.run_until_disconnected()
