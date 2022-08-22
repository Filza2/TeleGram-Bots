from requests import get,post
from telegram import *
from telegram.ext import *
#by @TweakPY - @vv1ck
token=""
ID=""
repqd=[[InlineKeyboardButton("المطور👨🏻‍",url="https://t.me/TweakPY")]]
weather_reply_markup=InlineKeyboardMarkup(repqd)
re=post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=HI please type [/weather] or [/start]')
def weather(update:Update,context:CallbackContext):
    try:
        con=''.join(context.args)
        if con=='':
            update.message.reply_text(text="[!!] Error you must enter a country name")
            while True:
                break
        else:
            cont=con.split(" ")        
            send=post(f"http://api.weatherapi.com/v1/current.json?key=33495cb83c0441efb79151844212505&q=${cont}&aqi=no")
            update.message.reply_text(text=f'{str(send.text)}',reply_markup=weather_reply_markup)
    except:
        pass
def start(update: Update, _: CallbackContext):
    name=update.message.from_user.full_name
    idd=update.message.chat_id
    ID=str(idd)
    if "-" in ID:
        update.message.reply_text(
             text="I Am Sorry,\nI Don't Work In Groups/Channels.\n*I Am Leaving.*",
             reply_markup=weather_reply_markup,
             parse_mode="MARKDOWN"
            )
        update.message.bot.leaveChat(
            chat_id=int(ID)
            )
    else:
        update.message.reply_text(text=f"""
*Hi* 
[[?]] to *start* /*weather* [name of the country]
    
[[@TweakPY - @vv1ck]]
""",reply_markup=weather_reply_markup,parse_mode="MARKDOWN")
def main():
    updater=Updater(token, use_context=True)
    dispatcher=updater.dispatcher
    dispatcher.add_handler(CommandHandler('weather', weather,run_async=True))
    dispatcher.add_handler(CommandHandler("start", start , run_async=True))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
