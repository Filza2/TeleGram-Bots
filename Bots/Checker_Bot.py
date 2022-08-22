import time,requests,random,datetime
from telegram import *
from telegram.ext import *
req=requests.session()
tims=datetime.datetime.now()
timo=tims.strftime('%I:%M %p  [%x]')
#By @TweakPY - @vv1ck

IDDD=""#Owner id  
IDDDDD=""#user id
IDDDD=""#owenr id 2 
token=""#Token
token_admin=""  # Token bot admin to receive login messages     
print(f'Done {timo} \n ')
back1 = [[InlineKeyboardButton("رجوع للخلف 🔙", callback_data="returns")]]
back2 = InlineKeyboardMarkup(back1)
repqd=[[InlineKeyboardButton("المطور👨🏻‍",url="https://t.me/TweakPY")]]
users_reply_markup=InlineKeyboardMarkup(repqd)
def tiktok5(update, _, query):
    count = 0
    remaining = 1000
    available = 0
    notavailable = 0
    done = 0
    user = ""
    Keyboard_check = [
        [InlineKeyboardButton(f"❇️ يوزر:{user}", url="https://t.me/TweakPY")],
        [InlineKeyboardButton(f"📜 العدد المتبقي:{remaining}", url="https://t.me/TweakPY")],
        [InlineKeyboardButton(f"❔ مفحوص:{done}", url="https://t.me/TweakPY")],
        [InlineKeyboardButton(f"✅ متاح:{available}", url="https://t.me/TweakPY"),
         InlineKeyboardButton(f"❌ غير متاح:{notavailable}", url='https://t.me/TweakPY')],
    ]
    InlineKeyboardMarkup(Keyboard_check)
    length = int(5)
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890_"
    try:
        while True:
            time.sleep(1.2)
            if count < 1000:
                count += 1
                remaining -= 1
                for user in range(1):
                    user = ""
                    for item in range(length):
                        user += random.choice(chars)
                urltik = f'https://www.tiktok.com/@{user}?'
                headertik = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'ar',
                    'cookie': 'bm_sz=D629F4942531777D6F7147A73605EDCB~YAAQhVQqLrT8ldN3AQAAvY4T+ArC4uvjnuxrV9pt2l0rKHkp1yqSFyVmqphzleo0kRsXlfI+NbB+LOM88S46yTNKJFjRIpTtPq9rKwsrBBAAkfcyq8+RZH7/Zf6msaZJtLNn/zxAtwnratRpub7m5xD5rufF7yyEZj5G5HxIutar/qCFiClDrwMZN4g39vBR; tt_webid_v2=6935404800675710465; tt_webid=6935404800675710465; tt_csrf_token=FHAWXV6vFZXlSM2eXSRS_6r1; MONITOR_WEB_ID=6935404800675710465; R6kq3TV7=AGOZE_h3AQAArT8QptQP5vh_zveCf-y5-BiUgB0w7IMZfUWedXYgJcIz57M8|1|0|75dd6b518f206372e6d404294a187c94b8126b35; s_v_web_id=verify_kltf64da_CijHZlfi_FdX3_4WE8_9Wwj_IAzVIICoeMBw; csrf_session_id=b2c399a35aae464682b040c14d913de2; bm_mi=DA047E87F2170B8EAEED36DFA89B7EEF~bFZTXUHt/x7P3I0BVhrEb4Td9L8oZ2GpyXZfW+xchO9i3D+JVDz88ASSnmIDwoAj9eNBEr2CRBfBybeh1gzxhUQkMpaXPauZmHFnxobirm+t2tUztvSHjRe7wVmEAzher5o6mgZFo3yICvGZj7Gl0DyAKf9IiMHUCT+P8WchaRo1zn2Tw+i7zcYmVNPFfKCWvBcFurSr7yHOl1W8DBZeM4NciHkWUQ4ZfRSnka5nPBc31710HS6gQL31mYIk5MCC2YzSf89SGSJodJGAkp1fZA==; bm_sv=7C1373BFC9FD4E0464B305E04E391F85~zYvKe8AvrP//Bh3yGBkN9hPkGyzM7JmwI5oyhbcxUHmMaMVX7A54ASSE97V9odLFyKW4B+RTI+2G3FqAeKElYXB+bw5DGu2vwRq89tI2ByGHuHWfJNmJPt+MLaUA1zVjxulAySr/HmXVp82syg2Hct0OfKH5FotWYANjWbWlwVU=; ak_bmsc=546A35303DC5B1DC24F699698FF233DC2E2A54854E2B0000EF813F605E1F4B1A~plMbX0Ui2pNYPSS/i1qPeHNc2xCUddsUFoAOF7Gbmm02GwXrVhn+fZfkeLsnlVZk33Fr4MD6SaesEjx/FclzePXXzOhSiJQ2GdQ996OpIB8lX+kjgVtkeQBXxQ139Neumt8jckA7jT81sgEzIDOZmLO6/KSDSaK95vwDjYEALYND6n9oYpmykVu2KGQYzRg6WueWyO0OrXSINNYmdYO7SF8ktYdO0didVcLX8JwAsFOIli2c6Ou6lhvuvoQeJClQQg; _abck=16220A303EE334985E7B40A39E10EC7F~0~YAAQhVQqLgT9ldN3AQAAwyUV+AUdqGmQv3CIqQnIyXwZFxf1lLyDf3M0i4kSrb/oGfOh9haoEWo2QxMzarNFIHPVzvja0C0ozETE+OS5CBaAx9+79ehyau7EX/wo3QgpVs1CS4v3sh0hclzVhl5LlwXtkCE3e3RCdvbNHXJiBpRf/+MD9HGuPlG1Ns83Auxj/eN8lMXLP3lQng/5xGgcDwXlNWO97iimgzB7FFhMa8cvLh5+7ua4P5HQ3T6O2WJAZZHsqK58z/u1W8NjeSUXh0dqrerPIc10L2hIcOpo6dGkFdG/SX/n9oqWpS4O8A3V640cN3rXoCb9JQFJZBrdRV/qJcpLt2ZdHby+/Igbtq1TFf6CD55L6DCvH8Q1pb1qA8z2zv9Rx1xyiXTnsYwY/YxCqyQrMPvK~-1~||-1||~-1',
                    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
                }
                send = req.get(urltik, headers=headertik)
                if send.status_code == 404:
                    available += 1
                    done += 1
                    Keyboard_check = [
                        [InlineKeyboardButton(f"❇️ يوزر:{user}", url="https://t.me/TweakPY")],
                        [InlineKeyboardButton(f"📜 العدد المتبقي:{remaining}", url="https://t.me/TweakPY")],
                        [InlineKeyboardButton(f"❔ مفحوص:{done}", url="https://t.me/TweakPY")],
                        [InlineKeyboardButton(f"✅ متاح:{available}", url="https://t.me/TweakPY"),
                         InlineKeyboardButton(f"❌ غير متاح:{notavailable}", url='https://t.me/TweakPY')],
                    ]
                    reply_markup_check = InlineKeyboardMarkup(Keyboard_check)
                    query.edit_message_text(
                        text=f"""تشيكر تيك توك خماسيات""",
                        reply_markup=reply_markup_check
                    )
                    query.message.reply_text(
                        text=f"[✅] استلم الجديد\n[⥮]اليوزر: {user}",
                        reply_markup=users_reply_markup
                    )
                else:
                    notavailable += 1
                    done += 1
                    Keyboard_check = [
                        [InlineKeyboardButton(f"❇️ يوزر:{user}", url="https://t.me/TweakPY")],
                        [InlineKeyboardButton(f"📜 العدد المتبقي:{remaining}", url="https://t.me/TweakPY")],
                        [InlineKeyboardButton(f"❔ مفحوص:{done}", url="https://t.me/TweakPY")],
                        [InlineKeyboardButton(f"✅ متاح:{available}", url="https://t.me/TweakPY"),
                         InlineKeyboardButton(f"❌ غير متاح:{notavailable}", url='https://t.me/TweakPY')],
                    ]
                    reply_markup_check = InlineKeyboardMarkup(Keyboard_check)
                    query.edit_message_text(
                        text=f"""تشيكر تيك توك خماسيات""",
                        reply_markup=reply_markup_check
                    )
                time.sleep(1)
            else:
                break
        query.edit_message_text(
            text=f"[❇️] Done Checking {count} users\n[✅] Available: {available}\n[❌] Not Available: {notavailable}",
            reply_markup=back2)
    except:
        pass

