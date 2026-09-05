import telebot
from telebot import types
import logging

BOT_TOKEN = "8618170953:AAGYuK_BoSlr2us6JYsr1yDpIbnopwX7JAQ"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

bot = telebot.TeleBot(BOT_TOKEN)

# ID премиум-эмодзи (можно взять у бота @getidsbot)
ICON_BELL = "6039486778597970865"      # 🔔
ICON_SEND = "6039573425268201570"      # 📤
ICON_STAR = "6034923938486684992"      # ⭐️

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    # Кнопка с каналом (синяя + иконка колокольчика)
    btn_channel = types.InlineKeyboardButton(
        "Перейти в канал",
        url="https://t.me/vocmaq",
        style="primary",
        icon_custom_emoji_id=ICON_BELL
    )
    
    # Кнопка с ботом (зелёная + иконка отправки)
    btn_bot = types.InlineKeyboardButton(
        "Перейти в бота",
        url="https://t.me/vocmabot",
        style="success",
        icon_custom_emoji_id=ICON_SEND
    )
    
    markup.add(btn_channel, btn_bot)
    
    bot.send_message(
        message.chat.id,
        "👋 Здравствуйте!\n\n"
        "Мы переехали в нового бота. Этот бот стал переходником, "
        "вся работа теперь ведётся в новом боте.\n\n"
        "Просим прощения за временные неудобства. Чтобы продолжить "
        "пользоваться, нажмите на кнопку ниже и переходите в нового бота. "
        "Там всё то же самое, просто под новым именем и на более стабильном боте.",
        reply_markup=markup,
        parse_mode="HTML"
    )

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    start(message)  # Просто вызываем ту же функцию

if __name__ == '__main__':
    print("✅ Бот-переходник запущен...")
    bot.infinity_polling(timeout=60, long_polling_timeout=30)
