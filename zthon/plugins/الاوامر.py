# ZedThon - zthon
# Copyright (C) 2022 ZedThon . All Rights Reserved
#< https://t.me/ZedThon >
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/master/LICENSE/>.

import os
import aiohttp
import requests
import re
import time
import sys
import asyncio
from validators.url import url
from subprocess import run as runapp
from datetime import datetime
from pySmartDL import SmartDL
from pathlib import Path
from platform import python_version
from telethon import Button, events ,types, version
from telethon.events import CallbackQuery, InlineQuery
from telethon.utils import get_display_name
from telethon.errors import QueryIdInvalidError
from telethon.tl.types import InputMessagesFilterDocument
from zthon import StartTime, zedub, zedversion
from ..Config import Config
from ..core import check_owner, pool
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..helpers.utils import reply_id, get_user_from_event, _format
from ..helpers.tools import media_type
from . import media_type, progress
from ..utils import load_module, remove_plugin
from ..sql_helper.global_collection import add_to_collectionlist, del_keyword_collectionlist, get_collectionlist_items
from . import SUDO_LIST, edit_delete, edit_or_reply, reply_id, BOTLOG, BOTLOG_CHATID, HEROKU_APP, mention


LOGS = logging.getLogger(os.path.basename(__name__))
LOGS1 = logging.getLogger(__name__)
ZORDR = gvarstatus("Z_ORDR") or "الاوامر"
ZLORDR = gvarstatus("Z_LORDR") or "الاوامر"
ppath = os.path.join(os.getcwd(), "temp", "githubuser.jpg")
GIT_TEMP_DIR = "./temp/"
cmdhd = Config.COMMAND_HAND_LER
DELETE_TIMEOUT = 1
USERID = bot.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME# ZedThon - zthon
# Copyright (C) 2022 ZedThon . All Rights Reserved
#< https://t.me/ZedThon >
# This file is a part of < https://github.com/Zed-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Zed-Thon/ZelZal/blob/master/LICENSE/>.

import os
import aiohttp
import requests
import re
import time
import sys
import asyncio
from validators.url import url
from subprocess import run as runapp
from datetime import datetime
from pySmartDL import SmartDL
from pathlib import Path
from platform import python_version
from telethon import Button, events ,types, version
from telethon.events import CallbackQuery, InlineQuery
from telethon.utils import get_display_name
from telethon.errors import QueryIdInvalidError
from telethon.tl.types import InputMessagesFilterDocument
from zthon import StartTime, zedub, zedversion
from ..Config import Config
from ..core import check_owner, pool
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..helpers.utils import reply_id, get_user_from_event, _format
from ..helpers.tools import media_type
from . import media_type, progress
from ..utils import load_module, remove_plugin
from ..sql_helper.global_collection import add_to_collectionlist, del_keyword_collectionlist, get_collectionlist_items
from . import SUDO_LIST, edit_delete, edit_or_reply, reply_id, BOTLOG, BOTLOG_CHATID, HEROKU_APP, mention


LOGS = logging.getLogger(os.path.basename(__name__))
LOGS1 = logging.getLogger(__name__)
ZORDR = gvarstatus("Z_ORDR") or "الاوامر"
ZLORDR = gvarstatus("Z_LORDR") or "الاوامر"
ppath = os.path.join(os.getcwd(), "temp", "githubuser.jpg")
GIT_TEMP_DIR = "./temp/"
cmdhd = Config.COMMAND_HAND_LER
DELETE_TIMEOUT = 1
USERID = bot.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")
Malath = f"**🖥┊لـوحـة اوامـر 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 الشفـافـه **\n**🧑🏻‍💻┊المستخـدم ↶** {mention} \n\n**•❐• قـائمــة الاوامــر الـعـامــه :**\n\n**•❶• اوامــر الـبحـث والـتحميـل **\n**•❷• اوامــر الـبـوت **\n**•❸• اوامــر الـوقـتـي **\n**•❹• اوامــر الـكــروب¹ **\n**•❺• اوامــر الـكــروب² **\n**•❻• اوامــر الـحسـاب **\n**•❼• اوامــر الميـديـا والـصيــغ **\n\n**•❐• لعـرض بقيـة الاوامـر اضغـط زر التـالي ⇒**\n**•❐• لعـرض الاوامـر مع الوصـف استخـدم امـر** `.الأوامر` "
Malotha = f"**🖥┊يتبـع لـوحـة اوامـر 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 الشفـافـه **\n**🧑🏻‍💻┊المستخـدم ↶** {mention} \n\n**•❐• يتبــع قـائمــة الاوامــر الـعـامــه :**\n\n**•❽• اوامــر الـفــارات **\n**•❾• اوامــر الخـدمــات العـامــه **\n**•❿• اوامــر الالعــاب **\n**•⓫• اوامــر الـتســليــه**\n**•⓬• اوامــر التحشيـش**\n**•⓭• اوامــر الستـوريات**\n**•⓮• اوامــر الآفتــارات**\n\n**•❐• للرجـوع للوحـه السـابقـه اضغـط زر السـابق ⇐**\n**•❐• لعـرض الاوامـر مع الوصـف استخـدم امـر** `.الأوامر` "
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Channels = f"**•❐• مـرحبــاً عـزيـزي  {mention} **\n**•❐• اليـك مجمـوعــة قنـوات العابث ↵ 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 ♥️🦾**\n\n**•❐• استـخـدم الازرار بالاسفــل↓**"
Zelzal = f"**•◈• اصــدار الســورس ⤽ 7.7**  \n**•◈• المستخــدم ⤽**  {mention}  \n**•◈• وقــت التشغيــل ⤽  {TM}  **\n**•◈• البــوت المســاعـد ⤽  {TG_BOT} **\n**•◈• قنــاة الســورس ⤽  @I_R_S_A_I **"



#لـوحــة الاوامــر - حقــوق عابث
@zedub.tgbot.on(events.InlineQuery)
@check_owner
async def zed_handler(event):
    builder = event.builder
    result = None
    query = event.text
    await zedub.get_me()
    if query.startswith("الاوامر") and event.query.user_id == zedub.uid:
        ZEDPIC = gvarstatus("CMD_PIC") or "https://telegra.ph/file/1035d07280ee0ec9fc29b.mp4"
        buttons = [[Button.inline("❶", data="ahmed1"), Button.inline("❷", data="ahmed2"), Button.inline("❸", data="ahmed3"), Button.inline("❹", data="ahmed4"),],[Button.inline("❺", data="ahmed5"), Button.inline("❻", data="ahmed6"), Button.inline("❼", data="ahmed7"), Button.inline("⇒", data="back1"),]]
        if ZEDPIC and ZEDPIC.endswith((".jpg", ".png")):
            result = builder.photo(ZEDPIC,text=Malath, buttons=buttons, link_preview=True)
        elif ZEDPIC and ZEDPIC.endswith((".gif", ".mp4")):
            result = builder.document(ZEDPIC,title="zedub", text=Malath ,buttons=buttons, link_preview=True)
        else:
            result = builder.article(title="zedub",text=Malath,buttons=buttons,link_preview=True)
        await event.answer([result] if result else None)
@zedub.zed_cmd(pattern="الاوامر(?: |$)(.*)")
async def repozedub(event):
    if event.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await event.client.inline_query(TG_BOT, "الاوامر")
    await response[0].click(event.chat_id)
    await event.delete()


