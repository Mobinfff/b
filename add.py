import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import TelegramClient , events , sync
from telethon.tl.functions.channels import InviteToChannelRequest
import os
import json
from telethon.tl.functions.messages import AddChatUserRequest

api_id ,api_hash = 12821795,"11302a8e320a6774bebc5800f05092c8"

with open('add.json','w') as v:
    d = {'mem':[]}
    json.dump(d,v)

kobscity = TelegramClient("Mr_Kobs" , api_id , api_hash)
kobscity.start()

@kobscity.on(events.NewMessage(outgoing=True, pattern='راهنما'))
async def crazy(event):
    await event.edit('''♨️ راهنمای اد گپ به گپ پایتون شهر کوبص :

❗️طرز کار ربات ب این شکله که میرید توی یک گروه و دستور get رو میزنید و بعد ربات شروع میکنه به جمع اوری ممبر ها
❕بعد از جمع کردن ممبرها شما دوباره میتونید برید توی یک گپ دیگه و ممبرهای اون رو هم جمع کنید
❗️بعد از زدن دستور get اول ♻️ رو میبینید که یعنی درحال جم کردن ممبر ها وقتی که ✅ رو دیدید یعنی ممبرا جمع شدند
❕حالا برای اد کردن ممبرها در گروه خودتون باید با اکانت ربات برید توی پیام های ذخیره شده یا....
❗️حالا باید دستور add رو بزنید و جلوش لینک یا ایدی گروهی که میخاید ربات توش ممبرارو بریزه رو بزنید مثلا:
❕add @KobsCity
❗️برای حذف کردن ممبرها از دیتابیس بعد از اد کردن اونها کافیه دستور del رو بزنید

‼️ توجه کنید ربات اگر بلاک باشه یا اد اون گروهی که میخاد بهش ممبر اضافه کنه بسته باشه نمیتونه ممبرارو اد کنه

**موفق باشید🌹**
Creator: Mr_Kobs
@KobsCity     <<<چنل ما
''')

@kobscity.on(events.NewMessage(outgoing=True,pattern='del'))
async def dele(event):
    os.remove('add.json')
    with open('add.json','w') as l:
        v = {'mem':[]}
        json.dump(v,l)
        await event.edit('با موفقیت پاک شد')

@kobscity.on(events.NewMessage(outgoing=True,pattern='get'))
async def get(event):
    await event.edit('♻️')
    with open('add.json','r') as v:
        add = json.load(v)
    chat = event.chat_id
    async for user in kobscity.iter_participants(chat):
            add['mem'].append(user.id)
    with open('add.json','w') as d:
        json.dump(add,d)
    await event.edit('✅')
    

@kobscity.on(events.NewMessage(outgoing=True, pattern='add'))
async def crazy(event):
    if event:
        with open('add.json','r') as fg:
            add = json.load(fg)
        await event.edit('درحال اد کردن ممبرها')
        chat = event.chat_id
        arg = event.raw_text.split(' ')
        chat = event.chat_id
        with open("add.json",'r') as vb:
            add = json.load(vb)
        try:
            await kobscity(InviteToChannelRequest(arg[1],add['mem']))
        except:
            await event.edit('فکر کنم من بلاک شدم نمیتونم اد کنم')
        await event.edit('اد شدند')
print('Bot Is Online')
kobscity.run_until_disconnected()
asyncio.get_event_loop().run_forever() 