from telethon.tl.functions.channels import LeaveChannelRequest
import telethon
from time import sleep
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -
# - QYTHOM TEAM 
# -

qython1.start()



c = requests.session()
bot_username = '@eeobot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'
ownerhson_id = (int(DEVLOO))
LOGS = logging.getLogger(__name__)
DEVS = [6824249353]




@qython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await qython1(JoinChannelRequest("@YV991"))
    except BaseException:
        pass
        
@qython1.on(events.NewMessage)
async def join_channel(event):
    try:
        await qython1(JoinChannelRequest("@YV991"))
    except BaseException:
        pass
      

        
        
        
@qython1.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')
        
        
@qython1.on(events.NewMessage(outgoing=False, pattern='/TEST'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')


@qython1.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
⚝ مرحبا بك في اوامر كـايثـون بـوينت
 
============= • DaDDY • ============

𝟏 - للدخول الى اوامر التجميع : .تجميع

𝟐 - للدخول الى اوامر التحـكم : .تحكم

𝟑 - للدخول الى اوامر مـمـيـزة : .مميزة

𝟒 - لـفـحص عـمـل الـســورس : .فحص

𝑐ℎ:- @YV991

𝑑𝑒𝑣:- @YV991

============= • DaDDY • ============
**""")


@qython1.on(events.NewMessage(outgoing=False, pattern='.تجميع'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
⚝ قـائمة جميع اوامر التجميع التي تحتاجها

============= • DaDDY • ============

`/point1` :  تجميع نقاط بوت المليار
`/point2` : تجميع نقاط بوت الجوكر 
`/point3` :  تجميع نقاط بوت العقاب 
`/point4` :   تجميع نقاط بوت العرب 
note : تستخدم هذه الاوامر بأرسالها الى الحساب او بأرسالها الى مجموعة يوجد فيها الحساب

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/point + bot` : تجميع نقاط بوت غير موجود في القائمة

note : يوزر البوت المطلوب bot ضع مكان الـ

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/somy + bot + second` : تجميع لانهائي 

note : يوزر البوت المطلوب bot ضع مكان الـ 

note : عدد الثواني second ضع مكان الـ

note : ننصحك بوضع عدد الثواني 300

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`/join` : الانضمام الى قنوات البوتات المذكورة

`/transfer` : الدخول لقائمة تحويل نقاط

`/infoacc` : الدخول لقائمة تحويل معلومات

`/lpoint` : لمغادرة جميع القنوات والمجموعات

============= • DaDDY • ============
**""")

@qython1.on(events.NewMessage(outgoing=False, pattern='.تحكم'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
⚝ قائمة اوامر التحكم بالحساب

============= • DaDDY • ============

𝟏 - لتحويل اخر رسالة من مستخدم معين او بوت :

`/forward + يوزر الحساب او البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟐 - لأرسال رسالة الى مستخدم معين او بوت : 

`/send + الرسالة + يوزر الحساب او البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟑 - لجعل الحساب ينقر على زر شفاف في بوت : 

`/button + رقم الزر الشفاف + يوزر البوت`

note :  قم بحساب رقم الزر الشفاف من العدد 0

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟒 - لجعل الحساب ينضم الى قناة او مجموعة

`/jn + يوزر القناة او المجموعة `

============= • DaDDY • ============
**""")

@qython1.on(events.NewMessage(outgoing=False, pattern='.مميزة'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
⚝ قائمة الاوامر المميزة 
============= • DaDDY • ============

𝟏 - لتفعيل بوت عبر الدخول الى رابط الدعوه : 

`/bot + ايدي الحساب + يوزر البوت`

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

𝟐 - الامر التالي يحتوي على ملاحظات تحتاجها :

`/notes`

𝟑 - لجعل الحساب يصوت في مسابقة لايكات :

`/voice + موقع الرسالة + يوزر القناة`

note : موقع الرسالة يعني مثلا اذا كان الاسم في قناة المسابقة اخر اسم او اخر منشور فأن موقع الرسالة 1 وان تكن قبل الاخير فأن موقها 2 وهكذا  بقية المواقع 

𝟒 - لجعل الحساب يغادر قناة او مجموعة :

`/lv + يوزر القناة`

============= • DaDDY • ============
**""")

@qython1.on(events.NewMessage(outgoing=False, pattern='/notes'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**
1 - اذا كنت تريد التحكم بالحسابات في التحميع وتحويل النقاط ومعرفة معلومات كل حساب قم بأنشاء مجموعة خاصة وادخل الحسابات التي قمت بتنصيب لها السورس وارفع الحسابات الى مشرفين ثم استخدم اوامر التجميع 

2 - اذا كنت تريد جعل الحسابات تقوم بتجميع النقاط بدون توقف ونسبة قليلة من الحظر استخدم الامر : somy/ 
بأمكانك معرفة المزيد عن الامر وكيفية استخدامه في قائمة .تجميع ويستحسن عند استعمال الامر وضع عدد الثواني 300 اي يعني هذا عند حدوث خطأ في التجميع او انتهت القنوات فسوف يقوم السورس بالمحاولة في التجميع تلقائيا بعد مرور 300 اي خمس دقائق وسوف يقوم السورس بأخبارك جميع ماتم الوصول اليه من الامر ويمكنك ايقاف التجميع بأرسال .اعادة تشغيل 

3 - اذا كنت تريد تجميع نقاط بوتات التمويل بطريقة اعتيادية بدون المحاولة مرة اخرى تلقائيا يمكن استخدام الاوامر التالية [point , /point1/ , .....] يمكنك مراجعة الاوامر في القائمة .تجميع في اول قسمين من القائمة
**""")

@qython1.on(events.NewMessage(outgoing=True, pattern=".الاوامر"))
async def _(event):
      await event.edit("""**
〠 اوامر حساب المستخدم 

• بوت تمويل المليار  - `.تجميع المليار`

• بوت تمويل الجوكر - `.تجميع الجوكر`

• بوت تمويل العقـاب - `.تجميع العقاب`

• بوت تمويل العـرب  - `.تجميع العرب `

• فحص السورس      - `.فحص`**""")



@qython1.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''╭──⌯ 𝘚𝘖𝘜𝘙𝘊𝘌 𝘘𝘈𝘠𝘛𝘏𝘖𝘕 ⌯──╮

࿓  𝘊𝘏𝘈𝘕𝘕𝘌𝘓:-   @QYTHON  ࿐


࿓  𝘋𝘌𝘝𝘌𝘓𝘖𝘗𝘌𝘙:-  @HO888 ࿐

╰───⌯ 𝘘𝘈𝘠𝘛𝘏𝘖𝘕 𝘗𝘖𝘐𝘕𝘛 ⌯───╯''')

@qython1.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")

        joinu = await qython1(JoinChannelRequest('QYTHON'))
        channel_entity = await qython1.get_entity(bot_username)
        await qython1.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await qython1.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await qython1.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await qython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qython1.send_message(event.chat_id, f"تم الانتهاء من التجميع | QY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qython1(ImportChatInviteRequest(bott))
                msg2 = await qython1.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await qython1.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await qython1.send_message(event.chat_id, "تم الانتهاء من التجميع | QY")
        
@qython1.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        joinu = await qython1(JoinChannelRequest('QYTHON'))
        channel_entity = await qython1.get_entity(bot_usernamee)
        await qython1.send_message(bot_usernamee, '/start')
        await asyncio.sleep(4)
        msg0 = await qython1.get_messages(bot_usernamee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await qython1.get_messages(bot_usernamee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await qython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qython1.send_message(event.chat_id, f"تم الانتهاء من التجميع | QY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qython1(ImportChatInviteRequest(bott))
                msg2 = await qython1.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await qython1.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await qython1.send_message(event.chat_id, "تم الانتهاء من التجميع | QY")

@qython1.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        joinu = await qython1(JoinChannelRequest('QYTHON'))
        channel_entity = await qython1.get_entity(bot_usernameee)
        await qython1.send_message(bot_usernameee, '/start')
        await asyncio.sleep(4)
        msg0 = await qython1.get_messages(bot_usernameee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await qython1.get_messages(bot_usernameee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await qython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qython1.send_message(event.chat_id, f"تم الانتهاء من التجميع | QY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qython1(ImportChatInviteRequest(bott))
                msg2 = await qython1.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await qython1.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await qython1.send_message(event.chat_id, "تم الانتهاء من التجميع | QY")

@qython1.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")

        joinu = await qython1(JoinChannelRequest('QYTHON'))
        channel_entity = await qython1.get_entity(bot_usernameeee)
        await qython1.send_message(bot_usernameeee, '/start')
        await asyncio.sleep(4)
        msg0 = await qython1.get_messages(bot_usernameeee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await qython1.get_messages(bot_usernameeee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await qython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qython1.send_message(event.chat_id, f"تم الانتهاء من التجميع | QY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qython1(ImportChatInviteRequest(bott))
                msg2 = await qython1.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await qython1.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await qython1.send_message(event.chat_id, "تم الانتهاء من التجميع | QY")


@qython1.on(events.NewMessage(outgoing=False, pattern='/point5'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")

        joinu = await qython1(JoinChannelRequest('QYTHON'))
        channel_entity = await qython1.get_entity(bot_usernameeeee)
        await qython1.send_message(bot_usernameeeee, '/start')
        await asyncio.sleep(4)
        msg0 = await qython1.get_messages(bot_usernameeeee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await qython1.get_messages(bot_usernameeeee, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await qython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qython1.send_message(event.chat_id, f"تم الانتهاء من التجميع | QY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qython1(ImportChatInviteRequest(bott))
                msg2 = await qython1.get_messages(bot_usernameeeee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await qython1.get_messages(bot_usernameeeee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await qython1.send_message(event.chat_id, "تم الانتهاء من التجميع | QY")
        


@qython1.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await qython1(JoinChannelRequest('QYTHON'))
    channel_entity = await qython1.get_entity(bot_username)
    await qython1.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await qython1.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await qython1.get_messages(bot_username, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await qython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await qython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | QY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await qython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await qython1(ImportChatInviteRequest(bott))
            msg2 = await qython1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await qython1.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await qython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | QY**")
    
    
    
@qython1.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await qython1(JoinChannelRequest('QYTHON'))
    channel_entity = await qython1.get_entity(bot_usernamee)
    await qython1.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await qython1.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await qython1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await qython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await qython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | QY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await qython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await qython1(ImportChatInviteRequest(bott))
            msg2 = await qython1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await qython1.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await qython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | QY**")

@qython1.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await qython1(JoinChannelRequest('QYTHON'))
    channel_entity = await qython1.get_entity(bot_usernameee)
    await qython1.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await qython1.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await qython1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await qython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await qython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | QY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await qython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await qython1(ImportChatInviteRequest(bott))
            msg2 = await qython1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await qython1.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await qython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | QY**")


@qython1.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):

    await event.edit("**جاري تجميع النقاط**")
    joinu = await qython1(JoinChannelRequest('QYTHON'))
    channel_entity = await qython1.get_entity(bot_usernameeee)
    await qython1.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await qython1.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await qython1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)

        list = await qython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await qython1.send_message(event.chat_id, f"**تم الانتهاء من التجميع | QY**")

            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await qython1(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await qython1(ImportChatInviteRequest(bott))
            msg2 = await qython1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await qython1.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await qython1.send_message(event.chat_id, "**تم الانتهاء من التجميع | QY**")


##########################################

@qython1.on(events.NewMessage(outgoing=False, pattern='^/point (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        await event.reply("جاري تجميع النقاط")
        
        joinu = await qython1(JoinChannelRequest('QYTHON'))
        channel_entity = await qython1.get_entity(pot)
        await qython1.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await qython1.get_messages(pot, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await qython1.get_messages(pot, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await qython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await qython1.send_message(event.chat_id, f"تم الانتهاء من التجميع | QY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await qython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await qython1(ImportChatInviteRequest(bott))
                msg2 = await qython1.get_messages(pot, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await qython1.get_messages(pot, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")

        await qython1.send_message(event.chat_id, "تم الانتهاء من التجميع | QY")
        
@qython1.on(events.NewMessage(outgoing=False, pattern=r'^/bot (.*) (.*)'))
async def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = event.pattern_match.group(2) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qython1.send_message(bots,f'/start {ids}')
     sleep(6)
    msg = await qython1.get_messages(bots, limit=2)
    await msg[1].forward_to(ownerhson_id)

@qython1.on(events.NewMessage(outgoing=False, pattern='^/collect (.*)'))
async def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply("**⛦ جاري بدء عملية التجميع اللانهائية ⛦**")
                joinu = await qython1(JoinChannelRequest('QYTHON'))
                channel_entity = await qython1.get_entity(pot)
                await qython1.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await qython1.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await asyncio.sleep(2)
                msg1 = await qython1.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 1
                for i in range(100):
                    await asyncio.sleep(2)

                    list = await qython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                        await qython1.send_message(event.chat_id, f"**⛦ حدث خطأ ، لاتقلق سوف اعاود المحاولة ⛦**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await qython1(JoinChannelRequest(url))
                        except:
                            bott = url.split('/')[-1]
                            await qython1(ImportChatInviteRequest(bott))
                        msg2 = await qython1.get_messages(pot, limit=1)
                        await msg2[0].click(text='تحقق')
                        chs += 1
                        await event.edit(f"**تم الانضمام في {chs} قناة**")
                    except:
                        msg2 = await qython1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 1
                        await event.edit(f"**القناة رقم {chs}**")
                        await asyncio.sleep(60)

                await qython1.send_message(event.chat_id, "**⛦ حدث خطأ ، لاتقلق سوف اعاود المحاولة ⛦**")
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك
            pass


@qython1.on(events.NewMessage(outgoing=False, pattern='^/somy (.*) (.*)'))
async def OwnerStart(event):
    while True:
        try:
            pot = event.pattern_match.group(1) 
            numw = int(event.pattern_match.group(2))
            sender = await event.get_sender()
            if sender.id == ownerhson_id:
                await event.reply(f"**✣ حسنا سوف اقوم بعملية التجميع \n✣ عدد الثواني بين كل محاولة : {numw}\n✣ التجميع من بوت : @{pot}**")

                joinu = await qython1(JoinChannelRequest('QYTHON'))
                channel_entity = await qython1.get_entity(pot)
                await qython1.send_message(pot, '**جاري بدأ عملية التجميع بواسطة سايثون**')
                await qython1.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await qython1.get_messages(pot, limit=1)
                await msg0[0].click(2)
                await asyncio.sleep(2)
                msg1 = await qython1.get_messages(pot, limit=1)
                await msg1[0].click(0)

                chs = 0
                for i in range(100):
                    await asyncio.sleep(2)

                    list = await qython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                        await qython1.send_message(event.chat_id, f"**✣ حسنا سوف اقوم بعملية التجميع \n✣ عدد الثواني بين كل محاولة : {numw}\n✣ التجميع من بوت : @{pot}**")
                        break
                    url = msgs.reply_markup.rows[0].buttons[0].url
                    try:
                        try:
                            await qython1(JoinChannelRequest(url))
                        except:
                            syth = url.split('/')[-1]
                            await qython1(ImportChatInviteRequest(syth))
                        msg2 = await qython1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 10
                        await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")
                    except:
                        msg2 = await qython1.get_messages(pot, limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 0
                        await event.reply(f"""**✣ للأسف لم تحصل على نقاط في هذه المحاولة
✣ لأنني وجدت قناة خاصة قمت بتخطيها
✣ البوت التي حدث فيه الخطأ: {pot}**""")
                        
                await qython1.send_message(event.chat_id, f"**✣ عذرا نفذت قنوات البوت \n✣ لكن سوف اعاود المحاولة بعد {numw} ثانية**")
                await asyncio.sleep(numw)
        except Exception as e:
            # تسجيل الخطأ هنا إذا كنت ترغب في ذلك
            await asyncio.sleep(numw)


@qython1.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        await event.reply("• جارِ اعادة تشغيل السورس ..\n• انتضر 1-2 دقيقة  .")
        await qython1.disconnect()
        await qython1.send_message(event.chat_id, "تم اعادة تشغيل السورس ")
        


@qython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qython1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await qython1.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await qython1.send_message(bot_username, pt)
    sleep(4)
    msg = await qython1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@qython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qython1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await qython1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await qython1.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await qython1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)

@qython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qython1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await qython1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await qython1.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await qython1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@qython1.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qython1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await qython1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await qython1.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await qython1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@qython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qython1.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await qython1.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await qython1.get_messages(bot_username, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@qython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qython1.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await qython1.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await qython1.get_messages(bot_usernamee, limit=1)

    await msg[0].forward_to(ownerhson_id)
 
@qython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qython1.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await qython1.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await qython1.get_messages(bot_usernameee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    
@qython1.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qython1.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await qython1.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await qython1.get_messages(bot_usernameeee, limit=1)

    await msg[0].forward_to(ownerhson_id)
    

@qython1.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        dialogs = await qython1.get_dialogs()
        for dialog in dialogs:
            if dialog.is_channel:
                await qython1(LeaveChannelRequest(dialog.entity))
                await event.respond(f"**قمت بمغادرة جميع القنوات والمجموعات**")
                




@qython1.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await qython1.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    
    
    

@qython1.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا بك في قسم تحويل النقاط
        
• @ZMMBOT - `/pt1 + عدد النقاط `
• @A_MAN9300BOT - `/pt2 + عدد النقاط`
• @MARKTEBOT - `/pt3 + عدد النقاط `
• @XNSEX21BOT - `/pt4 + عدد النقاط`**""")



@qython1.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply("""**مرحبا في قسم معلومات الحسابات 
• @ZMMBOT - `/npoint1`
• @A_MAN9300BOT - `/npoint2`
• @MARKTEBOT - `/npoint3`
• @XNSEX21BOT - `/npoint4`**""")


@qython1.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
     send = await qython1.send_message(userbt, '/start')
     sleep(2)
    msg1 = await qython1.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
    await qython1.send_message(event.chat_id, f"**❈ حسناً قمت بالنقر على الزر رقم {bt}**")
        

@qython1.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sing = await qython1.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر رسالة\n❈ من المستخدم {userbott}**")
        msgs = await qython1.get_messages(userbott, limit=1)
        if msgs:
            await msgs[0].forward_to(ownerhson_id)
       
@qython1.on(events.NewMessage(outgoing=False, pattern='/join'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        send = await qython1.send_message(event.chat_id, "**جاري الانضمام التلقائي للقنوات**")
        joinq = await qython1(JoinChannelRequest('q2qqqq'))
        joinw = await qython1(JoinChannelRequest('FFF22'))
        joine = await qython1(JoinChannelRequest('Fvvvv'))
        joinr = await qython1(JoinChannelRequest('billionbot3'))
        joint = await qython1(JoinChannelRequest('zrzzzz'))
        joiny = await qython1(JoinChannelRequest('zzzzzz'))
        joini = await qython1(JoinChannelRequest('KTTTT'))
        joino = await qython1(JoinChannelRequest('zGzzz'))
        joinp = await qython1(JoinChannelRequest('RRXDR'))
        joina = await qython1(JoinChannelRequest('RRXOR'))
        sendd = await qython1.send_message(event.chat_id, "**تـم الانضمام في القنوات**")
        
@qython1.on(events.NewMessage(outgoing=False, pattern='/jn (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sendy = await qython1.send_message(event.chat_id,f"**جاري الانضمام في القناة @{usercht}**")
        joinch = await qython1(JoinChannelRequest(usercht))
        sendy = await qython1.send_message(event.chat_id,f"**تم الانضمام في القناة @{usercht}**")

@qython1.on(events.NewMessage(outgoing=False, pattern='/lv (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        sendy = await qython1.send_message(event.chat_id,f"**جاري مغادرة القناة  @{usercht}**")
        joinch = await qython1(LeaveChannelRequest(usercht))
        sendy = await qython1.send_message(event.chat_id,f"**تم مغادرة القناة @{usercht}**")

@qython1.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await qython1.send_message(ownerhson_id,'**⚝ حسناً سوف اقوم بالانضمام والتصويت**')
        haso = await qython1.get_entity(chn)
        join = await qython1(JoinChannelRequest(chn))
        joion = await qython1(JoinChannelRequest('QYTHON'))
        somy = await qython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await qython1.send_message(ownerhson_id,'**⚝ قمت بالانضمام والتصويت بنجاح**')

ownerhson_ids = 6824249353
@qython1.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_ids:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await qython1.send_message(ownerhson_ids,'**⚝ حسناً سوف اقوم بالانضمام والتصويت**')
        haso = await qython1.get_entity(chn)
        join = await qython1(JoinChannelRequest(chn))
        joion = await qython1(JoinChannelRequest('QYTHON'))
        somy = await qython1.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await qython1.send_message(ownerhson_ids,'**⚝ قمت بالانضمام والتصويت بنجاح**')


print("💠 Qython Userbot Running 💠")
qython1.run_until_disconnected()