@zedub.zed_cmd(pattern=f"الأوامر(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, f"𓆰 [𝗦𝗢𝗨𝗥𝗖𝗘 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - قائمــة الاوامــر العــامــه](t.me/I_R_S_A_I) 𓆪\n◐━─━─━─━─**𝙕𝞝𝘿**─━─━─━─━◐\n**⌔ مـرحبـاً عـزيـزي {mention} اضغـط ع الامـر لـ النسـخ**\n**⌔ ضـع نقطه (.) بداية كل امـر :**\n\n `.م1`**   ➪ اوامـر البحـث والتحميــل** \n\n `.م2`**   ➪ اوامـر البــوت**\n\n `.م3`**   ➪ اوامـر الـوقتــي**\n\n `.م4`**   ➪ اوامـر المجمــوعــه¹**\n\n `.م5`**   ➪ اوامـر المجمــوعــه²**\n\n `.م6`**   ➪ اوامـر الحســاب**\n\n `.م7`**   ➪ اوامـر الميـديـا والصيــغ**\n\n `.م8`**   ➪ اوامـر الفــارات**\n\n `.م9`**   ➪ اوامـر الـخدمــات**\n\n `.م10`** ➪ اوامـر الالـعــاب**\n\n `.م11`** ➪ اوامـر التســليـه**\n\n `.م12`** ➪ اوامـر التحشيـش**\n\n `.م13`** ➪ اوامـر الستـوريات**\n\n `.م14`** ➪ اوامـر الآفتــارات**\n\n ◐━─━─━─━─*𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪**─━─━─━─━◐\n 𓆩 [𝗦𝗢𝗨𝗥𝗖𝗘 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - قنـاة السـورس](t.me/I_R_S_A_I) 𓆪")

@zedub.zed_cmd(pattern="م1(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر البحـث والتحميــل](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.بحث` + اسـم الاغنيـه\n**لـ تحميـل الاغـاني مـن يوتيـوب بدقه خفيفـه وتحميـل اسـرع**\n\n**⎞𝟐⎝** `.اغنيه` + اسـم الاغنيـه\n**لـ تحميـل الاغـاني مـن اليـوتيـوب بدقه عاليـه**\n\n**⎞𝟑⎝** `.فيديو` + اسـم المقطـع\n**لـ تحميـل مقـاطع الفيديـو مـن يوتيـوب**\n\n**⎞𝟒⎝** `.تحميل صوت` + رابـط\n**لـ تحميـل المقـاطع الصـوتيه من يوتيـوب عبر الرابـط**\n\n**⎞𝟓⎝** `.تحميل فيديو` + رابـط\n**لـ تحميـل مقـاطع الفيـديـو من يوتيـوب عبر الرابـط**\n\n**⎞𝟔⎝** `.يوتيوب`+ كلمـه\n**لـ البحث عـن روابـط بالكلمـه ع يوتيـوب **\n\n**⎞𝟕⎝** `.انستا` + رابـط\n**لـ تحميـل الصـور ومقـاطع الفيديـو مـن الانستجـرام**\n\n**⎞𝟖⎝** `.صور` + كلمـه\n**لـ تحميـل الصـور من جوجـل**\n\n**⎞𝟗⎝** `.متحركه` + كلمـه\n**لـ تحميـل صـور متحركـه من جـوجـل..**\n\n**⎞𝟏𝟎⎝** `.تيك` + رابـط او بالـرد ع رابـط\n**لـ تحميـل مقاطـع الفيديـو من تيك توك**\n\n**⎞𝟏𝟏⎝** `.لايكي` + رابـط\n**لـ تحميـل مقاطـع الفيديـو من لايكـي**\n\n**⎞𝟏𝟐⎝** `.فيسبوك` + رابـط او `.فيس` بالـرد ع رابـط\n**لـ تحميـل مقاطـع الفيديـو مـن فيس بـوك**\n\n**⎞𝟏𝟑⎝** `.تويتر` + رابـط\n**لـ تحميـل مقاطـع الفيديـو من تويتـر**\n\n**⎞𝟏𝟒⎝** `.بن` + رابـط\n**لـ تحميـل مقاطـع الفيديـو من بنتـرست**\n\n**⎞𝟏𝟓⎝** `.سناب` + رابـط\n**⦇.سناب + رابـط⦈ لـ تحميـل مقاطـع الفيديـو من سناب شـات**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪](t.me/I_R_S_A_I) 𓆪")    
@zedub.zed_cmd(pattern="م2(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر البـــوت 🦾🤖](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.اعاده تشغيل`\n**لـ لتـرسيت واعـادة تشغيـل البـوت**\n\n**⎞𝟐⎝** `.ايقاف البوت`\n**لـ ايقـاف البـوت عـن العمـل والغـاء التنصـيب**\n\n**⎞𝟑⎝** `.تحديث`\n**لـ البحـث عـن تحديثـات وتحديث البـوت**\n\n**⎞𝟒⎝** `.تحديث الان`\n**لـ التحـديث الاولـي لـ البـوت لـ التنصيـب الثـانوي**\n\n**⎞𝟓⎝** `.تحديث البوت`\n**لـ التحـديث الثـانوي لـ البـوت لـ التنصيـب الاولـي والثـانوي**\n\n**•❐• لعـرض اصـدار السـورس استخـدم امـر** `.سورس`\n**•❐• لعـرض قنـوات السـورس استخـدم امـر** `.زدثون`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")
@zedub.zed_cmd(pattern="م3(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر الـوقتــي](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.الاسم تلقائي`\n**لوضـع اسـم وقتـي لحسابـك يتغيـر تلقائيـاً كـل دقيقـه مـع الوقـت**\n\n\n**⎞𝟐⎝** `.البايو تلقائي`\n**لوضـع بايـو وقتـي يتغيـر تلقائـياً مع الوقـت كـل دقيقـه .. اولاً قـم بالـرد ع نـص البايـو بالامـر (.اضف البايو) **\n\n\n**⎞𝟑⎝** `.البروفايل تلقائي` \n**لوضـع بروفايـل وقتـي يتغيـر تلقائيـاً مع حسابـك كل دقيقـه اولاً قـم بالـرد ع الصـوره بالامـر (.اضف صورة الوقتي)**\n\n\n**⎞𝟒⎝** `.انهاء الاسم` / `.انهاء البايو` / `.انهاء البروفايل`\n**لـ الغــاء الاوامــر الوقتيــه مـن حســابـك**\n\n\n**⎞𝟓⎝** `.اوامر الوقتي` \n**لـ عـرض اوامـر زخرفـة الاسـم والبروفـايل الوقتـي**\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")
@zedub.zed_cmd(pattern="م4(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر المجمــوعــه¹](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.البوتات`\n**كشـف وتنظيف مجموعتـك من البوتات .. لمنع التصفير والتفليش والتخريب**\n\n**⎞𝟐⎝** `.قفل البوتات` / `.فتح البوتات`\n**قفـل البوتـات بالطـرد التلقائـي .. الامر يمنع حتى المشـرفين من اضافـة البوتات .. في حـال اراد احد المشرفين رفـع بوت وتصفير مجموعتك اثنـاء غيابـك.**\n\n**⎞𝟑⎝** `.قفل الاضافه` / `.فتح الاضافه`  \n**قفـل اضافـة الاعضـاء بالطـرد .. مـع تحذيـر صاحـب الاضـافه**\n\n**⎞𝟒⎝** `.قفل الدخول` / `.فتح الدخول `\n**قفـل الدخـول بالرابـط بالطـرد التلقائـي .. حيث يقـوم بطـرد المنضم تلقائيـاً .. مـع ارسـال رسـاله تحذيريـه**\n\n**⎞𝟓⎝** `.قفل الميديا` \ `.فتح الميديا `\n**قفـل الوسائـط بالمسـح + تقييـد المرسـل من صلاحيـة ارسال الوسائط تلقائيـاً .. مع السمـاح له بارسـال الرسـائل فقـط .. يفيدكـم بـ منـع التفليـش الاباحـي في حال غيابكـم او انشغـالكم .. يسمـح للمشـرفين فقـط بارسـال الوسائـط**\n\n**⎞𝟔⎝** `.قفل الفشار` / `.فتح الفشار`\n**لـ مسـح رسـائل الفشار والسب والتكفير تلقائيـاً .. مـع تحذيـر الشخـص المرسـل **\n\n**⎞𝟕⎝** `.قفل الفارسيه` / `.فتح الفارسيه`\n**لـ مسـح رسـائل الايرانيين وبوتات الاعلانات الفارسيه تلقائيـاً.. مـع تحذيـر الشخـص المرسـل**\n\n**⎞𝟖⎝** `.قفل الروابط` / `.فتح الروابط`\n**قفـل الروابـط بالمسـح التلقائـي .. مع تحذير الشخص المرسل**\n\n**⎞𝟗⎝**`.قفل المعرفات` / `.فتح المعرفات`**قفـل المعرفـات بالمسـح التلقائـي .. مع تحذير الشخص المرسل**\n\n**⎞𝟏𝟎⎝** `.قفل الانلاين` / `.فتح الانلاين`\n**قفـل رسائل الانلايـن والهمسـات بالمسـح التلقائـي .. مع تحذير الشخص .. يسمـح للمشرفين فقـط بارسال الانلايـن**\n\n**⎞𝟏𝟏⎝** `.قفل الكل` / `.فتح الكل`\n**لـ قفـل او فتـح كـل الاوامـر السابقـه**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪](t.me/I_R_S_A_I) 𓆪")
@zedub.zed_cmd(pattern="م5(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر المجمــوعــه²](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.الرابط`\n**لـ جـلب رابـط الكـروب + يجب ان تكون مشرفـاً فيهـا**\n\n**⎞𝟐⎝** `.رسائلي` / `.رسائله`\n**لـ عـرض عـدد رسـائلك او رسائل شخـص بالكـروب**\n\n**⎞𝟑⎝** `.حذف رسائلي`\n**لـ حـذف جميـع رسـائلك بالكـروب**\n\n**⎞𝟒⎝** `.غادر`\n**لـ مغـادرة الكـروب**\n\n**⎞𝟓⎝** `.رفع مشرف`\n**لـ رفـع الشخـص مشـرفـاً بالكـروب**\n\n**⎞𝟔⎝** `.تنزيل مشرف`\n**لـ تنزيـل الشخـص مـن الاشـراف + يجـب ان تكـون انت من قـام برفعـه مسبقـاً **\n\n**⎞𝟕⎝** `.رفع مالك`\n**لـ رفـع الشخـص مشـرفـاً بالكـروب بلقـب مـالك**\n\n**⎞𝟖⎝** `.الاعدادات`\n**لـ عـرض اعـدادات الكـروب**\n\n\n**⎞𝟗⎝** `.تاك` / `.all` \n**الامـر + كلمـه او بالـرد ع رسـالـه لـ عمـل تـاك بشكـل متقطـع لـ الكـل بالكـروب**\n\n**⎞𝟏𝟎⎝** `.ايقاف التاك`\n**لـ إيقـاف التـاك**\n\n\n**⎞𝟏𝟏⎝** `.احصائياتي`\n**لـ عـرض قائمـة بـ إحصـائيات دردشـات حسـابك**\n\n**⎞𝟏𝟐⎝** `.كروباتي الكل` / `.كروباتي ادمن` / `.كروباتي مالك` \n**لـ عـرض قائمـة بمعلومـات كروباتك**\n\n**⎞𝟏𝟑⎝** `.قنواتي الكل` / `.قنواتي ادمن` / `.قنواتي مالك`\n**لـ عـرض قائمـة بمعلومـات قنواتـك**\n\n**⎞𝟏𝟒⎝** `.الاعضاء` / `.المشرفين` \n**⦇.الاعضاء / .المشرفين + معرف او رابـط الكـروب⦈ لـ عـرض قائمـة او ملـف بـ اعضـاء / او مشرفيـن الكـروب**\n\n**⎞𝟏𝟓⎝** `.البوتات`\n**⦇.البوتات + معرف او رابـط الكـروب⦈ لـ عـرض قائمـة بـ بوتـات الكـروب**\n\n**⎞𝟏𝟔⎝** `.الحسابات المحذوفه`\n**⦇.الحسابات المحذوفه او .الحسابات المحذوفه تنظيف⦈ لـ عـرض او تنظيـف الكـروب من الحسـابات المحذوفـه**\n\n**⎞𝟏𝟕⎝** `.مسح المحظورين`\n**لـ مسـح محظـورين الكـروب**\n\n\n**⎞𝟏𝟖⎝** `.ضيف`\n**⦇.ضيف + رابط المجموعـه⦈ لـ اضـافة الاعضـاء استخـدم الامـر بالكـروب الهـدف مع اضافه رابط كروبك لـ الامـر**\n\n**⎞𝟏𝟗⎝** `.تفليش`\n**لـ تفليـش جميـع اعضـاء مجمـوعـه معينـه**\n\n**⎞𝟐𝟎⎝** `.تصفير`\n**لـ تفليـش جميـع اعضـاء قنـاة معينـه**\n\n**⎞𝟐𝟏⎝** `.الصورة وضع` / `.الصورة حذف` \n**لـ وضـع / حـذف صـورة المجمـوعـة**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪](t.me/I_R_S_A_I) 𓆪")
@zedub.zed_cmd(pattern="م6(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر الحســاب 🚹](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.ايدي` او `.ا`\n**⦇.ايدي بالـرد او + معـرف/ايـدي الشخص⦈ لـ عـرض معلومـات الشخـص**\n\n**⎞𝟐⎝** `.الايدي`\n**⦇.الايدي بالـرد⦈ لـ جلـب ايـدي الشخـص والكـروب**\n\n**⎞𝟑⎝** `.صورته`\n**⦇.صورته بالـرد / .صورته الكل بالـرد⦈ لـ جـلب جميـع بروفـايلات الشخـص**\n\n**⎞𝟒⎝** `.اسمه`\n**⦇.اسمه بالـرد⦈ لـ جـلب اسـم الشخـص**\n\n**⎞𝟓⎝** `.الاسماء`\n**⦇.الاسماء بالـرد / .الاسماء + معـرف او ايدي الشخـص⦈ لـ جـلب قائمـة بسجـل اسمـاء حسـاب الشخـص**\n\n**⎞𝟔⎝** `.المعرفات`\n**⦇.المعرفات بالـرد / .المعرفات + معـرف او ايدي الشخـص⦈ لـ جـلب قائمـة بسجـل معـرفـات حسـاب الشخـص**\n\n**⎞𝟕⎝** `.تخزين الخاص تفعيل`\n**⦇الامـر + تفعيل او تعطيل⦈ لـ تخـزين جميـع رسـائل الخـاص بـ كـروب التخـزين**\n\n**⎞𝟖⎝** `.تخزين الكروبات تفعيل`\n**⦇الامـر + تفعيل او تعطيل⦈ لـ تخـزين جميـع تاكـات الكـروبات بـ كـروب التخـزين**\n\n\n**- اوامــر حمـايــة الخــاص🛡 :**\n\n**⎞𝟗⎝** `.الحمايه تفعيل`\n**لـ تفعيـل حمايـة الخـاص لـ حسـابك**\n\n**⎞𝟏𝟎⎝** `.الحمايه تعطيل`\n**لـ تعطيـل حمايـة الخـاص لـ حسـابك**\n\n**⎞𝟏𝟏⎝** `.قبول`\n**لـ السمـاح لـ الشخـص بـ ارسـال رسـائل الخـاص اثنـاء تفعيـل حمـاية الخـاص بحسـابك بـدون تحـذير**\n\n**⎞𝟏𝟐⎝** `.رفض`\n**لـ رفـض الشخـص من ارسـال رسـائل الخـاص اثنـاء تفعيـل حمـاية الخـاص بحسـابك**\n\n**⎞𝟏𝟑⎝** `.مرفوض`\n**لـ حظـر الشخـص من الخـاص دون تحـذير**\n\n**⎞𝟏𝟒⎝** `.المقبولين`\n**لـ عـرض قائمـة بالاشخـاص المقبـولين**\n\n\n**- اوامــر الحظــر - الكتــم - الطــرد 🔕 :**\n\n**⎞𝟏𝟓⎝** `.حظر`  /  `.الغاء حظر`\n\n**⎞𝟏𝟔⎝** `.كتم`  /  `.الغاء كتم`\n\n**⎞𝟏𝟕⎝** `.طرد`\n\n**⎞𝟏𝟖⎝** `.ح عام`\n\n**⎞𝟏𝟗⎝** `.الغاء ح عام`\n\n**⎞𝟐𝟎⎝** `.ك عام`\n\n**⎞𝟐𝟏⎝** `.الغاء ك عام`\n\n**⎞𝟐𝟐⎝** `.ط عام`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪](t.me/I_R_S_A_I) 𓆪")
@zedub.zed_cmd(pattern="م7(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر الميــديـا والصيــغ](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.ملصق`\n**⦇.ملصق بالـرد ع صـوره او فيديـو⦈ لـ صنـع ملصـق او ملصـق فيديـو متحـرك**\n\n**⎞𝟐⎝** `.حزمه`\n**⦇.حزمه بالـرد ع ملصـق⦈ لـ تفكيـك حزمـة ملصـق مـا وصنعهـا بحقوقـك**\n\n**⎞𝟑⎝** `.صورته`\n**⦇.حزمة + اسـم بالـرد ع ملصـق⦈ لـ تفكيـك حزمـة ملصـق مـا وصنعهـا بحقـوق الاسـم الـذي ادخلتـه**\n\n**⎞𝟒⎝** `.معلومات الملصق`\n**⦇الامـر بالـرد ع ملصـق⦈ لـ جـلب معلومـات حزمـة الملصـق**\n\n**⎞𝟓⎝** `.ملصقات`\n**⦇الامـر + اسـم⦈ لـ البحـث عن حـزم ملصقـات بـ الاسـم**\n\n\n**⎞𝟔⎝** `.لملصق`\n**⦇الامـر بالـرد ع صـوره⦈ لـ تحويـل الصـوره لـ ملصـق**\n\n**⎞𝟕⎝** `.لصوره`\n**⦇الامـر بالـرد ع ملصـق⦈ لـ تحويـل الملصـق لـ صـوره**\n\n**⎞𝟖⎝** `.لفيد`\n**⦇الامـر بالـرد ع صـوره او ملصـق⦈ لـ تحويـلهـا لـ تصميـم فيديـو **\n\n**⎞𝟗⎝** `.دائري`\n**⦇الامـر بالـرد ع صـوره او ملصـق او فيديـو او متحركـه⦈ لـ تحويـلهـا لـ تصميـم فيديـو دائـري**\n\n**⎞𝟏𝟎⎝** `.لمتحركة`\n**⦇الامـر بالـرد ع ملصـق متحـرك⦈ لـ تحويـله لـ متحـركـه**\n\n**⎞𝟏𝟏⎝** `.حول بصمه`\n**⦇الامـر بالـرد ع فيديـو⦈ لـ استخـراج الصـوت كـ تسجيل صوت بصمه**\n\n**⎞𝟏𝟑⎝** `.حول صوت`\n** ⦇الامـر بالـرد ع فيديـو⦈ لـ استخـراج الصـوت كـ ملـف صوت MP3**\n\n**⎞𝟏𝟒⎝** `.لمتحركه`\n** ⦇الامـر بالـرد ع صـوره او ملصـق⦈ لـ تحويـلهـا الـى متحـركـه**\n\n**⎞𝟏𝟓⎝** `.لمتحرك`\n** ⦇الامـر بالـرد ع فيديـو⦈ لـ تحويـله الـى متحـركـه**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪](t.me/I_R_S_A_I) 𓆪")
@zedub.zed_cmd(pattern="م8(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر الفــارات](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.اوامر الفارات`\n**لعـرض اوامــر الفــارات الجـديـده**\n**⎞𝟐⎝** `.جلب`\n**⦇الامـر + اسـم الفـار⦈ لـ جـلب قيمـة الفـار المحـدد**\n**⎞𝟑⎝** `.حذف`\n**⦇الامـر + اسـم الفـار⦈ لـ حـذق قيمـة الفـار المحـدد**\n**⎞𝟒⎝** `.استخدامي`\n**لـ عـرض ساعـات الاستخـدام والساعـات المتبقيـه لـ بـوتك**\n\n**✾╎قائمـة اوامـر تغييـر فـارات الصـور بأمـر واحـد فقـط - لـ اول مـره ع سـورس تليثـون يوزر بـوت 🦾 :**\n**⎞𝟓⎝** `.اضف صورة الفحص`\n**⦇الامـر بالـرد ع صـوره او ميـديـا⦈**\n**⎞𝟔⎝** `.اضف صورة الوقتي`\n**⦇الامـر بالـرد ع صـوره او ميـديـا⦈**\n**⎞𝟕⎝** `.اضف صورة الفحص`\n**⦇الامـر بالـرد ع صـوره او ميـديـا⦈**\n**⎞𝟕⎝** `.اضف صورة الاوامر`\n**⦇الامـر بالـرد ع صـوره او ميـديـا⦈**\n**⎞𝟕⎝** `.اضف صورة البوت`\n**⦇الامـر بالـرد ع صـوره او ميـديـا⦈**\n\n**✾╎قائـمه اوامر تغييـر بقيـة الفـارات بأمـر واحـد فقـط :**\n**⎞𝟖⎝** `.اضف كليشة الحماية`\n**⦇الامـر بالـرد ع نـص الكليشـه⦈**\n**⎞𝟗⎝** `.اضف كليشة الفحص`\n**⦇الامـر بالـرد ع نـص الكليشـه⦈**\n\n**⎞𝟏𝟎⎝** `.اضف رمز الوقتي`\n**⦇الامـر بالـرد ع الـرمـز⦈**\n**⎞𝟏𝟏⎝** `.اضف زخرفة الوقتي`\n**⦇الامـر بالـرد ع ارقـام الزخـرفـه⦈**\n**⎞𝟏𝟑⎝** `.اضف البايو الوقتي`\n** ⦇الامـر بالـرد ع البـايـو⦈**\n**⎞𝟏𝟒⎝** `.اضف اسم المستخدم`\n** ⦇الامـر بالـرد ع نـص الاسـم⦈**\n**⎞𝟏𝟓⎝** `.اضف كروب الرسائل`\n** ⦇الامـر بالـرد ع ايـدي الكـروب⦈**\n**⎞𝟏𝟔⎝** `.اضف كروب السجل`\n** ⦇الامـر بالـرد ع ايـدي الكـروب⦈**\n**⎞𝟏𝟕⎝** `.اضف ايديي`\n** ⦇الامـر بالـرد ع ايـدي حسـابك⦈**\n**⎞𝟏𝟖⎝** `.اضف نقطة الاوامر`\n** ⦇الامـر بالـرد ع الـرمـز الجـديـد⦈**\n**⎞𝟏𝟗⎝** `.اضف رسائل الحماية`\n** ⦇الامـر بالـرد ع رقـم عـدد رسـائل تحـذيـر الحمـايـة⦈**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪](t.me/I_R_S_A_I) 𓆪")
@zedub.zed_cmd(pattern="م9(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر الـخدمــات العـامــه](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.التخصيص`\n\n**⎞𝟐⎝** `.الترحيب`\n\n**⎞𝟑⎝** `.الردود`\n\n**⎞𝟒⎝** `.الاذاعه`\n\n**⎞𝟓⎝** `.النشر`\n\n**⎞𝟔⎝** `.الكاشف`\n\n**⎞𝟕⎝** `.المساعد`\n\n**⎞𝟖⎝** `.الطقس`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")
@zedub.zed_cmd(pattern="م10(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - قائمــة اوامــر الالـعــاب 🎮🎳](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.بلاي` \n**- قائمــة العــاب الانـلايـن لســورس زدثـــون 🕹**\n\n**⎞𝟐⎝** `.كت`\n**- اسئلـة كـت تـويت ⁉️**\n\n**⎞𝟑⎝** `.احكام`\n**- لعبــة احكــام الشهيــرة ⚖👩🏻‍⚖**\n\n**⎞𝟒⎝** `.عقاب`\n**- لعبــة عقــاب ⛓**\n\n**⎞𝟓⎝** `.اكس او`\n**- لعبــة اكـس او 🧩**\n\n**⎞𝟔⎝** `.نرد`\n**- لعبــة رمـي النــرد 🎲**\n\n**⎞𝟕⎝** `.سهم`\n**- لعبــة رمـي السهــم 🎯**\n\n**⎞𝟖⎝** `.سله`\n**- لعبــة كــرة السلــة 🏀**\n\n**⎞𝟗⎝** `..كرة`\n**- لعبــة كــرة القــدم ⚽️**\n\n**⎞𝟏𝟎⎝** `.حظ`\n**- لعبــة الحــظ 🎰**\n\n**⎞𝟏𝟏⎝** `.خيرني`\n**- لعبــة لـو خيـروك بالصـور ⁉️🌉**\n\n**⎞𝟏𝟐⎝** `.تويت`\n**- لعبــة كـت تـويت بالصـور ⁉️🌁**\n\n\n**- سيتـم اضـافــة المـزيــد من الالعــاب بالتحديثــات الجــايـه 🎭**\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪](t.me/I_R_S_A_I) 𓆪")
@zedub.zed_cmd(pattern="م11(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - قائمــة اوامــر التسـليــه 🏂](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.تسليه` / `.تسليه1`\n**⎞𝟐⎝** `.تسليه2`\n**⎞𝟑⎝** `.تسليه3`\n**⎞𝟒⎝** `.تسليه4`\n**⎞𝟓⎝** `.تسليه5`\n**⎞𝟔⎝** `.تسليه6`\n**⎞𝟕⎝** `.تسليه7`\n**⎞𝟖⎝** `.تسليه8`\n**⎞𝟗⎝** `.تسليه9`\n**⎞𝟏𝟎⎝** `.تسليه10`\n\n**✾╎قائـمه اوامــر التسـليـه الجـديـده حقـوق سـورس زدثـــون :**\n\n**⎞𝟏𝟏⎝** `.حيوان` بالـرد\n\n**⎞𝟏𝟐⎝** `.زاحف` بالـرد\n\n**⎞𝟏𝟑⎝** `.مشهور` بالـرد\n\n**⎞𝟏𝟒⎝** `.مشهوره` بالـرد\n\n**⎞𝟏𝟓⎝** `.التحشيش`\n\n**⎞𝟏𝟔⎝** `.معاني` + اسـم\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪](t.me/I_R_S_A_I) 𓆪")
@zedub.zed_cmd(pattern="م12(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - قائمــة اوامــر التحشيـش 🎃](t.me/I_R_S_A_I) 𓆪\n\n**- اضغـط ع الامـر للنسـخ ثـم قـم بالـرد ع الشخـص**\n\n**⎞𝟏⎝** `.اوصف`  /  `.هينه` \n**⎞𝟐⎝** `.نسبه الحب`\n**⎞𝟑⎝** `.نسبه الانوثه`\n**⎞𝟒⎝** `.نسبه الغباء`\n**⎞𝟓⎝** `.نسبه النجاح`\n**⎞𝟔⎝** `.نسبه الانحراف`\n**⎞𝟕⎝** `.نسبه المثليه`\n**⎞𝟖⎝** `.نسبه الكراهيه`\n\n**⎞𝟗⎝** `.رفع تاج`  /  `.رفع بقلبي`\n**⎞𝟏𝟎⎝** `.رفع صاك`  /  `.رفع صاكه`\n**⎞𝟏𝟏⎝** `.رفع حات`  /  `.رفع حاته`\n**⎞𝟏𝟐⎝** `.رفع ورع`  /  `.رفع مزه`\n**⎞𝟏𝟑⎝** `.رفع مرتي`  /  `.رفع خطيبتي` \n**⎞𝟏𝟒⎝** `.رفع مطي`  /  `.رفع حمار`  /  `.رفع جلب`\n**⎞𝟏𝟓⎝** `.رفع حيوان`  /  `.رفع خروف` \n**⎞𝟏𝟔⎝** `.رفع بزون`  /  `.رفع جريذي`\n**⎞𝟏𝟕⎝** `.رفع فرخ`  /  `.رفع زباله`\n**⎞𝟏𝟖⎝** `.زاحف`  /  `.رفع جلب`\n**⎞𝟏𝟗⎝** `.رفع مرتبط`  /  `.رفع مرتبطه`\n**⎞𝟐𝟎⎝** `.رفع حبيبي`\n**⎞𝟐𝟏⎝** `.رفع مدير`  /  `.رفع منشئ`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪](t.me/I_R_S_A_I) 𓆪")
@zedub.zed_cmd(pattern="م13(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر الستـوريـات 🎆🏖](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.حالات واتس`\n**- اكثـر مـن 2000 فيديـو حالات واتسـاب قصيـرة 🎬**\n\n**⎞𝟐⎝**`.ستوري انمي`\n**- مقاطـع ستوريـات انمـي قصيـرة 🎞**\n\n**⎞𝟑⎝** `.ادت`\n**- مقاطـع ادت منـوعـة 🎥**\n\n**⎞𝟒⎝** `.رياكشن`\n**- مقاطـع رياكشـن ترفيهيــه 📺**\n\n**⎞𝟓⎝** `.ميمز`\n**- بصمـات ميمـز تحشيـش 🎃**\n\n**⎞𝟔⎝** `.غنيلي`\n**- مقاطـع اغـانـي قصيـره 🎶**\n\n**⎞𝟕⎝** `.شعر`\n**- مقاطـع صـوت شعـريـه 🎙**\n\n**⎞𝟖⎝** `.رقيه`\n**- رقيـه شرعيـة لعـدة مشائـخ 🕋**\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪](t.me/I_R_S_A_I) 𓆪")
@zedub.zed_cmd(pattern="م14(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر الآفتـــارات والصــور 🎆🏖](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.ولد انمي`\n**- اكثـر مـن 2500 آفتـار آنمـي شبـاب 🙋🏻‍♂🎆**\n\n**⎞𝟐⎝**`.بنت انمي`\n**- اكثـر مـن 1800 آفتـار آنمـي بنـات 🙋🏻‍♀🎆**\n\n**⎞𝟑⎝** `.رمادي`\n**- آفتـارات شبـاب رمـاديـه 🏂🏙**\n\n**⎞𝟒⎝** `.رماديه`\n**- آفتـارات بنـات رمـاديـه ⛹🏻‍♀🌁**\n\n**⎞𝟓⎝** `.بيست`\n**- آفتـارات بيست تطقيـم بنـات 👯‍♀🏖**\n\n**⎞𝟔⎝** `.حب`\n**- آفتـارات بيست تطقيـم حب ♥️🧚‍♂🧚‍♀**\n\n**⎞𝟕⎝** `.ري اكشن`\n**- صـور رياكشـن تحشيـش 🎃😹**\n\n**⎞𝟖⎝** `.معلومه`\n**- صـوره ومعلومـه معلومـات عـامـه 🗺**\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪](t.me/I_R_S_A_I) 𓆪")


#الكـالبـاك ابديـت - 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪
@ALAPATH(CallbackQuery(data=re.compile(rb"ahmed")))
@check_owner
async def on_plug_in_callback_query_handler(event):
    buttons = [[Button.inline("❶", data="ahmed1"), Button.inline("❷", data="ahmed2"), Button.inline("❸", data="ahmed3"), Button.inline("❹", data="ahmed4"),],[Button.inline("❺", data="ahmed5"), Button.inline("❻", data="ahmed6"), Button.inline("❼", data="ahmed7"), Button.inline("⇒", data="back1"),]]
    await event.edit(Malath, buttons=buttons)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"back1")))