def tiktok4(update, _, query):
    count = 0
    remaining = 1000
    available = 0
    notavailable = 0
    done=0
    user = ""
    length = int(4)
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890_"
    try:
        while True:
            time.sleep(1.2)
            if count < 1000:
                count += 1
                remaining -= 1
                for user in range(1):
                    user = ""
                    for item in range(length):
                        user += random.choice(chars)
                urltik = f'https://www.tiktok.com/@{user}?'
                headertik = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'ar',
                    'cookie': 'bm_sz=D629F4942531777D6F7147A73605EDCB~YAAQhVQqLrT8ldN3AQAAvY4T+ArC4uvjnuxrV9pt2l0rKHkp1yqSFyVmqphzleo0kRsXlfI+NbB+LOM88S46yTNKJFjRIpTtPq9rKwsrBBAAkfcyq8+RZH7/Zf6msaZJtLNn/zxAtwnratRpub7m5xD5rufF7yyEZj5G5HxIutar/qCFiClDrwMZN4g39vBR; tt_webid_v2=6935404800675710465; tt_webid=6935404800675710465; tt_csrf_token=FHAWXV6vFZXlSM2eXSRS_6r1; MONITOR_WEB_ID=6935404800675710465; R6kq3TV7=AGOZE_h3AQAArT8QptQP5vh_zveCf-y5-BiUgB0w7IMZfUWedXYgJcIz57M8|1|0|75dd6b518f206372e6d404294a187c94b8126b35; s_v_web_id=verify_kltf64da_CijHZlfi_FdX3_4WE8_9Wwj_IAzVIICoeMBw; csrf_session_id=b2c399a35aae464682b040c14d913de2; bm_mi=DA047E87F2170B8EAEED36DFA89B7EEF~bFZTXUHt/x7P3I0BVhrEb4Td9L8oZ2GpyXZfW+xchO9i3D+JVDz88ASSnmIDwoAj9eNBEr2CRBfBybeh1gzxhUQkMpaXPauZmHFnxobirm+t2tUztvSHjRe7wVmEAzher5o6mgZFo3yICvGZj7Gl0DyAKf9IiMHUCT+P8WchaRo1zn2Tw+i7zcYmVNPFfKCWvBcFurSr7yHOl1W8DBZeM4NciHkWUQ4ZfRSnka5nPBc31710HS6gQL31mYIk5MCC2YzSf89SGSJodJGAkp1fZA==; bm_sv=7C1373BFC9FD4E0464B305E04E391F85~zYvKe8AvrP//Bh3yGBkN9hPkGyzM7JmwI5oyhbcxUHmMaMVX7A54ASSE97V9odLFyKW4B+RTI+2G3FqAeKElYXB+bw5DGu2vwRq89tI2ByGHuHWfJNmJPt+MLaUA1zVjxulAySr/HmXVp82syg2Hct0OfKH5FotWYANjWbWlwVU=; ak_bmsc=546A35303DC5B1DC24F699698FF233DC2E2A54854E2B0000EF813F605E1F4B1A~plMbX0Ui2pNYPSS/i1qPeHNc2xCUddsUFoAOF7Gbmm02GwXrVhn+fZfkeLsnlVZk33Fr4MD6SaesEjx/FclzePXXzOhSiJQ2GdQ996OpIB8lX+kjgVtkeQBXxQ139Neumt8jckA7jT81sgEzIDOZmLO6/KSDSaK95vwDjYEALYND6n9oYpmykVu2KGQYzRg6WueWyO0OrXSINNYmdYO7SF8ktYdO0didVcLX8JwAsFOIli2c6Ou6lhvuvoQeJClQQg; _abck=16220A303EE334985E7B40A39E10EC7F~0~YAAQhVQqLgT9ldN3AQAAwyUV+AUdqGmQv3CIqQnIyXwZFxf1lLyDf3M0i4kSrb/oGfOh9haoEWo2QxMzarNFIHPVzvja0C0ozETE+OS5CBaAx9+79ehyau7EX/wo3QgpVs1CS4v3sh0hclzVhl5LlwXtkCE3e3RCdvbNHXJiBpRf/+MD9HGuPlG1Ns83Auxj/eN8lMXLP3lQng/5xGgcDwXlNWO97iimgzB7FFhMa8cvLh5+7ua4P5HQ3T6O2WJAZZHsqK58z/u1W8NjeSUXh0dqrerPIc10L2hIcOpo6dGkFdG/SX/n9oqWpS4O8A3V640cN3rXoCb9JQFJZBrdRV/qJcpLt2ZdHby+/Igbtq1TFf6CD55L6DCvH8Q1pb1qA8z2zv9Rx1xyiXTnsYwY/YxCqyQrMPvK~-1~||-1||~-1',
                    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36'
                }
                send = req.get(urltik, headers=headertik)
                if send.status_code == 404:
                    done += 1
                    available += 1
                    Keyboard_check = [
                        [InlineKeyboardButton(f"❇️ يوزر:{user}", url="https://t.me/TweakPY")],
                        [InlineKeyboardButton(f"📜 العدد المتبقي:{remaining}", url="https://t.me/TweakPY")],
                        [InlineKeyboardButton(f"❔ مفحوص:{done}", url="https://t.me/TweakPY")],
                        [InlineKeyboardButton(f"✅ متاح:{available}", url="https://t.me/TweakPY"),
                         InlineKeyboardButton(f"❌ غير متاح:{notavailable}", url='https://t.me/TweakPY')],
                    ]
                    reply_markup_check = InlineKeyboardMarkup(Keyboard_check)
                    query.edit_message_text(
                        text=f"""تشيكر تيك توك رباعيات""",
                        reply_markup=reply_markup_check
                    )
                    query.message.reply_text(
                        text=f"[✅] استلم الجديد\n[⥮]اليوزر: {user}",
                        reply_markup=users_reply_markup
                    )
                else:
                    done += 1
                    notavailable += 1
                    Keyboard_check = [
                        [InlineKeyboardButton(f"❇️ يوزر:{user}", url="https://t.me/TweakPY")],
                        [InlineKeyboardButton(f"📜 العدد المتبقي:{remaining}", url="https://t.me/TweakPY")],
                        [InlineKeyboardButton(f"❔ مفحوص:{done}", url="https://t.me/TweakPY")],
                        [InlineKeyboardButton(f"✅ متاح:{available}", url="https://t.me/TweakPY"),
                         InlineKeyboardButton(f"❌ غير متاح:{notavailable}", url='https://t.me/TweakPY')],
                    ]
                    reply_markup_check = InlineKeyboardMarkup(Keyboard_check)
                    query.edit_message_text(
                        text=f"""تشيكر تيك توك رباعيات""",
                        reply_markup=reply_markup_check
                    )
                time.sleep(1)
            else:
                break
        query.edit_message_text(
            text=f"Done Checking {count} Users.\nAvailable: {available}\n[❌] Not Available: {notavailable}",
            reply_markup=back2)
    except:
        pass
