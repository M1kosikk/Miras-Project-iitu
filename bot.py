import telebot
import random
from datetime import datetime

TOKEN = "8841967767:AAGfy7uEO_zZQxshf57heE1SP3ke_Pi24Tw"

bot = telebot.TeleBot(TOKEN)

subjects = {
    "физика": "Кабинет 305",
    "математика": "Кабинет 210",
    "программирование": "Кабинет 612",
    "английский": "Кабинет 115",
    "история": "Кабинет 221",
    "ВКС": "Кабинет 235",
    "SQL": "Кабинет 221"
}
answers = {
    "библиотека": "Библиотека работает с 9:00 до 18:00. Заходить со стороны Манаса",
    "wifi": "WiFi: IITU_FREE\nПароль: ваш логин и пароль от platonus",
    "общежитие": "Общежитие находится рядом с корпусом B.",
    "спортзал": "Спортзал работает до 20:00. На Ауезова",
    "буфет": "Буфет находится на нижнем этаже.",
    "медпункт": "Медпункт находится в кабинете 210."
}

tips = [
    "Не пропускай первые лекции — там объясняют требования.",
    "Записывай домашние задания сразу в телефон.",
    "Сдавай долги сразу, не откладывай на конец семестра.",
    "Используй студенческий билет — много скидок."
]

@bot.message_handler(commands=['start'])
def start(message):
    text = (
        "Привет! Я бот-помощник для первокурсников 🎓\n\n"
        "Что я умею:\n"
        "- Показывать кабинеты\n"
        "- Давать информацию о расписании\n"
        "- Показывать контакты\n\n"
        "Напиши название предмета.\n"
        "Например: физика"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['help'])
def help_command(message):
    text = (
        "Доступные команды:\n"
        "/start - запуск бота\n"
        "/help - помощь\n"
        "/schedule - расписание\n"
        "/contacts - контакты\n"
        "/rooms - все кабинеты\n"
        "/tip - совет дня\n"
        "/time - текущее время\n"
        "/faq - частые вопросы"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['schedule'])
def schedule(message):
    text = (
        "Расписание:\n"
        "Понедельник - Физика\n"
        "Вторник - Математика\n"
        "Среда - Программирование"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['contacts'])
def contacts(message):
    text = (
        "Контакты университета:\n"
        "Деканат: +7 707 961 71 21\n"
        "Email: dekanat@university.kz"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['rooms'])
def rooms(message):
    text = "🏫 Кабинеты предметов:\n\n"
    for subject, room in subjects.items():
        text += f"• {subject} — {room}\n"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['tip'])
def tip(message):
    advice = random.choice(tips)
    bot.send_message(message.chat.id, f"💡 Совет дня:\n\n{advice}")

@bot.message_handler(commands=['time'])
def current_time(message):
    now = datetime.now()
    bot.send_message(
        message.chat.id,
        f"🕐 Дата: {now.strftime('%d.%m.%Y')}\n"
        f"⏰ Время: {now.strftime('%H:%M:%S')}"
    )

@bot.message_handler(commands=['faq'])
def faq(message):
    text = (
        "❓ Частые вопросы:\n\n"
        "Q: Где расписание?\nA: На сайте или у старосты.\n\n"
        "Q: Что при пропуске?\nA: Объяснительная в деканат.\n\n"
        "Q: Где распечатать?\nA: В библиотеке, 1-й этаж.\n\n"
        "Q: Как получить справку?\nA: Деканат с паспортом."
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: True)
def answer(message):
    user_text = message.text.lower().strip()

    if user_text == "":
        bot.send_message(message.chat.id, "Введите сообщение.")
        return

    if user_text in subjects:
        bot.send_message(
            message.chat.id,
            f"{user_text.title()} проходит в: {subjects[user_text]}"
        )
    elif user_text in answers:
        bot.send_message(message.chat.id, answers[user_text])
    else:
        bot.send_message(
            message.chat.id,
            "Я не знаю такого запроса.\nВведи /help для списка команд."
        )

print("Бот запущен...Можете писать")
bot.infinity_polling()