@check_owner
async def on_plug_in_callback_query_handler(event):
    buttons = [[Button.inline("❽", data="ahmed8"), Button.inline("❾", data="ahmed9"), Button.inline("❿", data="ahmad10"), Button.inline("⓫", data="ahmad11"),],[Button.inline("⇐", data="ahmed"), Button.inline("⓬", data="ahmad12"), Button.inline("⓭", data="ahmad13"), Button.inline("⓮", data="ahmad14"),]]
    await event.edit(Malotha, buttons=buttons)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed1")))
@check_owner
async def zed_handler(event):
    buttons = [[Button.inline("رجــوع", data="ahmed")]]
    orden1 = "**⎞𝟏⎝** `.بحث`\n\n**⎞𝟐⎝** `.اغنيه`\n\n**⎞𝟑⎝** `.فيديو`\n\n**⎞𝟒⎝** `.تحميل صوت`\n\n**⎞𝟓⎝** `.تحميل فيديو`\n\n**⎞𝟔⎝** `.يوتيوب`\n\n**⎞𝟕⎝** `.انستا`\n\n**⎞𝟖⎝** `.صور`\n\n**⎞𝟗⎝** `.متحركه`\n\n**⎞𝟏𝟎⎝** `.تيك`\n\n**⎞𝟏𝟏⎝** `.لايكي`\n\n**⎞𝟏𝟐⎝** `.فيسبوك`\n\n**⎞𝟏𝟑⎝** `.تويتر`\n\n**⎞𝟏𝟒⎝** `.بن`\n\n**⎞𝟏𝟓⎝** `.سناب`"
    await event.edit(orden1, buttons=buttons)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed2")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر البـــوت 🦾🤖](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.اعاده تشغيل`\n\n**⎞𝟐⎝** `.ايقاف البوت`\n\n**⎞𝟑⎝** `.تحديث`\n\n**⎞𝟒⎝** `.تحديث الان`\n\n**⎞𝟓⎝** `.تحديث البوت`\n\n\n**•❐• لعـرض معلومـات السـورس استخـدم امـر** `.سورس`\n**•❐• لعـرض قنـوات السـورس استخـدم امـر** `.زدثون` \n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪](t.me/I_R_S_A_I) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed3")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر الوقتـــي ⌚️](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.الاسم تلقائي`\n\n**⎞𝟐⎝** `.البايو تلقائي`\n\n**⎞𝟑⎝** `.البروفايل تلقائي` \n\n**⎞𝟒⎝** `.انهاء الاسم` / `.انهاء البايو` / `.انهاء البروفايل`\n\n**⎞𝟓⎝** `.اوامر الوقتي`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪](t.me/I_R_S_A_I) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed4")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر المجمــوعــه¹](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.البوتات`\n\n**⎞𝟐⎝** `.قفل البوتات` / `.فتح البوتات`\n\n**⎞𝟑⎝** `.قفل الاضافه` / `.فتح الاضافه`  \n\n**⎞𝟒⎝** `.قفل الدخول` / `.فتح الدخول `\n\n**⎞𝟓⎝** `.قفل الميديا` / `.فتح الميديا `\n\n**⎞𝟔⎝** `.قفل الفشار` / `.فتح الفشار`\n\n**⎞𝟕⎝** `.قفل الفارسيه` / `.فتح الفارسيه`\n\n**⎞𝟖⎝** `.قفل الروابط` / `.فتح الروابط`\n\n**⎞𝟗⎝**`.قفل المعرفات` / `.فتح المعرفات`\n\n**⎞𝟏𝟎⎝** `.قفل الانلاين` / `.فتح الانلاين`\n\n**⎞𝟏𝟏⎝** `.قفل الكل` / `.فتح الكل`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪](t.me/I_R_S_A_I) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed5")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر المجمــوعــه²](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.الرابط`\n\n**⎞𝟐⎝**`.رسائلي` / `.رسائله` \n\n**⎞𝟑⎝** `.حذف رسائلي`\n\n**⎞𝟒⎝** `.غادر`\n\n**⎞𝟓⎝** `.رفع مشرف`\n\n**⎞𝟔⎝** `.تنزيل مشرف`\n\n**⎞𝟕⎝** `.رفع مالك`\n\n**⎞𝟖⎝** `.الاعدادات`\n\n**⎞𝟗⎝** `.تاك` / `.all` \n\n**⎞𝟏𝟎⎝** `ايقاف التاك` \n\n\n**⎞𝟏𝟏⎝** `.احصائياتي`\n\n**⎞𝟏𝟐⎝** `.كروباتي الكل` / `.كروباتي ادمن` / `.كروباتي مالك`\n\n**⎞𝟏𝟑⎝** `.قنواتي الكل` / `.قنواتي ادمن` / `.قنواتي مالك`\n\n**⎞𝟏𝟒⎝** `.الاعضاء` / `المشرفين` \n\n**⎞𝟏𝟓⎝** `.البوتات`\n\n**⎞𝟏𝟔⎝** `.الحسابات المحذوفه`\n\n**⎞𝟏𝟕⎝** `.مسح المحظورين`\n\n**⎞𝟏𝟖⎝** `.ضيف`\n\n**⎞𝟏𝟗⎝** `.تفليش`\n**- خـاص بتفليـش المجمـوعـات ✓**\n\n**⎞𝟐𝟎⎝** `.تصفير`\n**- خـاص بتصفيـر القنــوات ✓**\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed6")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر الحســاب 🚹](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.ايدي` / `.ا`\n\n**⎞𝟐⎝** `.الايدي`\n\n**⎞𝟑⎝** `.صورته`\n\n**⎞𝟒⎝** `.اسمه`\n\n**⎞𝟓⎝** `.الاسماء`\n\n**⎞𝟔⎝** `.المعرفات`\n\n**⎞𝟕⎝** `.تخزين الخاص تفعيل`\n\n**⎞𝟖⎝** `.تخزين الكروبات تفعيل`\n\n\n**- اوامــر حمـايــة الخــاص🛡 :**\n\n**⎞𝟗⎝** `.الحمايه تفعيل`\n\n**⎞𝟏𝟎⎝** `.الحمايه تعطيل`\n\n**⎞𝟏𝟏⎝** `.قبول`\n\n**⎞𝟏𝟐⎝** `.رفض`\n\n**⎞𝟏𝟑⎝** `.مرفوض`\n\n**⎞𝟏𝟒⎝** `.المقبولين`\n\n\n**- اوامــر الحظــر - الكتــم - الطــرد 🔕 :**\n\n**⎞𝟏𝟓⎝** `.حظر`  /  `.الغاء حظر`\n\n**⎞𝟏𝟔⎝** `.كتم`  /  `.الغاء كتم`\n\n**⎞𝟏𝟕⎝** `.طرد`\n\n**⎞𝟏𝟖⎝** `.ح عام`\n\n**⎞𝟏𝟗⎝** `.الغاء ح عام`\n\n**⎞𝟐𝟎⎝** `.ك عام`\n\n**⎞𝟐𝟏⎝** `.الغاء ك عام`\n\n**⎞𝟐𝟐⎝** `.ط عام`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed7")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر تحـويـل الصيــغ 💡🎞](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.ملصق`\n\n**⎞𝟐⎝** `.حزمه`\n\n**⎞𝟑⎝** `.صورته`\n\n**⎞𝟒⎝** `.معلومات الملصق`\n\n**⎞𝟓⎝** `.ملصقات`\n\n**⎞𝟔⎝** `.لملصق`\n\n**⎞𝟕⎝** `.لصوره`\n\n**⎞𝟖⎝** `.لفيد`\n\n**⎞𝟗⎝** `.دائري`\n\n**⎞𝟏𝟎⎝** `.لمتحركة`\n\n**⎞𝟏𝟏⎝** `.حول بصمه`\n\n**⎞𝟏𝟑⎝** `.حول صوت`\n\n**⎞𝟏𝟒⎝** `.لمتحركه`\n\n**⎞𝟏𝟓⎝** `.لمتحرك`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed8")))
@check_owner
async def zed_handler(zedub):
    text = "**⎞𝟏⎝** `.اوامر الفارات`\n\n**⎞𝟐⎝** `.استخدامي`\n\n**✾╎قائمـة اوامـر تغييـر فـارات الصـور بأمـر واحـد فقـط بالــرد - لـ اول مـره ع سـورس تليثـون يوزر بـوت :**\n\n**⎞𝟑⎝** `.اضف صورة الاوامر`\n\n**⎞𝟒⎝** `.اضف صورة الحمايه`\n\n**⎞𝟓⎝** `.اضف صورة الوقتي`\n\n**⎞𝟔⎝** `.اضف صورة الفحص`\n\n**⎞𝟕⎝** `.اضف صورة البوت`\n\n**✾╎قائـمه اوامر تغييـر بقيـة الفـارات بأمـر واحـد فقـط بالــرد :**\n\n**⎞𝟖⎝** `.اضف كليشة الحماية`\n\n**⎞𝟗⎝** `.اضف كليشة الفحص`\n\n**⎞𝟏𝟎⎝** `.اضف رمز الوقتي`\n\n**⎞𝟏𝟏⎝** `.اضف زخرفة الوقتي`\n\n**⎞𝟏𝟑⎝** `.اضف البايو`\n\n**⎞𝟏𝟒⎝** `.اضف اسم المستخدم`\n\n**⎞𝟏𝟓⎝** `.اضف كروب الرسائل`\n\n**⎞𝟏𝟔⎝** `.اضف كروب السجل`\n\n**⎞𝟏𝟕⎝** `.اضف ايديي`\n\n**⎞𝟏𝟖⎝** `.اضف نقطة الاوامر`\n\n**⎞𝟏𝟗⎝** `.اضف رسائل الحماية`"
    zilzal = [[Button.inline("رجــوع", data="back1")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed9")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر الـخدمــات العـامــه](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.التخصيص`\n\n**⎞𝟐⎝** `.الترحيب`\n\n**⎞𝟑⎝** `.الردود`\n\n**⎞𝟒⎝** `.الاذاعه`\n\n**⎞𝟓⎝** `.النشر`\n\n**⎞𝟔⎝** `.الكاشف`\n\n**⎞𝟕⎝** `.المساعد`\n\n**⎞𝟖⎝** `.الطقس`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="back1")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmad10")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر الالـعــاب 🎮🎳 ](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.بلاي` \n**- العــاب الانـلايـن لســورس زدثـــون 🕹\n\n**⎞𝟐⎝** `.كت`\n**- اسئلـة كـت تـويت ⁉️**\n\n**⎞𝟑⎝** `.احكام`\n**- لعبــة احكــام الشهيــرة ⚖👩🏻‍⚖**\n\n**⎞𝟒⎝** `.عقاب`\n**- لعبــة عقــاب ⛓**\n\n**⎞𝟓⎝** `.اكس او`\n**- لعبــة اكـس او 🧩**\n\n**⎞𝟔⎝** `.نرد`\n**- لعبــة رمـي النــرد 🎲**\n\n**⎞𝟕⎝** `.سهم`\n**- لعبــة رمـي السهــم 🎯**\n\n**⎞𝟖⎝** `.سله`\n**- لعبــة كــرة السلــة 🏀**\n\n**⎞𝟗⎝** `..كرة`\n**- لعبــة كــرة القــدم ⚽️**\n\n**⎞𝟏𝟎⎝** `.حظ`\n**- لعبــة الحــظ 🎰**\n\n**⎞𝟏𝟏⎝** `.خيرني`\n**- لعبــة لـو خيـروك بالصـور ⁉️🌉**\n\n**⎞𝟏𝟐⎝** `.تويت`\n**- لعبــة كـت تـويت بالصـور ⁉️🌁**\n\n\n**- سيتـم اضـافــة المـزيــد من الالعــاب بالتحديثــات الجــايـه 🎭**"
    zilzal = [[Button.inline("رجــوع", data="back1")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmad11")))
@check_owner
async def zed_handler(zedub):
    text = "**✾╎اوامــر التسـليــه 🏂 :**\n\n**⎞𝟏⎝** `.تسليه` / `.تسليه1`\n**⎞𝟐⎝** `.تسليه2`\n**⎞𝟑⎝** `.تسليه3`\n**⎞𝟒⎝** `.تسليه4`\n**⎞𝟓⎝** `.تسليه5`\n**⎞𝟔⎝** `.تسليه6`\n**⎞𝟕⎝** `.تسليه7`\n**⎞𝟖⎝** `.تسليه8`\n**⎞𝟗⎝** `.تسليه9`\n**⎞𝟏𝟎⎝** `.تسليه10`\n\n**✾╎قائـمه اوامــر التسـليـه الجـديـده حقـوق سـورس زدثـــون :**\n\n**⎞𝟏𝟏⎝** `.حيوان` بالـرد\n\n**⎞𝟏𝟐⎝** `.زاحف` بالـرد\n\n**⎞𝟏𝟑⎝** `.مشهور` بالـرد\n\n**⎞𝟏𝟒⎝** `.مشهوره` بالـرد\n\n**⎞𝟏𝟓⎝** `.التحشيش`\n\n**⎞𝟏𝟔⎝** `.معاني` + اسـم"
    zilzal = [[Button.inline("رجــوع", data="back1")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmad12")))
@check_owner
async def zed_handler(zedub):
    text = "**✾╎قائمــة اوامــر التحشيـش 🎃 :**\n**- اضغـط ع الامـر للنسـخ ثـم قـم بالـرد ع الشخـص**\n\n**⎞𝟏⎝** `.اوصف`  /  `.هينه` \n**⎞𝟐⎝** `.نسبه الحب`\n**⎞𝟑⎝** `.نسبه الانوثه`\n**⎞𝟒⎝** `.نسبه الغباء`\n**⎞𝟓⎝** `.نسبه النجاح`\n**⎞𝟔⎝** `.نسبه الانحراف`\n**⎞𝟕⎝** `.نسبه المثليه`\n**⎞𝟖⎝** `.نسبه الكراهيه`\n\n**⎞𝟗⎝** `.رفع تاج`  /  `.رفع بقلبي`\n**⎞𝟏𝟎⎝** `.رفع صاك`  /  `.رفع صاكه`\n**⎞𝟏𝟏⎝** `.رفع حات`  /  `.رفع حاته`\n**⎞𝟏𝟐⎝** `.رفع ورع`  /  `.رفع مزه`\n**⎞𝟏𝟑⎝** `.رفع مرتي`  /  `.رفع خطيبتي` \n**⎞𝟏𝟒⎝** `.رفع مطي`  /  `.رفع حمار`  /  `.رفع جلب`\n**⎞𝟏𝟓⎝** `.رفع حيوان`  /  `.رفع خروف` \n**⎞𝟏𝟔⎝** `.رفع بزون`  /  `.رفع جريذي`\n**⎞𝟏𝟕⎝** `.رفع فرخ`  /  `.رفع زباله`\n**⎞𝟏𝟖⎝** `.زاحف`  /  `.رفع جلب`\n**⎞𝟏𝟗⎝** `.رفع مرتبط`  /  `.رفع مرتبطه`\n**⎞𝟐𝟎⎝** `.رفع حبيبي`\n**⎞𝟐𝟏⎝** `.رفع مدير`  /  `.رفع منشئ`"
    zilzal = [[Button.inline("رجــوع", data="back1")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmad13")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر الستـوريـات 🎆🏖](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.حالات واتس`\n**- اكثـر مـن 2000 فيديـو حالات واتسـاب قصيـرة 🎬**\n\n**⎞𝟐⎝**`.ستوري انمي`\n**- مقاطـع ستوريـات انمـي قصيـرة 🎞**\n\n**⎞𝟑⎝** `.ادت`\n**- مقاطـع ادت منـوعـة 🎥**\n\n**⎞𝟒⎝** `.رياكشن`\n**- مقاطـع رياكشـن ترفيهيــه 📺**\n\n**⎞𝟓⎝** `.ميمز`\n**- بصمـات ميمـز تحشيـش 🎃**\n\n**⎞𝟔⎝** `.غنيلي`\n**- مقاطـع اغـانـي قصيـره 🎶**\n\n**⎞𝟕⎝** `.شعر`\n**- مقاطـع صـوت شعـريـه 🎙**\n\n**⎞𝟖⎝** `.رقيه`\n**- رقيـه شرعيـة لعـدة مشائـخ 🕋**\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪](t.me/I_R_S_A_I) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="back1")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmad14")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪 - اوامــر الآفتـــارات والصــور 🎆🏖](t.me/I_R_S_A_I) 𓆪\n\n**⎞𝟏⎝** `.ولد انمي`\n**- اكثـر مـن 2500 آفتـار آنمـي شبـاب 🙋🏻‍♂🎆**\n\n**⎞𝟐⎝**`.بنت انمي`\n**- اكثـر مـن 1800 آفتـار آنمـي بنـات 🙋🏻‍♀🎆**\n\n**⎞𝟑⎝** `.رمادي`\n**- آفتـارات شبـاب رمـاديـه 🏂🏙**\n\n**⎞𝟒⎝** `.رماديه`\n**- آفتـارات بنـات رمـاديـه ⛹🏻‍♀🌁**\n\n**⎞𝟓⎝** `.بيست`\n**- آفتـارات بيست تطقيـم بنـات 👯‍♀🏖**\n\n**⎞𝟔⎝** `.حب`\n**- آفتـارات بيست تطقيـم حب ♥️🧚‍♂🧚‍♀**\n\n**⎞𝟕⎝** `.ري اكشن`\n**- صـور رياكشـن تحشيـش 🎃😹**\n\n**⎞𝟖⎝** `.معلومه`\n**- صـوره ومعلومـه معلومـات عـامـه 🗺**\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𓆩𓅃𝘼𝙇𝘼𝙋𝘼𝙏𝙃𓃠𓆪](t.me/I_R_S_A_I) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="back1")]]
    await zedub.edit(text, buttons=zilzal)