def insta5(update, _, query):
    count = 0
    remaining = 1000
    available = 0
    notavailable = 0
    done = 0
    user = ""
    length = int(5)
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890_"
    while True:
        if count < 1000:
            count += 1
            remaining -= 1
            for user in range(1):
                user = ""
                for item in range(length):
                    user += random.choice(chars)
            urlinsta = f'https://www.instagram.com/{user}'
            headerinsta = {
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Google Chrome";v="89","Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
            }
            send = req.get(urlinsta, headers=headerinsta)
            if send.status_code == 404:
                available += 1
                done += 1
                Keyboard_check = [
                    [InlineKeyboardButton(f"❇️ يوزر:{user}", url="https://t.me/TweakPY")],
                    [InlineKeyboardButton(f"📜 العدد المتبقي:{remaining}", url="https://t.me/TweakPY")],
                    [InlineKeyboardButton(f"❔ مفحوص:{done}", url="https://t.me/TweakPY")],
                    [InlineKeyboardButton(f"✅ متاح:{available}", url="https://t.me/TweakPY"),
                     InlineKeyboardButton(f"❌ غير متاح:{notavailable}", url='https://t.me/TweakPY')],
                ]
                reply_markup_check = InlineKeyboardMarkup(Keyboard_check)
                query.edit_message_text(
                    text=f"""تشيكر انستقرام خماسيات""",
                    reply_markup=reply_markup_check
                )
                query.message.reply_text(
                    text=f"[✅] استلم الجديد\n[⥮]اليوزر: {user}",
                    reply_markup=users_reply_markup
                )
            else:
                notavailable += 1
                done += 1
                Keyboard_check = [
                    [InlineKeyboardButton(f"❇️ يوزر:{user}", url="https://t.me/TweakPY")],
                    [InlineKeyboardButton(f"📜 العدد المتبقي:{remaining}", url="https://t.me/TweakPY")],
                    [InlineKeyboardButton(f"❔ مفحوص:{done}", url="https://t.me/TweakPY")],
                    [InlineKeyboardButton(f"✅ متاح:{available}", url="https://t.me/TweakPY"),
                     InlineKeyboardButton(f"❌ غير متاح:{notavailable}", url='https://t.me/TweakPY')],
                ]
                reply_markup_check = InlineKeyboardMarkup(Keyboard_check)
                query.edit_message_text(
                    text=f"""تشيكر انستقرام خماسيات""",
                    reply_markup=reply_markup_check
                )
            time.sleep(1)
        else:
            break
    query.edit_message_text(
        text=f"[❇️] Done Checking {count} users\n[✅] Available: {available}\n[❌] Not Available: {notavailable}",
        reply_markup=back2)


