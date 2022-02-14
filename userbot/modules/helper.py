""" Userbot module for other small commands. """
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import edit_or_reply, bdrl_cmd


@bdrl_cmd(pattern="ihelp$")
async def usit(event):
    await edit_or_reply(
        event,
        f"**Hai {owner} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        f"★ **GroupSupport :** [Grup Support](t.me/BdrlSupporrt)\n"
        f"★ **Channel :** [Channel](t.me/RuangTerbukaa)\n"
        f"★ **OwnerRepo :** [Bdrl](t.me/Bukan_Bdrl)\n"
        f"★ **Repo :** [Bdrl-Ubot](https://github.com/Yansaii/Bdrl-Ubot)\n",
    )


@bdrl_cmd(pattern="listvar$")
async def var(event):
    await edit_or_reply(
        event,
        "**Daftar Lengkap Vars Dari Bdrl-Ubot:** [KLIK DISINI](https://telegra.ph/List-Variabel-Heroku-untuk-Man-Userbot-09-22)",
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  •  **Syntax :** `{cmd}ihelp`\
        \n  •  **Function : **Bantuan Untuk Bdrl-Ubot.\
        \n\n  •  **Syntax :** `{cmd}listvar`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Syntax :** `{cmd}repo`\
        \n  •  **Function : **Melihat Repository Bdrl-Ubot.\
        \n\n  •  **Syntax :** `{cmd}string`\
        \n  •  **Function : **Link untuk mengambil String Bdrl-Ubot.\
    "
    }
)