#لوحـة قنــوات الســورس
@zedub.tgbot.on(events.InlineQuery)
@check_owner
async def zed_handler(event):
    builder = event.builder
    result = None
    query = event.text
    await zedub.get_me()
    if query.startswith("ALAPATH") and event.query.user_id == zedub.uid:
        ZPIC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/1035d07280ee0ec9fc29b.mp4"
        buttons = [[Button.url("قنـاة السـورس", "https://t.me/I_R_S_A_I"),],[Button.url("التحـديثـات", "https://t.me/I_R_S_A_I"), Button.url("الفـارات", "https://t.me/ALAPATH"),],[Button.url("الشـروحـات¹", "https://t.me/ALAPATH"),],[Button.url("الشـروحـات²", "https://t.me/I_R_S_A_I"),],[Button.url("مطـور السـورس", "https://t.me/ALAPATH"),]]
        if ZPIC and ZPIC.endswith((".jpg", ".png", "gif", "mp4")):
            result = builder.photo(ZPIC,text=Channels, buttons=buttons, link_preview=True)
        elif ZPIC and ZPIC.endswith((".gif", ".mp4")):
            result = builder.document(ZPIC,title="zedub",text=Channels,buttons=buttons,link_preview=True)
        else:
            result = builder.article(title="zedub",text=Channels,buttons=buttons,link_preview=True)
        await event.answer([result] if result else None)