def start(update: Update, _: CallbackContext):
    global user, pppppp
    user = str(update.message.from_user.username).upper()
    Keyboard = [
        [InlineKeyboardButton("⛏ قناه البوت", url='https://t.me/TweakPY'),
         InlineKeyboardButton("👨🏻‍💻 المطور", url='https://t.me/tweakpy')],
        [InlineKeyboardButton("🎵 تشيكر تيك", callback_data="tik")],
        [InlineKeyboardButton("💡 تشيكر انستا", callback_data="insta"),
         InlineKeyboardButton("❔ مساعده", callback_data="help")],
    ]
    reply_markup = InlineKeyboardMarkup(Keyboard)
    username = update.message.from_user.username
    idd = update.message.chat_id
    name=update.message.from_user.full_name
    ID = str(idd)
    textsend = f"""
━━━━━━*𝙽𝙴𝚆𝙻𝙾𝙶𝙸𝙽*━━━━━━
▫️𝙽𝙰𝙼𝙴: *{name}*    
▫️𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴: *@{username}*  
▫️𝙸𝙳: *{ID}*
▫️𝙱𝙾𝚃: *@{update.message.bot.username}*
⌛️𝚃𝙸𝙼𝙴: *{timo}*
━━━━━━*𝙽𝙴𝚆𝙻𝙾𝙶𝙸𝙽*━━━━━━"""
    tadk = (f'https://api.telegram.org/bot{token_admin}/sendMessage?chat_id={IDDD}&text={textsend}')
    if IDDD in ID:
        update.message.reply_text(
            text=f"""ارحب يالمطور الاساسي ارحب وياهلا بك ✪ """,
            reply_markup=reply_markup
        )
    elif IDDDD in ID:
        update.message.reply_text(
            text=f""" ارحب يالمطور الاساسي ارحب وياهلا بك ✪ """,
            reply_markup=reply_markup
        )
    elif "-" in ID:
        update.message.reply_text(
             text="I Am Sorry,\nI Don't Work In Groups/Channels.\n*I Am Leaving.*",
             parse_mode="MARKDOWN"
            )
        update.message.bot.leaveChat(
            chat_id=int(ID)
            )
    elif IDDDDD == ID:
        update.message.reply_text(
            text=f"""
{name}  ارحب ️️
""",

            reply_markup=reply_markup
        )
        pppppp = requests.post(tadk)
    else:
        pass


