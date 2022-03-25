# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2021 TeamUltroid for autobot
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#
# autopilot by @kenkan
#
""" Userbot start point """


import sys
from importlib import import_module
from platform import python_version

import requests
from pytgcalls import __version__ as pytgcalls
from pytgcalls import idle
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditPhotoRequest,
)
from telethon.tl.types import ChatAdminRights
from telethon import version


from userbot import BOT_TOKEN, BOT_USERNAME, BOT_VER, BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import DEVS, LOGS, bot, call_py
from userbot.modules import ALL_MODULES
from userbot.utils import autobot, autopilot, checking, waiting

try:
    bot.start()
    call_py.start()
    user = bot.get_me()
    name = user.first_name
    uid = user.id
    blacklistbdrl = requests.get(
        "https://raw.githubusercontent.com/Yansaii/Reforestation/master/bdrlblacklist.json"
    ).json()
    if user.id in blacklistbdrl:
        LOGS.warning(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOTnya GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nCredits: @mrismanaziz"
        )
        sys.exit(1)
    if 1883126074 not in DEVS:
        LOGS.warning(
            f"EOL\nBᴅʀʟ-Usᴇʀʙᴏᴛ v{BOT_VER}, Copyright © 2021-2022 𝙰𝚈𝙸𝙸𝙽𝚇𝙳• <https://github.com/Yansaii>"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(f"Python Version - {python_version()}")
LOGS.info(f"Telethon Version - {version.__version__}")
LOGS.info(f"PyTgCalls Version - {pytgcalls.__version__}")

LOGS.info(
    f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
)

LOGS.info(
    f"Jika {name} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/pantekyks"
)

LOGS.info(f"Bdrl-Userbot ⚙️ V{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")


if not BOTLOG_CHATID:
    LOGS.info(
        "BOTLOG_CHATID Vars tidak terisi, Memulai Membuat Grup Otomatis..."
    )
    bot.loop.run_until_complete(autopilot())

async def bdrl_userbot_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"✪ **Bᴅʀʟ-Usᴇʀʙᴏᴛ Berhasil Di Aktifkan** ✪\n━━\n➠ **Userbot Version -** `{BOT_VER}`\n➠ **Ketik** `{cmd}alive` **untuk Mengecheck Bot**\n━━",
            )

    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(JoinChannelRequest("@RuangTerbukaa"))
    except BaseException:
        pass
    try:
        rights = ChatAdminRights(
            add_admins=False,
            invite_users=True,
            change_info=True,
            ban_users=True,
            delete_messages=True,
            pin_messages=True,
            anonymous=False,
            manage_call=True,
        )
        await bot(EditAdminRequest(int(BOTLOG_CHATID), BOT_USERNAME, rights, "Assistant"))
        logo = "userbot/resources/logo.jpg"
        await bot(EditPhotoRequest(BOTLOG_CHATID, await bot.upload_file(logo)))
    except BaseException:
        pass


bot.loop.run_until_complete(waiting())
bot.loop.run_until_complete(checking())
bot.loop.run_until_complete(bdrl_userbot_on())
if not BOT_TOKEN:
    bot.loop.run_until_complete(autobot())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