@zedub.zed_cmd(pattern="العابث")
async def repozedub(event):
    if event.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await zedub.inline_query(TG_BOT, "العابث")
    await response[0].click(event.chat_id)
    await event.delete()


@zedub.tgbot.on(InlineQuery)
@check_owner
async def zed_handler(event):
    builder = event.builder
    result = None
    query = event.text
    await zedub.get_me()
    if query.startswith("سورس") and event.query.user_id == zedub.uid:
        ZPIC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/1035d07280ee0ec9fc29b.mp4"
        buttons = [[Button.url("قنـاة الســورس", "https://t.me/I_R_S_A_I"), Button.url("مطـور الســورس", "https://t.me/ALAPATH")]]
        if ZPIC and ZPIC.endswith((".jpg", ".png")):
            result = builder.photo(ZPIC,text=Zelzal, buttons=buttons, link_preview=True)
        elif ZPIC and ZPIC.endswith((".gif", ".mp4")):
            result = builder.document(ZPIC,title="zedub",text=Zelzal,buttons=buttons,link_preview=True)
        else:
            result = builder.article(title="zedub",text=Zelzal,buttons=buttons,link_preview=True)
        await event.answer([result] if result else None)
@zedub.zed_cmd(pattern="سورس")
async def repozedub(event):
    if event.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await zedub.inline_query(TG_BOT, "سورس")
    await response[0].click(event.chat_id)
    await event.delete()
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")
Malath = f"**🖥┊لـوحـة اوامـر آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ الشفـافـه **\n**🧑🏻‍💻┊المستخـدم ↶** {mention} \n\n**•❐• قـائمــة الاوامــر الـعـامــه :**\n\n**•❶• اوامــر الـبحـث والـتحميـل **\n**•❷• اوامــر الـبـوت **\n**•❸• اوامــر الـوقـتـي **\n**•❹• اوامــر الـكــروب¹ **\n**•❺• اوامــر الـكــروب² **\n**•❻• اوامــر الـحسـاب **\n**•❼• اوامــر الميـديـا والـصيــغ **\n\n**•❐• لعـرض بقيـة الاوامـر اضغـط زر التـالي ⇒**\n**•❐• لعـرض الاوامـر مع الوصـف استخـدم امـر** `.الأوامر` "
Malotha = f"**🖥┊يتبـع لـوحـة اوامـر آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ الشفـافـه **\n**🧑🏻‍💻┊المستخـدم ↶** {mention} \n\n**•❐• يتبــع قـائمــة الاوامــر الـعـامــه :**\n\n**•❽• اوامــر الـفــارات **\n**•❾• اوامــر الخـدمــات العـامــه **\n**•❿• اوامــر الالعــاب **\n**•⓫• اوامــر الـتســليــه**\n**•⓬• اوامــر التحشيـش**\n**•⓭• اوامــر الستـوريات**\n**•⓮• اوامــر الآفتــارات**\n\n**•❐• للرجـوع للوحـه السـابقـه اضغـط زر السـابق ⇐**\n**•❐• لعـرض الاوامـر مع الوصـف استخـدم امـر** `.الأوامر` "
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Channels = f"**•❐• مـرحبــاً عـزيـزي  {mention} **\n**•❐• اليـك مجمـوعــة قنـوات زدثـــون ↵ 𝙕𝙏𝙝𝙤𝙣 ♥️🦾**\n\n**•❐• استـخـدم الازرار بالاسفــل↓**"
Zelzal = f"**•◈• اصــدار الســورس ⤽ 7.7**  \n**•◈• المستخــدم ⤽**  {mention}  \n**•◈• وقــت التشغيــل ⤽  {TM}  **\n**•◈• البــوت المســاعـد ⤽  {TG_BOT} **\n**•◈• قنــاة الســورس ⤽  @ZedThon **"



#لـوحــة الاوامــر - حقــوق زدثـــون
@zedub.tgbot.on(events.InlineQuery)
@check_owner
async def zed_handler(event):
    builder = event.builder
    result = None
    query = event.text
    await zedub.get_me()
    if query.startswith("الاوامر") and event.query.user_id == zedub.uid:
        ZEDPIC = gvarstatus("CMD_PIC") or "https://telegra.ph/file/1035d07280ee0ec9fc29b.mp4"
        buttons = [[Button.inline("❶", data="ahmed1"), Button.inline("❷", data="ahmed2"), Button.inline("❸", data="ahmed3"), Button.inline("❹", data="ahmed4"),],[Button.inline("❺", data="ahmed5"), Button.inline("❻", data="ahmed6"), Button.inline("❼", data="ahmed7"), Button.inline("⇒", data="back1"),]]
        if ZEDPIC and ZEDPIC.endswith((".jpg", ".png")):
            result = builder.photo(ZEDPIC,text=Malath, buttons=buttons, link_preview=True)
        elif ZEDPIC and ZEDPIC.endswith((".gif", ".mp4")):
            result = builder.document(ZEDPIC,title="zedub", text=Malath ,buttons=buttons, link_preview=True)
        else:
            result = builder.article(title="zedub",text=Malath,buttons=buttons,link_preview=True)
        await event.answer([result] if result else None)
@zedub.zed_cmd(pattern="الاوامر(?: |$)(.*)")
async def repozedub(event):
    if event.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await event.client.inline_query(TG_BOT, "الاوامر")
    await response[0].click(event.chat_id)
    await event.delete()


