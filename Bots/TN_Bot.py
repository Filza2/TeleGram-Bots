import time,requests,urllib3.request,datetime,random
from telegram import *
from instabot import Bot
from telegram.ext import *
import cowsay
r=requests.session()
global IDDD,IDDDD,IDDDDD,token,timo
tims=datetime.datetime.now()
timo=tims.strftime('%I:%M %p  [%x]')
IDDD=""#Owner id
IDDDD=""#owner id 2
token_admin=""#Token bot admin to receive login messages
IDDDDD=""#user id
token=''#token
#By @TweakPY - @vv1ck

cowsay.trex("@TweakPY-@vv1ck \n\n\nCHECK TIK\nComments TIK\nReport insta\nComments insta")
def pt(update,context):
    try:
        i=''.join(context.args)
        if i=="":
            update.message.reply_text(text="Enter a post url")
            while True:
                break
        else:
            h=str(i.split('?')[0].split('/')[5])
            update.message.reply_text(text='post id:'+str(h))
    except:
        pass
def post(update,context):
    try:
        b=Bot
        postt = ''.join(context.args)
        if postt=="":
            update.message.reply_text(text="Enter a post url")
            while True:
                break
        else:
            ida=b.get_media_id_from_link(self='',link=postt)
            update.message.reply_text(text=f"post id:{ida}")
    except:pass
def tik(update,context:CallbackContext):
    try:
        sw = ''.join(context.args)
        if sw == "":
            update.message.reply_text(text=f"[🆔] Please Enter your session id")
            while True:
                break
        else:
            update.message.reply_text(text=f"[🆔] {sw}\n\n[▶️] remaining:1000\n\n[❓] length:4")
            count = 0
            remaining = 1000
            user = ""
            length = int(4)
            chars = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
            while True:
                time.sleep(1.2)
                if count < 500:
                    count += 1
                    remaining -= 1
                    for user in range(1):
                        user = ""
                        for item in range(length):
                            user += random.choice(chars)
                    url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id=" + user + "&app_language=ar"
                    payload = ""
                    headers = {
                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                                "Connection": "close",
                                "Host": "www.tiktok.com",
                                "Accept-Encoding": "gzip, deflate",
                                "Cache-Control": "max-age=0"}
                    cookies = {'sessionid': sw}
                    response = requests.request("GET", url, data=payload, headers=headers, cookies=cookies)
                    post = str(response.json()["status_msg"])
                    if post=="":
                        update.message.reply_text(text=f"NEW USER SIR [✅]\n\n[⥮] username : @{user}\n\n[⌛] Time:{timo}\n\n[@TweakPY]-[@vv1ck]")
                    else:
                        update.message.reply_text(text=f"{remaining}")
                    time.sleep(0.9)
                else:
                    break
    except:
        pass
