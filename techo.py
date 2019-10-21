import telebot
import pyowm

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = "ru")
bot = telebot.TeleBot("945450664:AAGoBI6DH6eC5q4kJCuToLI8d1IsasIaTB8")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]

    answer = "В городе " + message.text + " cейчас " + w.get_detailed_status() + "\n"
    answer += "Температура сейчас около " + str(temp) + "\n\n"

    if temp < 10:
        answer += "Холодно, сейчас бы коньяку или водки для согреву!"
    elif temp < 20:
        answer += "Прохладно, выпей глинтвейна!"
    else:
        answer += "Температура нормальная, можно выпить по пиву"


    bot.send_message(message.chat.id, answer)

bot.polling( none_stop  = True)	