@zedub.zed_cmd(pattern=f"الأوامر(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, f"𓆰 [𝗦𝗢𝗨𝗥𝗖𝗘 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - قائمــة الاوامــر العــامــه](t.me/ZEDthon) 𓆪\n◐━─━─━─━─**𝙕𝞝𝘿**─━─━─━─━◐\n**⌔ مـرحبـاً عـزيـزي {mention} اضغـط ع الامـر لـ النسـخ**\n**⌔ ضـع نقطه (.) بداية كل امـر :**\n\n `.م1`**   ➪ اوامـر البحـث والتحميــل** \n\n `.م2`**   ➪ اوامـر البــوت**\n\n `.م3`**   ➪ اوامـر الـوقتــي**\n\n `.م4`**   ➪ اوامـر المجمــوعــه¹**\n\n `.م5`**   ➪ اوامـر المجمــوعــه²**\n\n `.م6`**   ➪ اوامـر الحســاب**\n\n `.م7`**   ➪ اوامـر الميـديـا والصيــغ**\n\n `.م8`**   ➪ اوامـر الفــارات**\n\n `.م9`**   ➪ اوامـر الـخدمــات**\n\n `.م10`** ➪ اوامـر الالـعــاب**\n\n `.م11`** ➪ اوامـر التســليـه**\n\n `.م12`** ➪ اوامـر التحشيـش**\n\n `.م13`** ➪ اوامـر الستـوريات**\n\n `.م14`** ➪ اوامـر الآفتــارات**\n\n ◐━─━─━─━─**آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽**─━─━─━─━◐\n 𓆩 [𝗦𝗢𝗨𝗥𝗖𝗘 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - قنـاة السـورس](t.me/ZEDthon) 𓆪")

@zedub.zed_cmd(pattern="م1(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر البحـث والتحميــل](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.بحث` + اسـم الاغنيـه\n**لـ تحميـل الاغـاني مـن يوتيـوب بدقه خفيفـه وتحميـل اسـرع**\n\n**⎞𝟐⎝** `.اغنيه` + اسـم الاغنيـه\n**لـ تحميـل الاغـاني مـن اليـوتيـوب بدقه عاليـه**\n\n**⎞𝟑⎝** `.فيديو` + اسـم المقطـع\n**لـ تحميـل مقـاطع الفيديـو مـن يوتيـوب**\n\n**⎞𝟒⎝** `.تحميل صوت` + رابـط\n**لـ تحميـل المقـاطع الصـوتيه من يوتيـوب عبر الرابـط**\n\n**⎞𝟓⎝** `.تحميل فيديو` + رابـط\n**لـ تحميـل مقـاطع الفيـديـو من يوتيـوب عبر الرابـط**\n\n**⎞𝟔⎝** `.يوتيوب`+ كلمـه\n**لـ البحث عـن روابـط بالكلمـه ع يوتيـوب **\n\n**⎞𝟕⎝** `.انستا` + رابـط\n**لـ تحميـل الصـور ومقـاطع الفيديـو مـن الانستجـرام**\n\n**⎞𝟖⎝** `.صور` + كلمـه\n**لـ تحميـل الصـور من جوجـل**\n\n**⎞𝟗⎝** `.متحركه` + كلمـه\n**لـ تحميـل صـور متحركـه من جـوجـل..**\n\n**⎞𝟏𝟎⎝** `.تيك` + رابـط او بالـرد ع رابـط\n**لـ تحميـل مقاطـع الفيديـو من تيك توك**\n\n**⎞𝟏𝟏⎝** `.لايكي` + رابـط\n**لـ تحميـل مقاطـع الفيديـو من لايكـي**\n\n**⎞𝟏𝟐⎝** `.فيسبوك` + رابـط او `.فيس` بالـرد ع رابـط\n**لـ تحميـل مقاطـع الفيديـو مـن فيس بـوك**\n\n**⎞𝟏𝟑⎝** `.تويتر` + رابـط\n**لـ تحميـل مقاطـع الفيديـو من تويتـر**\n\n**⎞𝟏𝟒⎝** `.بن` + رابـط\n**لـ تحميـل مقاطـع الفيديـو من بنتـرست**\n\n**⎞𝟏𝟓⎝** `.سناب` + رابـط\n**⦇.سناب + رابـط⦈ لـ تحميـل مقاطـع الفيديـو من سناب شـات**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽](t.me/ZedThon) 𓆪")    
@zedub.zed_cmd(pattern="م2(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر البـــوت 🦾🤖](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.اعاده تشغيل`\n**لـ لتـرسيت واعـادة تشغيـل البـوت**\n\n**⎞𝟐⎝** `.ايقاف البوت`\n**لـ ايقـاف البـوت عـن العمـل والغـاء التنصـيب**\n\n**⎞𝟑⎝** `.تحديث`\n**لـ البحـث عـن تحديثـات وتحديث البـوت**\n\n**⎞𝟒⎝** `.تحديث الان`\n**لـ التحـديث الاولـي لـ البـوت لـ التنصيـب الثـانوي**\n\n**⎞𝟓⎝** `.تحديث البوت`\n**لـ التحـديث الثـانوي لـ البـوت لـ التنصيـب الاولـي والثـانوي**\n\n**•❐• لعـرض اصـدار السـورس استخـدم امـر** `.سورس`\n**•❐• لعـرض قنـوات السـورس استخـدم امـر** `.زدثون`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽](t.me/ZedThon) 𓆪")
@zedub.zed_cmd(pattern="م3(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر الـوقتــي](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.الاسم تلقائي`\n**لوضـع اسـم وقتـي لحسابـك يتغيـر تلقائيـاً كـل دقيقـه مـع الوقـت**\n\n\n**⎞𝟐⎝** `.البايو تلقائي`\n**لوضـع بايـو وقتـي يتغيـر تلقائـياً مع الوقـت كـل دقيقـه .. اولاً قـم بالـرد ع نـص البايـو بالامـر (.اضف البايو) **\n\n\n**⎞𝟑⎝** `.البروفايل تلقائي` \n**لوضـع بروفايـل وقتـي يتغيـر تلقائيـاً مع حسابـك كل دقيقـه اولاً قـم بالـرد ع الصـوره بالامـر (.اضف صورة الوقتي)**\n\n\n**⎞𝟒⎝** `.انهاء الاسم` / `.انهاء البايو` / `.انهاء البروفايل`\n**لـ الغــاء الاوامــر الوقتيــه مـن حســابـك**\n\n\n**⎞𝟓⎝** `.اوامر الوقتي` \n**لـ عـرض اوامـر زخرفـة الاسـم والبروفـايل الوقتـي**\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")
@zedub.zed_cmd(pattern="م4(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر المجمــوعــه¹](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.البوتات`\n**كشـف وتنظيف مجموعتـك من البوتات .. لمنع التصفير والتفليش والتخريب**\n\n**⎞𝟐⎝** `.قفل البوتات` / `.فتح البوتات`\n**قفـل البوتـات بالطـرد التلقائـي .. الامر يمنع حتى المشـرفين من اضافـة البوتات .. في حـال اراد احد المشرفين رفـع بوت وتصفير مجموعتك اثنـاء غيابـك.**\n\n**⎞𝟑⎝** `.قفل الاضافه` / `.فتح الاضافه`  \n**قفـل اضافـة الاعضـاء بالطـرد .. مـع تحذيـر صاحـب الاضـافه**\n\n**⎞𝟒⎝** `.قفل الدخول` / `.فتح الدخول `\n**قفـل الدخـول بالرابـط بالطـرد التلقائـي .. حيث يقـوم بطـرد المنضم تلقائيـاً .. مـع ارسـال رسـاله تحذيريـه**\n\n**⎞𝟓⎝** `.قفل الميديا` \ `.فتح الميديا `\n**قفـل الوسائـط بالمسـح + تقييـد المرسـل من صلاحيـة ارسال الوسائط تلقائيـاً .. مع السمـاح له بارسـال الرسـائل فقـط .. يفيدكـم بـ منـع التفليـش الاباحـي في حال غيابكـم او انشغـالكم .. يسمـح للمشـرفين فقـط بارسـال الوسائـط**\n\n**⎞𝟔⎝** `.قفل الفشار` / `.فتح الفشار`\n**لـ مسـح رسـائل الفشار والسب والتكفير تلقائيـاً .. مـع تحذيـر الشخـص المرسـل **\n\n**⎞𝟕⎝** `.قفل الفارسيه` / `.فتح الفارسيه`\n**لـ مسـح رسـائل الايرانيين وبوتات الاعلانات الفارسيه تلقائيـاً.. مـع تحذيـر الشخـص المرسـل**\n\n**⎞𝟖⎝** `.قفل الروابط` / `.فتح الروابط`\n**قفـل الروابـط بالمسـح التلقائـي .. مع تحذير الشخص المرسل**\n\n**⎞𝟗⎝**`.قفل المعرفات` / `.فتح المعرفات`**قفـل المعرفـات بالمسـح التلقائـي .. مع تحذير الشخص المرسل**\n\n**⎞𝟏𝟎⎝** `.قفل الانلاين` / `.فتح الانلاين`\n**قفـل رسائل الانلايـن والهمسـات بالمسـح التلقائـي .. مع تحذير الشخص .. يسمـح للمشرفين فقـط بارسال الانلايـن**\n\n**⎞𝟏𝟏⎝** `.قفل الكل` / `.فتح الكل`\n**لـ قفـل او فتـح كـل الاوامـر السابقـه**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽](t.me/ZedThon) 𓆪")
@zedub.zed_cmd(pattern="م5(?: |$)(.*)") ]
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر المجمــوعــه²](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.الرابط`\n**لـ جـلب رابـط الكـروب + يجب ان تكون مشرفـاً فيهـا**\n\n**⎞𝟐⎝** `.رسائلي` / `.رسائله`\n**لـ عـرض عـدد رسـائلك او رسائل شخـص بالكـروب**\n\n**⎞𝟑⎝** `.حذف رسائلي`\n**لـ حـذف جميـع رسـائلك بالكـروب**\n\n**⎞𝟒⎝** `.غادر`\n**لـ مغـادرة الكـروب**\n\n**⎞𝟓⎝** `.رفع مشرف`\n**لـ رفـع الشخـص مشـرفـاً بالكـروب**\n\n**⎞𝟔⎝** `.تنزيل مشرف`\n**لـ تنزيـل الشخـص مـن الاشـراف + يجـب ان تكـون انت من قـام برفعـه مسبقـاً **\n\n**⎞𝟕⎝** `.رفع مالك`\n**لـ رفـع الشخـص مشـرفـاً بالكـروب بلقـب مـالك**\n\n**⎞𝟖⎝** `.الاعدادات`\n**لـ عـرض اعـدادات الكـروب**\n\n\n**⎞𝟗⎝** `.تاك` / `.all` \n**الامـر + كلمـه او بالـرد ع رسـالـه لـ عمـل تـاك بشكـل متقطـع لـ الكـل بالكـروب**\n\n**⎞𝟏𝟎⎝** `.ايقاف التاك`\n**لـ إيقـاف التـاك**\n\n\n**⎞𝟏𝟏⎝** `.احصائياتي`\n**لـ عـرض قائمـة بـ إحصـائيات دردشـات حسـابك**\n\n**⎞𝟏𝟐⎝** `.كروباتي الكل` / `.كروباتي ادمن` / `.كروباتي مالك` \n**لـ عـرض قائمـة بمعلومـات كروباتك**\n\n**⎞𝟏𝟑⎝** `.قنواتي الكل` / `.قنواتي ادمن` / `.قنواتي مالك`\n**لـ عـرض قائمـة بمعلومـات قنواتـك**\n\n**⎞𝟏𝟒⎝** `.الاعضاء` / `.المشرفين` \n**⦇.الاعضاء / .المشرفين + معرف او رابـط الكـروب⦈ لـ عـرض قائمـة او ملـف بـ اعضـاء / او مشرفيـن الكـروب**\n\n**⎞𝟏𝟓⎝** `.البوتات`\n**⦇.البوتات + معرف او رابـط الكـروب⦈ لـ عـرض قائمـة بـ بوتـات الكـروب**\n\n**⎞𝟏𝟔⎝** `.الحسابات المحذوفه`\n**⦇.الحسابات المحذوفه او .الحسابات المحذوفه تنظيف⦈ لـ عـرض او تنظيـف الكـروب من الحسـابات المحذوفـه**\n\n**⎞𝟏𝟕⎝** `.مسح المحظورين`\n**لـ مسـح محظـورين الكـروب**\n\n\n**⎞𝟏𝟖⎝** `.ضيف`\n**⦇.ضيف + رابط المجموعـه⦈ لـ اضـافة الاعضـاء استخـدم الامـر بالكـروب الهـدف مع اضافه رابط كروبك لـ الامـر**\n\n**⎞𝟏𝟗⎝** `.تفليش`\n**لـ تفليـش جميـع اعضـاء مجمـوعـه معينـه**\n\n**⎞𝟐𝟎⎝** `.تصفير`\n**لـ تفليـش جميـع اعضـاء قنـاة معينـه**\n\n**⎞𝟐𝟏⎝** `.الصورة وضع` / `.الصورة حذف` \n**لـ وضـع / حـذف صـورة المجمـوعـة**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽](t.me/ZedThon) 𓆪")
@zedub.zed_cmd(pattern="م6(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر الحســاب 🚹](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.ايدي` او `.ا`\n**⦇.ايدي بالـرد او + معـرف/ايـدي الشخص⦈ لـ عـرض معلومـات الشخـص**\n\n**⎞𝟐⎝** `.الايدي`\n**⦇.الايدي بالـرد⦈ لـ جلـب ايـدي الشخـص والكـروب**\n\n**⎞𝟑⎝** `.صورته`\n**⦇.صورته بالـرد / .صورته الكل بالـرد⦈ لـ جـلب جميـع بروفـايلات الشخـص**\n\n**⎞𝟒⎝** `.اسمه`\n**⦇.اسمه بالـرد⦈ لـ جـلب اسـم الشخـص**\n\n**⎞𝟓⎝** `.الاسماء`\n**⦇.الاسماء بالـرد / .الاسماء + معـرف او ايدي الشخـص⦈ لـ جـلب قائمـة بسجـل اسمـاء حسـاب الشخـص**\n\n**⎞𝟔⎝** `.المعرفات`\n**⦇.المعرفات بالـرد / .المعرفات + معـرف او ايدي الشخـص⦈ لـ جـلب قائمـة بسجـل معـرفـات حسـاب الشخـص**\n\n**⎞𝟕⎝** `.تخزين الخاص تفعيل`\n**⦇الامـر + تفعيل او تعطيل⦈ لـ تخـزين جميـع رسـائل الخـاص بـ كـروب التخـزين**\n\n**⎞𝟖⎝** `.تخزين الكروبات تفعيل`\n**⦇الامـر + تفعيل او تعطيل⦈ لـ تخـزين جميـع تاكـات الكـروبات بـ كـروب التخـزين**\n\n\n**- اوامــر حمـايــة الخــاص🛡 :**\n\n**⎞𝟗⎝** `.الحمايه تفعيل`\n**لـ تفعيـل حمايـة الخـاص لـ حسـابك**\n\n**⎞𝟏𝟎⎝** `.الحمايه تعطيل`\n**لـ تعطيـل حمايـة الخـاص لـ حسـابك**\n\n**⎞𝟏𝟏⎝** `.قبول`\n**لـ السمـاح لـ الشخـص بـ ارسـال رسـائل الخـاص اثنـاء تفعيـل حمـاية الخـاص بحسـابك بـدون تحـذير**\n\n**⎞𝟏𝟐⎝** `.رفض`\n**لـ رفـض الشخـص من ارسـال رسـائل الخـاص اثنـاء تفعيـل حمـاية الخـاص بحسـابك**\n\n**⎞𝟏𝟑⎝** `.مرفوض`\n**لـ حظـر الشخـص من الخـاص دون تحـذير**\n\n**⎞𝟏𝟒⎝** `.المقبولين`\n**لـ عـرض قائمـة بالاشخـاص المقبـولين**\n\n\n**- اوامــر الحظــر - الكتــم - الطــرد 🔕 :**\n\n**⎞𝟏𝟓⎝** `.حظر`  /  `.الغاء حظر`\n\n**⎞𝟏𝟔⎝** `.كتم`  /  `.الغاء كتم`\n\n**⎞𝟏𝟕⎝** `.طرد`\n\n**⎞𝟏𝟖⎝** `.ح عام`\n\n**⎞𝟏𝟗⎝** `.الغاء ح عام`\n\n**⎞𝟐𝟎⎝** `.ك عام`\n\n**⎞𝟐𝟏⎝** `.الغاء ك عام`\n\n**⎞𝟐𝟐⎝** `.ط عام`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽](t.me/ZedThon) 𓆪")
@zedub.zed_cmd(pattern="م7(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر الميــديـا والصيــغ](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.ملصق`\n**⦇.ملصق بالـرد ع صـوره او فيديـو⦈ لـ صنـع ملصـق او ملصـق فيديـو متحـرك**\n\n**⎞𝟐⎝** `.حزمه`\n**⦇.حزمه بالـرد ع ملصـق⦈ لـ تفكيـك حزمـة ملصـق مـا وصنعهـا بحقوقـك**\n\n**⎞𝟑⎝** `.صورته`\n**⦇.حزمة + اسـم بالـرد ع ملصـق⦈ لـ تفكيـك حزمـة ملصـق مـا وصنعهـا بحقـوق الاسـم الـذي ادخلتـه**\n\n**⎞𝟒⎝** `.معلومات الملصق`\n**⦇الامـر بالـرد ع ملصـق⦈ لـ جـلب معلومـات حزمـة الملصـق**\n\n**⎞𝟓⎝** `.ملصقات`\n**⦇الامـر + اسـم⦈ لـ البحـث عن حـزم ملصقـات بـ الاسـم**\n\n\n**⎞𝟔⎝** `.لملصق`\n**⦇الامـر بالـرد ع صـوره⦈ لـ تحويـل الصـوره لـ ملصـق**\n\n**⎞𝟕⎝** `.لصوره`\n**⦇الامـر بالـرد ع ملصـق⦈ لـ تحويـل الملصـق لـ صـوره**\n\n**⎞𝟖⎝** `.لفيد`\n**⦇الامـر بالـرد ع صـوره او ملصـق⦈ لـ تحويـلهـا لـ تصميـم فيديـو **\n\n**⎞𝟗⎝** `.دائري`\n**⦇الامـر بالـرد ع صـوره او ملصـق او فيديـو او متحركـه⦈ لـ تحويـلهـا لـ تصميـم فيديـو دائـري**\n\n**⎞𝟏𝟎⎝** `.لمتحركة`\n**⦇الامـر بالـرد ع ملصـق متحـرك⦈ لـ تحويـله لـ متحـركـه**\n\n**⎞𝟏𝟏⎝** `.حول بصمه`\n**⦇الامـر بالـرد ع فيديـو⦈ لـ استخـراج الصـوت كـ تسجيل صوت بصمه**\n\n**⎞𝟏𝟑⎝** `.حول صوت`\n** ⦇الامـر بالـرد ع فيديـو⦈ لـ استخـراج الصـوت كـ ملـف صوت MP3**\n\n**⎞𝟏𝟒⎝** `.لمتحركه`\n** ⦇الامـر بالـرد ع صـوره او ملصـق⦈ لـ تحويـلهـا الـى متحـركـه**\n\n**⎞𝟏𝟓⎝** `.لمتحرك`\n** ⦇الامـر بالـرد ع فيديـو⦈ لـ تحويـله الـى متحـركـه**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")
@zedub.zed_cmd(pattern="م8(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر الفــارات](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.اوامر الفارات`\n**لعـرض اوامــر الفــارات الجـديـده**\n**⎞𝟐⎝** `.جلب`\n**⦇الامـر + اسـم الفـار⦈ لـ جـلب قيمـة الفـار المحـدد**\n**⎞𝟑⎝** `.حذف`\n**⦇الامـر + اسـم الفـار⦈ لـ حـذق قيمـة الفـار المحـدد**\n**⎞𝟒⎝** `.استخدامي`\n**لـ عـرض ساعـات الاستخـدام والساعـات المتبقيـه لـ بـوتك**\n\n**✾╎قائمـة اوامـر تغييـر فـارات الصـور بأمـر واحـد فقـط - لـ اول مـره ع سـورس تليثـون يوزر بـوت 🦾 :**\n**⎞𝟓⎝** `.اضف صورة الفحص`\n**⦇الامـر بالـرد ع صـوره او ميـديـا⦈**\n**⎞𝟔⎝** `.اضف صورة الوقتي`\n**⦇الامـر بالـرد ع صـوره او ميـديـا⦈**\n**⎞𝟕⎝** `.اضف صورة الفحص`\n**⦇الامـر بالـرد ع صـوره او ميـديـا⦈**\n**⎞𝟕⎝** `.اضف صورة الاوامر`\n**⦇الامـر بالـرد ع صـوره او ميـديـا⦈**\n**⎞𝟕⎝** `.اضف صورة البوت`\n**⦇الامـر بالـرد ع صـوره او ميـديـا⦈**\n\n**✾╎قائـمه اوامر تغييـر بقيـة الفـارات بأمـر واحـد فقـط :**\n**⎞𝟖⎝** `.اضف كليشة الحماية`\n**⦇الامـر بالـرد ع نـص الكليشـه⦈**\n**⎞𝟗⎝** `.اضف كليشة الفحص`\n**⦇الامـر بالـرد ع نـص الكليشـه⦈**\n\n**⎞𝟏𝟎⎝** `.اضف رمز الوقتي`\n**⦇الامـر بالـرد ع الـرمـز⦈**\n**⎞𝟏𝟏⎝** `.اضف زخرفة الوقتي`\n**⦇الامـر بالـرد ع ارقـام الزخـرفـه⦈**\n**⎞𝟏𝟑⎝** `.اضف البايو الوقتي`\n** ⦇الامـر بالـرد ع البـايـو⦈**\n**⎞𝟏𝟒⎝** `.اضف اسم المستخدم`\n** ⦇الامـر بالـرد ع نـص الاسـم⦈**\n**⎞𝟏𝟓⎝** `.اضف كروب الرسائل`\n** ⦇الامـر بالـرد ع ايـدي الكـروب⦈**\n**⎞𝟏𝟔⎝** `.اضف كروب السجل`\n** ⦇الامـر بالـرد ع ايـدي الكـروب⦈**\n**⎞𝟏𝟕⎝** `.اضف ايديي`\n** ⦇الامـر بالـرد ع ايـدي حسـابك⦈**\n**⎞𝟏𝟖⎝** `.اضف نقطة الاوامر`\n** ⦇الامـر بالـرد ع الـرمـز الجـديـد⦈**\n**⎞𝟏𝟗⎝** `.اضف رسائل الحماية`\n** ⦇الامـر بالـرد ع رقـم عـدد رسـائل تحـذيـر الحمـايـة⦈**\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽](t.me/ZedThon) 𓆪")
@zedub.zed_cmd(pattern="م9(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر الـخدمــات العـامــه](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.التخصيص`\n\n**⎞𝟐⎝** `.الترحيب`\n\n**⎞𝟑⎝** `.الردود`\n\n**⎞𝟒⎝** `.الاذاعه`\n\n**⎞𝟓⎝** `.النشر`\n\n**⎞𝟔⎝** `.الكاشف`\n\n**⎞𝟕⎝** `.المساعد`\n\n**⎞𝟖⎝** `.الطقس`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽]](t.me/ZedThon) 𓆪")
@zedub.zed_cmd(pattern="م10(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - قائمــة اوامــر الالـعــاب 🎮🎳](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.بلاي` \n**- قائمــة العــاب الانـلايـن لســورس زدثـــون 🕹**\n\n**⎞𝟐⎝** `.كت`\n**- اسئلـة كـت تـويت ⁉️**\n\n**⎞𝟑⎝** `.احكام`\n**- لعبــة احكــام الشهيــرة ⚖👩🏻‍⚖**\n\n**⎞𝟒⎝** `.عقاب`\n**- لعبــة عقــاب ⛓**\n\n**⎞𝟓⎝** `.اكس او`\n**- لعبــة اكـس او 🧩**\n\n**⎞𝟔⎝** `.نرد`\n**- لعبــة رمـي النــرد 🎲**\n\n**⎞𝟕⎝** `.سهم`\n**- لعبــة رمـي السهــم 🎯**\n\n**⎞𝟖⎝** `.سله`\n**- لعبــة كــرة السلــة 🏀**\n\n**⎞𝟗⎝** `..كرة`\n**- لعبــة كــرة القــدم ⚽️**\n\n**⎞𝟏𝟎⎝** `.حظ`\n**- لعبــة الحــظ 🎰**\n\n**⎞𝟏𝟏⎝** `.خيرني`\n**- لعبــة لـو خيـروك بالصـور ⁉️🌉**\n\n**⎞𝟏𝟐⎝** `.تويت`\n**- لعبــة كـت تـويت بالصـور ⁉️🌁**\n\n\n**- سيتـم اضـافــة المـزيــد من الالعــاب بالتحديثــات الجــايـه 🎭**\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")
@zedub.zed_cmd(pattern="م11(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - قائمــة اوامــر التسـليــه 🏂](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.تسليه` / `.تسليه1`\n**⎞𝟐⎝** `.تسليه2`\n**⎞𝟑⎝** `.تسليه3`\n**⎞𝟒⎝** `.تسليه4`\n**⎞𝟓⎝** `.تسليه5`\n**⎞𝟔⎝** `.تسليه6`\n**⎞𝟕⎝** `.تسليه7`\n**⎞𝟖⎝** `.تسليه8`\n**⎞𝟗⎝** `.تسليه9`\n**⎞𝟏𝟎⎝** `.تسليه10`\n\n**✾╎قائـمه اوامــر التسـليـه الجـديـده حقـوق سـورس زدثـــون :**\n\n**⎞𝟏𝟏⎝** `.حيوان` بالـرد\n\n**⎞𝟏𝟐⎝** `.زاحف` بالـرد\n\n**⎞𝟏𝟑⎝** `.مشهور` بالـرد\n\n**⎞𝟏𝟒⎝** `.مشهوره` بالـرد\n\n**⎞𝟏𝟓⎝** `.التحشيش`\n\n**⎞𝟏𝟔⎝** `.معاني` + اسـم\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽](t.me/ZedThon) 𓆪")
@zedub.zed_cmd(pattern="م12(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - قائمــة اوامــر التحشيـش 🎃](t.me/ZedThon) 𓆪\n\n**- اضغـط ع الامـر للنسـخ ثـم قـم بالـرد ع الشخـص**\n\n**⎞𝟏⎝** `.اوصف`  /  `.هينه` \n**⎞𝟐⎝** `.نسبه الحب`\n**⎞𝟑⎝** `.نسبه الانوثه`\n**⎞𝟒⎝** `.نسبه الغباء`\n**⎞𝟓⎝** `.نسبه النجاح`\n**⎞𝟔⎝** `.نسبه الانحراف`\n**⎞𝟕⎝** `.نسبه المثليه`\n**⎞𝟖⎝** `.نسبه الكراهيه`\n\n**⎞𝟗⎝** `.رفع تاج`  /  `.رفع بقلبي`\n**⎞𝟏𝟎⎝** `.رفع صاك`  /  `.رفع صاكه`\n**⎞𝟏𝟏⎝** `.رفع حات`  /  `.رفع حاته`\n**⎞𝟏𝟐⎝** `.رفع ورع`  /  `.رفع مزه`\n**⎞𝟏𝟑⎝** `.رفع مرتي`  /  `.رفع خطيبتي` \n**⎞𝟏𝟒⎝** `.رفع مطي`  /  `.رفع حمار`  /  `.رفع جلب`\n**⎞𝟏𝟓⎝** `.رفع حيوان`  /  `.رفع خروف` \n**⎞𝟏𝟔⎝** `.رفع بزون`  /  `.رفع جريذي`\n**⎞𝟏𝟕⎝** `.رفع فرخ`  /  `.رفع زباله`\n**⎞𝟏𝟖⎝** `.زاحف`  /  `.رفع جلب`\n**⎞𝟏𝟗⎝** `.رفع مرتبط`  /  `.رفع مرتبطه`\n**⎞𝟐𝟎⎝** `.رفع حبيبي`\n**⎞𝟐𝟏⎝** `.رفع مدير`  /  `.رفع منشئ`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")
@zedub.zed_cmd(pattern="م13(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر الستـوريـات 🎆🏖](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.حالات واتس`\n**- اكثـر مـن 2000 فيديـو حالات واتسـاب قصيـرة 🎬**\n\n**⎞𝟐⎝**`.ستوري انمي`\n**- مقاطـع ستوريـات انمـي قصيـرة 🎞**\n\n**⎞𝟑⎝** `.ادت`\n**- مقاطـع ادت منـوعـة 🎥**\n\n**⎞𝟒⎝** `.رياكشن`\n**- مقاطـع رياكشـن ترفيهيــه 📺**\n\n**⎞𝟓⎝** `.ميمز`\n**- بصمـات ميمـز تحشيـش 🎃**\n\n**⎞𝟔⎝** `.غنيلي`\n**- مقاطـع اغـانـي قصيـره 🎶**\n\n**⎞𝟕⎝** `.شعر`\n**- مقاطـع صـوت شعـريـه 🎙**\n\n**⎞𝟖⎝** `.رقيه`\n**- رقيـه شرعيـة لعـدة مشائـخ 🕋**\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")
@zedub.zed_cmd(pattern="م14(?: |$)(.*)") 
async def zed(event):
    await edit_or_reply(event, "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر الآفتـــارات والصــور 🎆🏖](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.ولد انمي`\n**- اكثـر مـن 2500 آفتـار آنمـي شبـاب 🙋🏻‍♂🎆**\n\n**⎞𝟐⎝**`.بنت انمي`\n**- اكثـر مـن 1800 آفتـار آنمـي بنـات 🙋🏻‍♀🎆**\n\n**⎞𝟑⎝** `.رمادي`\n**- آفتـارات شبـاب رمـاديـه 🏂🏙**\n\n**⎞𝟒⎝** `.رماديه`\n**- آفتـارات بنـات رمـاديـه ⛹🏻‍♀🌁**\n\n**⎞𝟓⎝** `.بيست`\n**- آفتـارات بيست تطقيـم بنـات 👯‍♀🏖**\n\n**⎞𝟔⎝** `.حب`\n**- آفتـارات بيست تطقيـم حب ♥️🧚‍♂🧚‍♀**\n\n**⎞𝟕⎝** `.ري اكشن`\n**- صـور رياكشـن تحشيـش 🎃😹**\n\n**⎞𝟖⎝** `.معلومه`\n**- صـوره ومعلومـه معلومـات عـامـه 🗺**\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪")