def tm(update,context):
    try:
        done = 0
        r = requests.session()
        okey = ' '.join(context.args)
        tx = okey.split(":")[0]
        postid = okey.split(":")[1]
        sessionid = okey.split(":")[2]
        update.message.reply_text(text=f"""[🛠] info confirm\n\n[✳️] text:{tx}\n\n[🛂] session id:{sessionid}\n\n[❇️] post id:{postid}\n\n[📡] auto sleep has been set to [6.6]\n\n[#️⃣] auto spam comments has been set to [100] comment\n\n""")
        update.message.reply_text(text=f"""[🔒] now locked to post id \n{postid}""")
        url = f"https://www.tiktok.com/api/comment/publish/?aid=1988&app_name=tiktok_web&device_platform=web&referer=https:%2F%2Fwww.tiktok.com%2F&root_referer=https:%2F%2Fwww.tiktok.com%2F&user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F90.0.4430.93+Safari%2F537.36&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=ar&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F90.0.4430.93+Safari%2F537.36&browser_online=true&ac=4g&timezone_name=Asia%2FBahrain&priority_region=BH&verifyFp=verify_kmwy2hf4_AmVogh0N_Tkne_4BpA_ANSq_9oOueM2pIh3s&appId=1233&region=BH&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=windows&did=6944589237636646401&tt-web-region=BH&uid=6957894826579641349&aweme_id={postid}&text={tx}&device_id=6944589237636646401&_signature=_02B4Z6wo00101xegn7AAAIDAKCYplETPOLsXoJsAAKVx98"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '0',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': f'tt_webid_v2=6944589237636646401; tt_webid=6944589237636646401; s_v_web_id=verify_kmwy2hf4_AmVogh0N_Tkne_4BpA_ANSq_9oOueM2pIh3s; tt_csrf_token=dQmMg8Uekbw2Oq3qWeMzmZPV; csrf_session_id=53caf56337014635982064c815fd0b40; R6kq3TV7=APBQKTB5AQAARUF0d_OQ-94UVu51UTkJV6aMnxLDIekq-bfbknTR1okfl63_|1|0|27675acbbb7f3bf62040a83a6038ebc361ab9539; ak_bmsc=1C37B7EFB848AACA78C6A86D2E98F4472E2A548E28340000BD668F60218C611A~plMf9kvndtWdGMYA6ntojGLjZAnbo9JL/O3k0tlMDA/bnO2xhgSlQPPClh0dOgGSaun5sLRBrfmGZ2EZStGoGE8ZvuGNl7JDdOJ+vMkSPg8ONxn/pue9pK75OI1uenyR8+BSuBg0l/4nl8Gkz2mC4jTKnu2W8fm8vyijAPGEy9dHMGeHevdaKji8TeHmTmmz+qIM2AqFZBgMiLtpZqfNfN3vFoeaojuT1oOXdwCP/j6P4=; bm_sz=F2EFD804894550F3CA53C6456C64DB72~YAAQjlQqLhK1DiB5AQAA/1MpMAudG6Do3bfpbNxInp+UTsyWegkW8B64MgSviKu0pp5V6Fhluh66SzeqUvOsChOxFC+JDudD3O+1JSYqWBdunXgsvsM1RiFfvonoaen5R1R+Y0DbcTkKaCo/9sii4e9IYFF6icxq+NHilHnVzugyLNeBoXWWdMejkyg1M6bJ; _abck=D689B4F48527BC79C2A79217632F331E~0~YAAQjlQqLhO1DiB5AQAA/1MpMAVWkY7o8DGEfut8tpMTkcOrYGsuzI00y8cmKO/os7ywHsi5UeafSAqlHSEyTY8wbVoei6XMgYICIMnoZ8tCQe8nzK9j3h5K+aYRq+C7U7YFp0vToH1HZBDYtynCuZqOmKSoZ5CymLYStP97xIyliQ2+hOFddb2GUSlZ/p4lSupiCDj3XximHvlm7r746WAF3MBJC4JAqedluFI3UkebwX8A87Y3DDK4iAqVeDyKLjlKJ2scqw/5anKng648GEBMYJr2Sx1M8Ph6bct1qCSMXsm/lUlJMXn9YHxMXnM9tSCgovhpCSjHokc3o1DXebuNR+BWl4FDeZ3rdMMec+Mrf7UbHWapraXB7V1hRyI2dSIAlG86Mg6PFL79KgGmpQ8PQuD2q30t~-1~-1~-1; passport_csrf_token=45de29b0fdd44543ae03ebca1712aba9; passport_csrf_token_default=45de29b0fdd44543ae03ebca1712aba9; ttwid=1%7C76-Am_AM-jdvsHzB1lr6PLsnCSwMEQmDmftstnJM4c4%7C1620011314%7C98e8f2f8df0f69b0d8133eab649605fa3487dba3c89a7632aaeeddd6b8b0ed51; sid_guard={sessionid}%7C1620011343%7C5184000%7CFri%2C+02-Jul-2021+03%3A09%3A03+GMT; uid_tt=1cb4ab185b6df7ced107550b73cba72dc6ae4d5d36a5b360202bf9712f73db6e; uid_tt_ss=1cb4ab185b6df7ced107550b73cba72dc6ae4d5d36a5b360202bf9712f73db6e; sid_tt={sessionid}; sessionid={sessionid}; sessionid_ss={sessionid}; store-idc=alisg; store-country-code=bh; cmpl_token=AgQQAPNZF-RMpbCxht16_B08-gG6LbPKf4PSYPhliQ; MONITOR_WEB_ID=6944589237636646401; odin_tt=a0e48820809040f306cc53f7c451b11dc8b0dcc1a0a154e9aa47bc3b460120ce2073a7979a3ba19fd724b00c8968968fd494a2299079c4607d3d3d5fdcbd1a12996f7fc7e82bc35ba3623247430e4e58; bm_sv=313B67CA31A48965C7AAD5944033B58E~Lso3XobClkO+2LgPELng8uvbHFQCpeycIWyhPae5NVMiuMlyoz2pWZbwQ6Z6gAO5arGhNfLqdCy0HQaYdIdEQanEAPwyfc0vmFH4fXTNkKg9xGR3OVK9Euo8BXuHIw3clCQpN6/kAXDBufMKkXmOhTF55BEqEYKxm+UDNHlZYAo=',
            'origin': 'https://www.tiktok.com',
            'referer': f'https://www.tiktok.com/@volleyboll_dear/video/{postid}?is_copy_url=1&is_from_webapp=v1',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'tt-csrf-token': 'dQmMg8Uekbw2Oq3qWeMzmZPV',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
        while True:
            time.sleep(6.6)
            req = requests.post(url, headers=headers)
            if url==url:
                update.message.reply_text(f'[✅] DONE SEND COMMENT [{tx}]\n[💣] conut [{done}]')
                done += 1
                if done == 101:
                    break
    except Exception as tmerror:
        print("ops u have error in tiktok comments ==>",tmerror)
