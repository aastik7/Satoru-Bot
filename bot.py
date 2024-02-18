from dotenv import load_dotenv
import os 
import telebot
import requests

load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")



@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    print("Received /horoscope command")
    text = "What's your zodiac sign?\nChoose one: *Aries*, *Taurus*, *Gemini*, *Cancer,* *Leo*, *Virgo*, *Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)

def day_handler(message):
    sign = message.text
    print(f"Received zodiac sign: {sign}")
    text = "What day do you want to know?\nChoose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date in format YYYY-MM-DD."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    # Here, we use lambda function to pass both sign and message
    bot.register_next_step_handler(sent_msg, lambda msg: fetch_horoscope(msg, sign.capitalize()))

def fetch_horoscope(message, sign):
    day = message.text
    print(f"Received day: {day}")
    horoscope = get_daily_horoscope(sign, day)
    if horoscope.get("error"):
        bot.send_message(message.chat.id, "Sorry, I couldn't fetch the horoscope for that day.")
    else:
        data = horoscope["data"]
        horoscope_message = f'*Horoscope:* {data["horoscope_data"]}\n*Sign:* {sign}\n*Day:* {data["date"]}'
        bot.send_message(message.chat.id, "Here's your horoscope!")
        bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")


def get_daily_horoscope(sign: str, day: str) -> dict:
    url = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
    params = {"sign": sign, "day": day}
    response = requests.get(url, params)
    return response.json()

print("Bot is running...")
bot.infinity_polling()