#الكـالبـاك ابديـت - زدثـــون
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed")))
@check_owner
async def on_plug_in_callback_query_handler(event):
    buttons = [[Button.inline("❶", data="ahmed1"), Button.inline("❷", data="ahmed2"), Button.inline("❸", data="ahmed3"), Button.inline("❹", data="ahmed4"),],[Button.inline("❺", data="ahmed5"), Button.inline("❻", data="ahmed6"), Button.inline("❼", data="ahmed7"), Button.inline("⇒", data="back1"),]]
    await event.edit(Malath, buttons=buttons)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"back1")))
@check_owner
async def on_plug_in_callback_query_handler(event):
    buttons = [[Button.inline("❽", data="ahmed8"), Button.inline("❾", data="ahmed9"), Button.inline("❿", data="ahmad10"), Button.inline("⓫", data="ahmad11"),],[Button.inline("⇐", data="ahmed"), Button.inline("⓬", data="ahmad12"), Button.inline("⓭", data="ahmad13"), Button.inline("⓮", data="ahmad14"),]]
    await event.edit(Malotha, buttons=buttons)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed1")))
@check_owner
async def zed_handler(event):
    buttons = [[Button.inline("رجــوع", data="ahmed")]]
    orden1 = "**⎞𝟏⎝** `.بحث`\n\n**⎞𝟐⎝** `.اغنيه`\n\n**⎞𝟑⎝** `.فيديو`\n\n**⎞𝟒⎝** `.تحميل صوت`\n\n**⎞𝟓⎝** `.تحميل فيديو`\n\n**⎞𝟔⎝** `.يوتيوب`\n\n**⎞𝟕⎝** `.انستا`\n\n**⎞𝟖⎝** `.صور`\n\n**⎞𝟗⎝** `.متحركه`\n\n**⎞𝟏𝟎⎝** `.تيك`\n\n**⎞𝟏𝟏⎝** `.لايكي`\n\n**⎞𝟏𝟐⎝** `.فيسبوك`\n\n**⎞𝟏𝟑⎝** `.تويتر`\n\n**⎞𝟏𝟒⎝** `.بن`\n\n**⎞𝟏𝟓⎝** `.سناب`"
    await event.edit(orden1, buttons=buttons)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed2")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر البـــوت 🦾🤖](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.اعاده تشغيل`\n\n**⎞𝟐⎝** `.ايقاف البوت`\n\n**⎞𝟑⎝** `.تحديث`\n\n**⎞𝟒⎝** `.تحديث الان`\n\n**⎞𝟓⎝** `.تحديث البوت`\n\n\n**•❐• لعـرض معلومـات السـورس استخـدم امـر** `.سورس`\n**•❐• لعـرض قنـوات السـورس استخـدم امـر** `.زدثون` \n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed3")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر الوقتـــي ⌚️](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.الاسم تلقائي`\n\n**⎞𝟐⎝** `.البايو تلقائي`\n\n**⎞𝟑⎝** `.البروفايل تلقائي` \n\n**⎞𝟒⎝** `.انهاء الاسم` / `.انهاء البايو` / `.انهاء البروفايل`\n\n**⎞𝟓⎝** `.اوامر الوقتي`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed4")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر المجمــوعــه¹](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.البوتات`\n\n**⎞𝟐⎝** `.قفل البوتات` / `.فتح البوتات`\n\n**⎞𝟑⎝** `.قفل الاضافه` / `.فتح الاضافه`  \n\n**⎞𝟒⎝** `.قفل الدخول` / `.فتح الدخول `\n\n**⎞𝟓⎝** `.قفل الميديا` / `.فتح الميديا `\n\n**⎞𝟔⎝** `.قفل الفشار` / `.فتح الفشار`\n\n**⎞𝟕⎝** `.قفل الفارسيه` / `.فتح الفارسيه`\n\n**⎞𝟖⎝** `.قفل الروابط` / `.فتح الروابط`\n\n**⎞𝟗⎝**`.قفل المعرفات` / `.فتح المعرفات`\n\n**⎞𝟏𝟎⎝** `.قفل الانلاين` / `.فتح الانلاين`\n\n**⎞𝟏𝟏⎝** `.قفل الكل` / `.فتح الكل`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed5")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر المجمــوعــه²](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.الرابط`\n\n**⎞𝟐⎝**`.رسائلي` / `.رسائله` \n\n**⎞𝟑⎝** `.حذف رسائلي`\n\n**⎞𝟒⎝** `.غادر`\n\n**⎞𝟓⎝** `.رفع مشرف`\n\n**⎞𝟔⎝** `.تنزيل مشرف`\n\n**⎞𝟕⎝** `.رفع مالك`\n\n**⎞𝟖⎝** `.الاعدادات`\n\n**⎞𝟗⎝** `.تاك` / `.all` \n\n**⎞𝟏𝟎⎝** `ايقاف التاك` \n\n\n**⎞𝟏𝟏⎝** `.احصائياتي`\n\n**⎞𝟏𝟐⎝** `.كروباتي الكل` / `.كروباتي ادمن` / `.كروباتي مالك`\n\n**⎞𝟏𝟑⎝** `.قنواتي الكل` / `.قنواتي ادمن` / `.قنواتي مالك`\n\n**⎞𝟏𝟒⎝** `.الاعضاء` / `المشرفين` \n\n**⎞𝟏𝟓⎝** `.البوتات`\n\n**⎞𝟏𝟔⎝** `.الحسابات المحذوفه`\n\n**⎞𝟏𝟕⎝** `.مسح المحظورين`\n\n**⎞𝟏𝟖⎝** `.ضيف`\n\n**⎞𝟏𝟗⎝** `.تفليش`\n**- خـاص بتفليـش المجمـوعـات ✓**\n\n**⎞𝟐𝟎⎝** `.تصفير`\n**- خـاص بتصفيـر القنــوات ✓**\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed6")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر الحســاب 🚹](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.ايدي` / `.ا`\n\n**⎞𝟐⎝** `.الايدي`\n\n**⎞𝟑⎝** `.صورته`\n\n**⎞𝟒⎝** `.اسمه`\n\n**⎞𝟓⎝** `.الاسماء`\n\n**⎞𝟔⎝** `.المعرفات`\n\n**⎞𝟕⎝** `.تخزين الخاص تفعيل`\n\n**⎞𝟖⎝** `.تخزين الكروبات تفعيل`\n\n\n**- اوامــر حمـايــة الخــاص🛡 :**\n\n**⎞𝟗⎝** `.الحمايه تفعيل`\n\n**⎞𝟏𝟎⎝** `.الحمايه تعطيل`\n\n**⎞𝟏𝟏⎝** `.قبول`\n\n**⎞𝟏𝟐⎝** `.رفض`\n\n**⎞𝟏𝟑⎝** `.مرفوض`\n\n**⎞𝟏𝟒⎝** `.المقبولين`\n\n\n**- اوامــر الحظــر - الكتــم - الطــرد 🔕 :**\n\n**⎞𝟏𝟓⎝** `.حظر`  /  `.الغاء حظر`\n\n**⎞𝟏𝟔⎝** `.كتم`  /  `.الغاء كتم`\n\n**⎞𝟏𝟕⎝** `.طرد`\n\n**⎞𝟏𝟖⎝** `.ح عام`\n\n**⎞𝟏𝟗⎝** `.الغاء ح عام`\n\n**⎞𝟐𝟎⎝** `.ك عام`\n\n**⎞𝟐𝟏⎝** `.الغاء ك عام`\n\n**⎞𝟐𝟐⎝** `.ط عام`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed7")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر تحـويـل الصيــغ 💡🎞](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.ملصق`\n\n**⎞𝟐⎝** `.حزمه`\n\n**⎞𝟑⎝** `.صورته`\n\n**⎞𝟒⎝** `.معلومات الملصق`\n\n**⎞𝟓⎝** `.ملصقات`\n\n**⎞𝟔⎝** `.لملصق`\n\n**⎞𝟕⎝** `.لصوره`\n\n**⎞𝟖⎝** `.لفيد`\n\n**⎞𝟗⎝** `.دائري`\n\n**⎞𝟏𝟎⎝** `.لمتحركة`\n\n**⎞𝟏𝟏⎝** `.حول بصمه`\n\n**⎞𝟏𝟑⎝** `.حول صوت`\n\n**⎞𝟏𝟒⎝** `.لمتحركه`\n\n**⎞𝟏𝟓⎝** `.لمتحرك`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="ahmed")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed8")))