def cm(update,context):
    global tx,slp,go,headLG,datLG
    try:
        done=0
        r = requests.session()
        okey = ' '.join(context.args)
        user = okey.split(":")[0]
        pess = okey.split(":")[1]
        tx = okey.split(":")[2]
        idd = okey.split(":")[3]
        update.message.reply_text(text=f"""[🛠] info confirm\n\n[✳️] user:{user}\n\n[🛂] password:{pess}\n\n[❇️] post id:{idd}\n\n[📡] auto sleep has been set to [6.6]\n\n[#️⃣] auto spam comments has been set to [100] comment\n\n[*] your msg [{tx}]""")
        slp = int(7.1)
        urLG = "https://www.instagram.com/accounts/login/ajax/"
        headLG = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '272',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; shbid=6144; shbts=1614374582.8963153',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '790551e77c76',
        'x-requested-with': 'XMLHttpRequest'}
        datLG = {
        "username": user,
        "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{pess}",
        "queryParams": "{}",
        "optIntoOneTap": "false"}
        go = r.post(urLG, headers=headLG, data=datLG)
        if ("userId") in go.text:
            update.message.reply_text(text=f"""تم تسجيل دخول للحساب بنجاح [✅]""")
            update.message.reply_text(text=f"""[🔒] now locked to post id \n{idd}""")
            sis = go.cookies['sessionid']
            urCOm = 'https://www.instagram.com/web/comments/{}/add/'.format(idd)
            hedCOM = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '44',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; csrftoken=wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi; ds_user_id=46165248972; sessionid=' + sis,
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/p/CMmx4KOpnx6/',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'x-csrftoken': 'wYPaFI4U1osqOiXc2Tv5vOsNgTdBwrxi',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgYkq',
            'x-instagram-ajax': '753ce878cd6d',
            'x-requested-with': 'XMLHttpRequest'}
            daCOM = {
                'comment_text': tx,
                'replied_to_comment_id': ''}
            while True:
                time.sleep(slp)
                ct = r.post(urCOm, headers=hedCOM, data=daCOM)
                if '"status":"ok"' in ct.text:
                    update.message.reply_text(f'[✅] DONE SEND COMMENT [{tx}]\n[💣] conut [{done}]')
                    done += 1
                    if done==101:
                        break
                elif 'Please' in ct.text:
                    update.message.reply_text(text='\n[‼️] ERROR SEND COMMENT - BAN ')
                elif ("two_factor") in go.text:
                    update.message.reply_text(text='\n[⛔️] Binary verification \n')
                    break
                elif ("checkpoint_url") in go.text:
                    update.message.reply_text(text='\n[⚠️] Account Secure \n')
                    break
                else:
                    update.message.reply_text(text='\n[✖️] The username or password is wrong ! \n')
                    break
    except Exception as cmerror:
        print("ops u have error in tiktok comments ==>", cmerror)
def target(update,context):
    try:
        okey = ' '.join(context.args)
        filza445 = okey.split(":")[0]
        FLOZ20 = okey.split(":")[1]
        floz70 = okey.split(":")[2]
        done = 0
        update.message.reply_text(text=f"""[🛠] info confirm\n\n[✳️] user:{filza445}\n\n[🛂] password:{FLOZ20}\n\n[❇️] target:{floz70}\n\n[📡] auto sleep has been set to [4.5]\n\n[#️⃣] auto spam reports has been set to [100] report""")
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '296',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'x-csrftoken': 'MPicCBRW0thEKbRdX9DhiTL6UB0nGtqV',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR1Y1dEsDcV-xq-u_7U0XISuyjCpWSS-VvmOhVU2N6rp9zg7',
            'x-instagram-ajax': 'f65d2f981648',
            'x-requested-with': 'XMLHttpRequest'}
        data = {
            'username': f'{filza445}',
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{FLOZ20}',
            'queryParams': '{}',
            'optIntoOneTap': 'false'}
        filza5448 = r.post(url, headers=headers, data=data)
        if '"authenticated":true' in filza5448.text:
            update.message.reply_text(text=f"""تم تسجيل دخول للحساب بنجاح [✅]""")
            update.message.reply_text(text=f"""[🔒] Target has been locked now spam to user:{floz70}""")
            r.headers.update({'x-csrftoken': filza5448.cookies['csrftoken']})
            sl = int(4.5)
            url_id = 'https://www.instagram.com/{}/?__a=1'.format(floz70)
            req_id = r.get(url_id).json()
            user_id = str(req_id['logging_page_id'])
            ffilza2000 = user_id.split('_')[1]
            while True:
                url_spam = 'https://www.instagram.com/users/{}/report/'.format(ffilza2000)
                data_spam = {
                'source_name': '',
                'reason_id': 1,
                'frx_context': ''}
                solo = r.post(url_spam, data=data_spam)
                update.message.reply_text(f'[✅] DONE SPAM USER [{floz70}]\n[💣] conut [{done}]')
                time.sleep(sl)
                done += 1
                if done == 101:
                    break
        elif ('checkpoint_required') in filza5448.text:
            update.message.reply_text(text=f"""[⚠️] SECURE!!!""")
        elif ('"user":true,"authenticated":false') in filza5448.text:
            update.message.reply_text(text=f"""[✖️] WRONG PASSWORD!!!""")
        elif filza5448.status_code == "429":
            update.message.reply_text(text=f"""[⛔️] YOU HAVE BAN!""")
        elif ('"user":false') in filza5448.text:
            update.message.reply_text(text=f"""[❗️] USERNAME WAS NOT FOUND!!!""")
        else:
            update.message.reply_text(text="""[‼️] ERROR_CODE 404!""")
    except Exception as reportinstaerror:
        print("ops u have error in tiktok comments ==>", reportinstaerror)
