"""
Created by @Jisan7509
Modified @Akarata
#credit @GulfysHalfyyyy
"""
import asyncio

from ..utils import admin_cmd, edit_or_reply, sudo_cmd
from . import mention

# ==================================================================

C = (
    "\n......................................../´¯/) "
    "\n......................................,/¯../ "
    "\n...................................../..../ "
    "\n..................................../´.¯/"
    "\n..................................../´¯/"
    "\n..................................,/¯../ "
    "\n................................../..../ "
    "\n................................./´¯./"
    "\n................................/´¯./"
    "\n..............................,/¯../ "
    "\n............................./..../ "
    "\n............................/´¯/"
    "\n........................../´¯./"
    "\n........................,/¯../ "
    "\n......................./..../ "
    "\n....................../´¯/"
    "\n....................,/¯../ "
    "\n.................../..../ "
    "\n............./´¯/'...'/´¯¯`·¸ "
    "\n........../'/.../..../......./¨¯\ "
    "\n........('(...´...´.... ¯~/'...') "
    "\n.........\.................'...../ "
    "\n..........''...\.......... _.·´ "
    "\n............\..............( "
    "\n..............\.............\..."
)


GAMBAR_TITIT = """
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆       🍆🍆
"""

# =======================================================


@bot.on(admin_cmd(pattern=r"muth$"))
@bot.on(sudo_cmd(pattern="muth$", allow_sudo=True))
async def kakashi(bsdk):
    if bsdk.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(50)
    bsdk = await edit_or_reply(bsdk, f"**Ahhh pengin coli......**💦💦...")
    animation_chars = [
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8===✊️D💦",
        "8==✊️=D💦💦",
        "Croooottt💦💦💦",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await bsdk.edit(animation_chars[i % 10])


@bot.on(admin_cmd(pattern=r"ohnoo$"))
@bot.on(sudo_cmd(pattern="ohnoo$", allow_sudo=True))
async def kakashi(bsdk):
    if bsdk.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(11)
    bsdk = await edit_or_reply(bsdk, f"**Ahhh lagi sange **💦💦...")
    animation_chars = [
        "**Ohhh Sayang..**😈",
        "__**Ohh Yeaah..**__\n\n 😈\n  |\  \n  |  \   \n 8=👊-D\n  |   \         \n 👟 👟       😲",
        "__**Ohh ohhh..**__\n\n 😈\n  |\  \n  |  \   \n  8=👊-D\n  |   \         \n 👟 👟       😲",
        "__**Ohh.. **__\n\n 😈\n  |\  \n  |  \   \n 8=👊-D\n  |   \         \n 👟 👟       😲",
        "__**Ohh Sayang..**__\n\n 😈\n  |\  \n  |  \   \n8=👊-D💦\n  |   \         \n 👟 👟       😲",
        "__**Yeaah..**__\n\n 😣\n  |\  \n  |  \   \n 8=👊-D💦\n  |   \         \n 👟 👟       😲",
        "__**Yeaah Yaaah..**__\n\n 😣\n  |\  \n  |  \   \n  8=👊-D💦\n  |   \         💦\n 👟 👟       😲",
        "__**Yaah Sayang..**__\n\n 😘\n  |\  \n  |  \   \n 8=👊-D💦\n  |   \         💦\n 👟 👟       🤤",
        "__**Ohhh..**__\n\n 😍\n  |\  \n  |  \   \n8=👊-D💦\n  |   \         💦\n 👟 👟       🤤",
        "__**Cinta kamu..**__\n\n 😘\n  |\  \n  |  \   \n 8=👊-D💦\n  |   \         \n 👟 👟       🤤",
        "__**Cinta kamu sayang**__\n\n 😍\n  |\  \n  |  \   \n 8=👊-D\n  |   \         \n 👟 👟       🤤",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await bsdk.edit(animation_chars[i % 11])


@bot.on(admin_cmd(pattern=r"lovestory$"))
@bot.on(sudo_cmd(pattern="lovestory$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 3
    animation_ttl = range(14)
    event = await edit_or_reply(event, "Mulai suatu....")
    animation_chars = [
        "1 ❤️ kisah cinta",
        "  😐             😕 \n/👕\         <👗\ \n 👖               /|",
        "  😉          😳 \n/👕\       /👗\ \n  👖            /|",
        "  😚            😒 \n/👕\         <👗> \n  👖             /|",
        "  😍         ☺️ \n/👕\      /👗\ \n  👖          /|",
        "  😍          😍 \n/👕\       /👗\ \n  👖           /|",
        "  😘   😊 \n /👕\/👗\ \n   👖   /|",
        " 😳  😁 \n /|\ /👙\ \n /     / |",
        "😈    /😰\ \n<|\      👙 \n /🍆    / |",
        "😅 \n/(),✊😮 \n /\         _/\\/|",
        "😎 \n/\\_,__😫 \n  //    //       \\",
        "😖 \n/\\_,💦_😋  \n  //         //        \\",
        "  😭      ☺️ \n  /|\   /(👶)\ \n  /!\   / \ ",
        "Tamat 😂...",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])


@bot.on(admin_cmd(pattern=r"ohyaah$"))
@bot.on(sudo_cmd(pattern="ohyaah$", allow_sudo=True))
async def kakashi(baby):
    if event.fwd_from:
        return
    await edit_or_reply(
        baby,
        "**💪💪Ohhh Yeeah Baby**...\n\n"
        "／ イ  ..........(((ヽ   \n"
        "(  ﾉ       ￣—--＼    \n"
        "| (＼  (\🎩/)   ｜    )  \n"
        "ヽ ヽ` ( ͡° ͜ʖ ͡°) _ノ    /  \n"
        " ＼ | ⌒Ｙ⌒ /  /  \n"
        "   ｜ヽ  ｜  ﾉ ／  \n"
        "     ＼トー仝ーイ \n"
        "        ｜ ミ土彡/ \n"
        "         ) \      °   /  \n"
        "        (     \🌿 /  \n"
        "         /       /ѼΞΞΞΞΞΞΞD💨💦\n"
        "      /  /     /      \ \   \  \n"
        "      ( (    ).           ) ).  ) \n"
        "     (      ).            ( |    | \n"
        "      |    /                \    |\n"
        "      👞.                  👞",
    )


@bot.on(admin_cmd(pattern=r"foff$"))
@bot.on(sudo_cmd(pattern="foff$", allow_sudo=True))
async def bluedevilfooku(fooku):
    await edit_or_reply(
        fooku,
        ".                       /¯ )\n"
        "                      /¯  /\n"
        "                    /    /\n"
        "              /´¯/'   '/´¯¯`•¸\n"
        "          /'/   /    /       /¨¯\ \n"
        "        ('(   (   (   (  ¯~/'  ')\n"
        "         \                        /\n"
        "          \                _.•´\n"
        "            \              (\n"
        "              \  \n"
        "Ikan hiu makan tomat\n"
        "Goblog 🖕😂\n",
    )


@bot.on(admin_cmd(pattern=r"mf$"))
@bot.on(sudo_cmd(pattern="mf$", allow_sudo=True))
async def kakashi(mf):
    await edit_or_reply(mf, C)


@bot.on(admin_cmd(pattern=r"sporn$"))
@bot.on(sudo_cmd(pattern="sporn$", allow_sudo=True))
async def kakashi(pornhub):
    await edit_or_reply(
        pornhub,
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣧⣤⣤⠀⢠⣤⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿   ⠸⠿⠇⢸⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⠿⠷⣤⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⡏⢀⣤⣤⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⡇⠘⠿⠿⠃⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⡿⠦⠤⠤⠴⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣧⣤⣤⣄⡀   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣇⣀⣀⣀⡀   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠟⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣧⣤⣤⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠉⠉⢉⣉⣉⣉⣉⣉⣉⡉⠉⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⠻⠿⠿⠿⣿⡿⠿⠇⠀⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⣤⣤⣤⣤⣾⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⢉⣩⣭⣭⣭⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⣿⡟⠋⠉⠋⠁⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⣾⣿⣶⣶⣶⡆⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⣶⣶⣶⣶⣶⣶⣶⡆⠀⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⣾⣏⠀⠀⣹⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠀⠀⠘⠿⠿⠿⠟⠃⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n",
    )


@bot.on(admin_cmd(pattern=r"spika$"))
@bot.on(sudo_cmd(pattern="spika$", allow_sudo=True))
async def kakashi(pikachu):
    await edit_or_reply(
        pikachu,
        "⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿\n"
        "⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿\n"
        "⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠻⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿\n"
        "⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿\n"
        "⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠸⣿⣿⣿\n"
        "⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠀⠤⠄⠀⠀⠉⠁⠀⠀⠀⢿⣿⣿\n"
        "⣿⣿⣿⣿⠀⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠠⣿⣿⣷⠀⣿⣿\n"
        "⣿⣿⣿⣿⡀⠀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠉⠉⠁⠀⣿⣿\n"
        "⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿\n"
        "⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿\n"
        "⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿\n"
        "⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿🅼🅰️ 🅺🅸 🅲🅷🆄⢸⣿⣿⣿⣿⣿⣿\n"
        "🅿️🅸🅺🅰️ 🅿️🅸🅺🅰️ 🅿️🅸🅺🅰️🅲🅷🆄\n",
    )


@bot.on(admin_cmd(pattern=r"sxx$"))
@bot.on(sudo_cmd(pattern="sxx$", allow_sudo=True))
async def kakashi(saxy):
    await edit_or_reply(
        saxy,
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀\n"
        "⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀\n"
        "⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀\n"
        "⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀\n"
        "⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦\n"
        "⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟\n"
        "⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
        "⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇\n"
        "⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀\n"
        "⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀\n"
        "⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀\n"
        "⠄⠄⠄⠄⠄⠄⣠⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡄⠄⠄⠄\n"
        "⠄⠄⣀⣤⣴⣾⣿⣷⣭⣭⣭⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⠄\n"
        "⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣧⠄⠄\n"
        "⠄⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢻⣿⣿⡄⠄\n"
        "⠄⢸⣿⣮⣿⣿⣿⣿⣿⣿⣿⡟⢹⣿⣿⣿⡟⢛⢻⣷⢻⣿⣧⠄\n"
        "⠄⠄⣿⡏⣿⡟⡛⢻⣿⣿⣿⣿⠸⣿⣿⣿⣷⣬⣼⣿⢸⣿⣿⠄\n"
        "⠄⠄⣿⣧⢿⣧⣥⣾⣿⣿⣿⡟⣴⣝⠿⣿⣿⣿⠿⣫⣾⣿⣿⡆\n"
        "⠄⠄⢸⣿⣮⡻⠿⣿⠿⣟⣫⣾⣿⣿⣿⣷⣶⣾⣿⡏⣿⣿⣿⡇\n"
        "⠄⠄⢸⣿⣿⣿⡇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⡇\n"
        "⠄⠄⢸⣿⣿⣿⡇⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⠄\n"
        "⠄⠄⣼⣿⣿⣿⢃⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⡇⠄\n"
        "⠄⠄⠸⣿⣿⢣⢶⣟⣿⣖⣿⣷⣻⣮⡿⣽⣿⣻⣖⣶⣤⣭⡉⠄\n"
        "⠄⠄⠄⢹⠣⣛⣣⣭⣁⡛⠻⢽⣿⣿⣿⣿⢻⣿⣿⣿⣽⡧⡄⠄\n"
        "⠄⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣶⣌⡛⢿⣽⢘⣿⣷⣿⡻⠏⣛⣀\n"
        "⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠙⡅⣿⠚⣡⣴⣿⣿⡆\n"
        "⠄⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⣱⣾⣿⣿⣿⣿⣿\n"
        "⠄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿\n"
        "⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠣⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠑⣿⣮⣝⣛⠿⠿⣿⣿⣿\n"
        "⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⡟\n"
        "⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠄⠄⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⡟\n"
        "⣸⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠸⣿⣿⣿⣿⡿⢟⣣\n"
        "ɮǟȶǟʊ ȶɦǟʀӄɨօ ӄʏǟ ɦǟǟʟ ,ӄɛֆǟ ʟǟɢǟ\n",
    )


@bot.on(admin_cmd(pattern="sdick (.*)"))
@bot.on(sudo_cmd(pattern="sdick  (.*)", allow_sudo=True))
async def kakashi(dicksay):
    text = dicksay.pattern_match.group(1)
    await edit_or_reply(
        dicksay,
        f"**{mention} ➥ {text} .\n**"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠲⢄\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠁⠀⠀⠀⠀⢱\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠀⠀⠀⣸\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠀⠀⠀⠀⢀⡠⠖⠁\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⠁⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣯⣿⣿⣿⣿⣿⠇⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⣻⣿⣿⣿⣿⣯⠏⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⣠⠾⣽⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⣴⣻⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⣠⢾⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⣼⣷⣿⣿⣿⣿⣿⣿⣟⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⢸⢿⣿⣿⣿⣿⣿⣿⣿⣯⣻⡟⡆⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠸⣿⣿⣿⣿⣿⣿⣿⣿⣹⣿⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠹⣟⣿⣿⣿⣿⡿⣷⡿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠈⠛⠯⣿⡯⠟⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n",
    )


@bot.on(admin_cmd(outgoing=True, pattern=r"^\.(?:penis|dick)\s?(.)?"))
@bot.on(sudo_cmd(outgoing=True, pattern=r"^\.(?:penis|dick)\s?(.)?", allow_sudo=True))
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)
    titid = GAMBAR_TITIT
    if emoji:
        titid = titid.replace("🍆", emoji)
    await e.edit(titid)