@check_owner
async def zed_handler(zedub):
    text = "**⎞𝟏⎝** `.اوامر الفارات`\n\n**⎞𝟐⎝** `.استخدامي`\n\n**✾╎قائمـة اوامـر تغييـر فـارات الصـور بأمـر واحـد فقـط بالــرد - لـ اول مـره ع سـورس تليثـون يوزر بـوت :**\n\n**⎞𝟑⎝** `.اضف صورة الاوامر`\n\n**⎞𝟒⎝** `.اضف صورة الحمايه`\n\n**⎞𝟓⎝** `.اضف صورة الوقتي`\n\n**⎞𝟔⎝** `.اضف صورة الفحص`\n\n**⎞𝟕⎝** `.اضف صورة البوت`\n\n**✾╎قائـمه اوامر تغييـر بقيـة الفـارات بأمـر واحـد فقـط بالــرد :**\n\n**⎞𝟖⎝** `.اضف كليشة الحماية`\n\n**⎞𝟗⎝** `.اضف كليشة الفحص`\n\n**⎞𝟏𝟎⎝** `.اضف رمز الوقتي`\n\n**⎞𝟏𝟏⎝** `.اضف زخرفة الوقتي`\n\n**⎞𝟏𝟑⎝** `.اضف البايو`\n\n**⎞𝟏𝟒⎝** `.اضف اسم المستخدم`\n\n**⎞𝟏𝟓⎝** `.اضف كروب الرسائل`\n\n**⎞𝟏𝟔⎝** `.اضف كروب السجل`\n\n**⎞𝟏𝟕⎝** `.اضف ايديي`\n\n**⎞𝟏𝟖⎝** `.اضف نقطة الاوامر`\n\n**⎞𝟏𝟗⎝** `.اضف رسائل الحماية`"
    zilzal = [[Button.inline("رجــوع", data="back1")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmed9")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر الـخدمــات العـامــه](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.التخصيص`\n\n**⎞𝟐⎝** `.الترحيب`\n\n**⎞𝟑⎝** `.الردود`\n\n**⎞𝟒⎝** `.الاذاعه`\n\n**⎞𝟓⎝** `.النشر`\n\n**⎞𝟔⎝** `.الكاشف`\n\n**⎞𝟕⎝** `.المساعد`\n\n**⎞𝟖⎝** `.الطقس`\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="back1")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmad10")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر الالـعــاب 🎮🎳 ](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.بلاي` \n**- العــاب الانـلايـن لســورس زدثـــون 🕹\n\n**⎞𝟐⎝** `.كت`\n**- اسئلـة كـت تـويت ⁉️**\n\n**⎞𝟑⎝** `.احكام`\n**- لعبــة احكــام الشهيــرة ⚖👩🏻‍⚖**\n\n**⎞𝟒⎝** `.عقاب`\n**- لعبــة عقــاب ⛓**\n\n**⎞𝟓⎝** `.اكس او`\n**- لعبــة اكـس او 🧩**\n\n**⎞𝟔⎝** `.نرد`\n**- لعبــة رمـي النــرد 🎲**\n\n**⎞𝟕⎝** `.سهم`\n**- لعبــة رمـي السهــم 🎯**\n\n**⎞𝟖⎝** `.سله`\n**- لعبــة كــرة السلــة 🏀**\n\n**⎞𝟗⎝** `..كرة`\n**- لعبــة كــرة القــدم ⚽️**\n\n**⎞𝟏𝟎⎝** `.حظ`\n**- لعبــة الحــظ 🎰**\n\n**⎞𝟏𝟏⎝** `.خيرني`\n**- لعبــة لـو خيـروك بالصـور ⁉️🌉**\n\n**⎞𝟏𝟐⎝** `.تويت`\n**- لعبــة كـت تـويت بالصـور ⁉️🌁**\n\n\n**- سيتـم اضـافــة المـزيــد من الالعــاب بالتحديثــات الجــايـه 🎭**"
    zilzal = [[Button.inline("رجــوع", data="back1")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmad11")))
@check_owner
async def zed_handler(zedub):
    text = "**✾╎اوامــر التسـليــه 🏂 :**\n\n**⎞𝟏⎝** `.تسليه` / `.تسليه1`\n**⎞𝟐⎝** `.تسليه2`\n**⎞𝟑⎝** `.تسليه3`\n**⎞𝟒⎝** `.تسليه4`\n**⎞𝟓⎝** `.تسليه5`\n**⎞𝟔⎝** `.تسليه6`\n**⎞𝟕⎝** `.تسليه7`\n**⎞𝟖⎝** `.تسليه8`\n**⎞𝟗⎝** `.تسليه9`\n**⎞𝟏𝟎⎝** `.تسليه10`\n\n**✾╎قائـمه اوامــر التسـليـه الجـديـده حقـوق سـورس زدثـــون :**\n\n**⎞𝟏𝟏⎝** `.حيوان` بالـرد\n\n**⎞𝟏𝟐⎝** `.زاحف` بالـرد\n\n**⎞𝟏𝟑⎝** `.مشهور` بالـرد\n\n**⎞𝟏𝟒⎝** `.مشهوره` بالـرد\n\n**⎞𝟏𝟓⎝** `.التحشيش`\n\n**⎞𝟏𝟔⎝** `.معاني` + اسـم"
    zilzal = [[Button.inline("رجــوع", data="back1")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmad12")))
@check_owner
async def zed_handler(zedub):
    text = "**✾╎قائمــة اوامــر التحشيـش 🎃 :**\n**- اضغـط ع الامـر للنسـخ ثـم قـم بالـرد ع الشخـص**\n\n**⎞𝟏⎝** `.اوصف`  /  `.هينه` \n**⎞𝟐⎝** `.نسبه الحب`\n**⎞𝟑⎝** `.نسبه الانوثه`\n**⎞𝟒⎝** `.نسبه الغباء`\n**⎞𝟓⎝** `.نسبه النجاح`\n**⎞𝟔⎝** `.نسبه الانحراف`\n**⎞𝟕⎝** `.نسبه المثليه`\n**⎞𝟖⎝** `.نسبه الكراهيه`\n\n**⎞𝟗⎝** `.رفع تاج`  /  `.رفع بقلبي`\n**⎞𝟏𝟎⎝** `.رفع صاك`  /  `.رفع صاكه`\n**⎞𝟏𝟏⎝** `.رفع حات`  /  `.رفع حاته`\n**⎞𝟏𝟐⎝** `.رفع ورع`  /  `.رفع مزه`\n**⎞𝟏𝟑⎝** `.رفع مرتي`  /  `.رفع خطيبتي` \n**⎞𝟏𝟒⎝** `.رفع مطي`  /  `.رفع حمار`  /  `.رفع جلب`\n**⎞𝟏𝟓⎝** `.رفع حيوان`  /  `.رفع خروف` \n**⎞𝟏𝟔⎝** `.رفع بزون`  /  `.رفع جريذي`\n**⎞𝟏𝟕⎝** `.رفع فرخ`  /  `.رفع زباله`\n**⎞𝟏𝟖⎝** `.زاحف`  /  `.رفع جلب`\n**⎞𝟏𝟗⎝** `.رفع مرتبط`  /  `.رفع مرتبطه`\n**⎞𝟐𝟎⎝** `.رفع حبيبي`\n**⎞𝟐𝟏⎝** `.رفع مدير`  /  `.رفع منشئ`"
    zilzal = [[Button.inline("رجــوع", data="back1")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmad13")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر الستـوريـات 🎆🏖](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.حالات واتس`\n**- اكثـر مـن 2000 فيديـو حالات واتسـاب قصيـرة 🎬**\n\n**⎞𝟐⎝**`.ستوري انمي`\n**- مقاطـع ستوريـات انمـي قصيـرة 🎞**\n\n**⎞𝟑⎝** `.ادت`\n**- مقاطـع ادت منـوعـة 🎥**\n\n**⎞𝟒⎝** `.رياكشن`\n**- مقاطـع رياكشـن ترفيهيــه 📺**\n\n**⎞𝟓⎝** `.ميمز`\n**- بصمـات ميمـز تحشيـش 🎃**\n\n**⎞𝟔⎝** `.غنيلي`\n**- مقاطـع اغـانـي قصيـره 🎶**\n\n**⎞𝟕⎝** `.شعر`\n**- مقاطـع صـوت شعـريـه 🎙**\n\n**⎞𝟖⎝** `.رقيه`\n**- رقيـه شرعيـة لعـدة مشائـخ 🕋**\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="back1")]]
    await zedub.edit(text, buttons=zilzal)
@zedub.tgbot.on(CallbackQuery(data=re.compile(rb"ahmad14")))
@check_owner
async def zed_handler(zedub):
    text = "𓆰 [𝙎𝙊𝙐𝙍𝘾𝞝 آڷــ؏ــابـث𓃮⇣ۧ⍣≼ٰٖٜٖٖ۬≽ - اوامــر الآفتـــارات والصــور 🎆🏖](t.me/ZedThon) 𓆪\n\n**⎞𝟏⎝** `.ولد انمي`\n**- اكثـر مـن 2500 آفتـار آنمـي شبـاب 🙋🏻‍♂🎆**\n\n**⎞𝟐⎝**`.بنت انمي`\n**- اكثـر مـن 1800 آفتـار آنمـي بنـات 🙋🏻‍♀🎆**\n\n**⎞𝟑⎝** `.رمادي`\n**- آفتـارات شبـاب رمـاديـه 🏂🏙**\n\n**⎞𝟒⎝** `.رماديه`\n**- آفتـارات بنـات رمـاديـه ⛹🏻‍♀🌁**\n\n**⎞𝟓⎝** `.بيست`\n**- آفتـارات بيست تطقيـم بنـات 👯‍♀🏖**\n\n**⎞𝟔⎝** `.حب`\n**- آفتـارات بيست تطقيـم حب ♥️🧚‍♂🧚‍♀**\n\n**⎞𝟕⎝** `.ري اكشن`\n**- صـور رياكشـن تحشيـش 🎃😹**\n\n**⎞𝟖⎝** `.معلومه`\n**- صـوره ومعلومـه معلومـات عـامـه 🗺**\n\n\n 𓆩 [𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿](t.me/ZedThon) 𓆪"
    zilzal = [[Button.inline("رجــوع", data="back1")]]
    await zedub.edit(text, buttons=zilzal)


#لوحـة قنــوات الســورس
@zedub.tgbot.on(events.InlineQuery)
@check_owner
async def zed_handler(event):
    builder = event.builder
    result = None
    query = event.text
    await zedub.get_me()
    if query.startswith("زدثون") and event.query.user_id == zedub.uid:
        ZPIC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/1035d07280ee0ec9fc29b.mp4"
        buttons = [[Button.url("قنـاة السـورس", "https://t.me/ZedThon"),],[Button.url("التحـديثـات", "https://t.me/Zed_Thon"), Button.url("الفـارات", "https://t.me/ALAPATH"),],[Button.url("الشـروحـات¹", "https://t.me/ALAPATH"),],[Button.url("الشـروحـات²", "https://t.me/W_l_N"),],[Button.url("مطـور السـورس", "https://t.me/ALAPATH"),]]
        if ZPIC and ZPIC.endswith((".jpg", ".png", "gif", "mp4")):
            result = builder.photo(ZPIC,text=Channels, buttons=buttons, link_preview=True)
        elif ZPIC and ZPIC.endswith((".gif", ".mp4")):
            result = builder.document(ZPIC,title="zedub",text=Channels,buttons=buttons,link_preview=True)
        else:
            result = builder.article(title="zedub",text=Channels,buttons=buttons,link_preview=True)
        await event.answer([result] if result else None)
@zedub.zed_cmd(pattern="زدثون")
async def repozedub(event):
    if event.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await zedub.inline_query(TG_BOT, "زدثون")
    await response[0].click(event.chat_id)
    await event.delete()


@zedub.tgbot.on(InlineQuery)
@check_owner
async def zed_handler(event):
    builder = event.builder
    result = None
    query = event.text
    await zedub.get_me()
    if query.startswith("سورس") and event.query.user_id == zedub.uid:
        ZPIC = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/1035d07280ee0ec9fc29b.mp4"
        buttons = [[Button.url("قنـاة الســورس", "https://t.me/ZedThon"), Button.url("مطـور الســورس", "https://t.me/ALAPATH")]]
        if ZPIC and ZPIC.endswith((".jpg", ".png")):
            result = builder.photo(ZPIC,text=Zelzal, buttons=buttons, link_preview=True)
        elif ZPIC and ZPIC.endswith((".gif", ".mp4")):
            result = builder.document(ZPIC,title="zedub",text=Zelzal,buttons=buttons,link_preview=True)
        else:
            result = builder.article(title="zedub",text=Zelzal,buttons=buttons,link_preview=True)
        await event.answer([result] if result else None)
@zedub.zed_cmd(pattern="سورس")
async def repozedub(event):
    if event.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await zedub.inline_query(TG_BOT, "سورس")
    await response[0].click(event.chat_id)
    await event.delete()