def start(update: Update,context: CallbackContext):
    global user,pppppp,tadk
    try:
        user = str(update.message.from_user.username).upper()
        name = update.message.from_user.first_name
        idd = update.message.chat_id
        ID = str(idd)
        url_url_user = f"tg://user_id?={ID}"
        sosoa = f'Free bot src(report insta+cm insta+cmtiktok+tiktok checker)\n\n𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄: {name}\n𝐈𝐃: {ID}\n𝐔𝐒𝐄𝐑 𝐔𝐑𝐋: {url_url_user}\nTOKEN: {token}\n𝐓𝐈𝐌𝐄: {timo}'
        tadk = (f'https://api.telegram.org/bot{token_admin}/sendMessage?chat_id={IDDD}&text={sosoa}')
        if IDDD in ID:
            update.message.reply_text(text=f""" اهلا عزيزي المطور منور البوت قلبي ✪ """)
        elif IDDDD in ID:
            update.message.reply_text(text=f""" اهلا عزيزي المطور منور البوت قلبي ✪ """)
        elif "-" in ID:
            update.message.reply_text(text="https://t.me/TweakPY")
            update.message.reply_text(text=
"""عذرا البوت لايعمل بالمجموعات!
Sorry, the bot does not work 
in groups!
@TweakPY - @vv1ck
""")
        elif IDDDDD == ID:
            update.message.reply_text(text="@TweakPY - @vv1ck")
            update.message.reply_text(
            text=f"""
📅 🆃🅸🅼🅴:{timo}

By @TweakPY - @vv1ck
WELCOME BOOS {name} ♥️️

reports Instagram 
comments instagram
tiktok comments
tiktok checker

رجاء اضغط هنا قبل بدء الاستخدام 🚷:
/help
""")
            pppppp = requests.post(tadk)        
        else:
            pass
    except:
        pass
    return main
def help(update,context):
    tef="""
start message - by @TweakPY - @vv1ck
طريقه استخدام بلاغات الانستا:
/target user:pass:target
مثال:
/target joker24:jok123456789:tjoker
------------------------------------
طريقه استخدام كومنتات الانستا:
/cm user:pass:msg:post id 
مثال:
/cm joker:jok123456789:test:216599595599
-------------------------------------
طريقه استخدام استخراج ايدي البوست للانستا:
/post url
مثال:
/post https://instagram.aodjopjasd.caispo554
-------------------------------------
طريقه استخدام كومنتات التيك توك:
/tm your message:post id:session id
مثال:
/tm test_tweakPY:597997977978979879797:dioass5a4d65as4dad4as5d4sa65
-------------------------------------
طريقه استخدام تشيكر تيك توك الي بالسيشن:
/tik sess id 
مثال:
/tik oajk6456sa565as5dasd6adas8sad98aasd
--------------------------------------------
طريقه استخدام استخراج ايدي البوست لتيك توك:
/pt url
مثال:
/pt https://tiktok.aodjopjasd.caispo554

 
/start """
    update.message.reply_text(tef)
def main() -> None:
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    start_command_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_command_handler)
    help_command_handler = CommandHandler('help', help)
    dispatcher.add_handler(help_command_handler)
    hw = CommandHandler('target', target)
    dispatcher.add_handler(hw)
    hsw = CommandHandler('cm', cm)
    dispatcher.add_handler(hsw)
    hssw = CommandHandler('post', post)
    dispatcher.add_handler(hssw)
    hsasw = CommandHandler('tm', tm)
    dispatcher.add_handler(hsasw)
    hsssssw = CommandHandler('tik', tik)
    dispatcher.add_handler(hsssssw)
    hsssssw = CommandHandler('pt', pt)
    dispatcher.add_handler(hsssssw)
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