def returns(update, _, query):
    name = query.from_user.first_name
    Keyboard = [
        [InlineKeyboardButton("⛏ قناه البوت", url='https://t.me/TweakPY'),
         InlineKeyboardButton("👨🏻‍💻 المطور", url='https://t.me/TWeakpy')],
        [InlineKeyboardButton("🎵 تشيكر تيك", callback_data="tik")],
        [InlineKeyboardButton("💡 تشيكر انستا", callback_data="insta"),
         InlineKeyboardButton("❔ مساعده", callback_data="help")],
    ]
    reply_markup = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(
        text=f"""
{name}  ارحب ️️
""",

        reply_markup=reply_markup
    )
def tiktok(update, _, query):
    try:
        Keyboard = [
            [InlineKeyboardButton("5 حروف", callback_data="5tik")],
            [InlineKeyboardButton("4 حروف", callback_data="4tik")],
            [InlineKeyboardButton("رجوع للخلف 🔙", callback_data="returns")]
        ]
        reply_markup = InlineKeyboardMarkup(Keyboard)
        time.sleep(1.2)
        query.edit_message_text(
            text="اختار طول اليوزر الي يناسبك الفحص تومتيك يجي الف يوزر",
            reply_markup=reply_markup
        )
    except:
        pass
def instas(update, _, query):
    Keyboard = [
        [InlineKeyboardButton("5 حروف", callback_data="5insta")],
        [InlineKeyboardButton("رجوع للخلف 🔙", callback_data="returns")]
    ]
    reply_markup = InlineKeyboardMarkup(Keyboard)
    query.edit_message_text(
        text="اختار طول اليوزر الي يناسبك الفحص تومتيك يجي الف يوزر",
        reply_markup=reply_markup
    )
def help(update, _, query):
    tef = """
START MESSAGE
/start """
    query.edit_message_text(text=tef, reply_markup=back2)


def button(update: Update, _: CallbackContext):
    query = update.callback_query
    query.answer()
    choice = query.data
    if choice == "returns":
        returns(update=Update, _=CallbackContext, query=query)
    elif choice == "tik":
        tiktok(update=Update, _=CallbackContext, query=query)
    elif choice == "insta":
        instas(update=Update, _=CallbackContext, query=query)
    elif choice == "help":
        help(update=Update, _=CallbackContext, query=query)
    elif choice == "5tik":
        tiktok5(update=Update, _=CallbackContext, query=query)
    elif choice== "4tik":
        tiktok4(update=Update,_=CallbackContext,query=query)
    elif choice == "5insta":
        insta5(update=Update, _=CallbackContext, query=query)


def main():
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CallbackQueryHandler(button, run_async=True))
    dispatcher.add_handler(CommandHandler("start", start, run_async=True))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, start, run_async=True))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
