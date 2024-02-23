from telebot import types, TeleBot
from datetime import timedelta, datetime
from locale import setlocale, LC_ALL
import text
import json

setlocale(category=LC_ALL, locale="Russian")  # Настройка локализации для правильной работы datetime


API_TOKEN = "<api_token>"
bot = TeleBot(API_TOKEN)

with open("data.json", encoding="utf-8") as file:
	registered = json.load(file)
print(registered)


def write_file_registered():
	with open("data.json", "w", encoding="utf-8") as file:
		json.dump(registered, file, ensure_ascii=False)


@bot.message_handler(commands=['start'])
def start(message):
	"""Обработка команды /start. Подключение кнопок."""

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

	btn_today = types.KeyboardButton("📚 Расписание")
	btn_help = types.KeyboardButton("❓ Помощь")
	btn_calls = types.KeyboardButton("🔔 Звонки")

	markup.row(btn_today)
	markup.add(btn_calls, btn_help)

	bot.send_message(message.chat.id, text.start_text_message, reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
	today_date = datetime.today()
	tomorrow_date = today_date + timedelta(days=1)
	yesterday_date = today_date - timedelta(days=1)

	user_class = registered[str(callback.message.chat.id)]

	user_schedules = text.schedules[user_class]

	if callback.data == "tomorrow":
		beautiful_date = tomorrow_date.strftime('%d %b. %Y г.')  # Вывод даты в красивом формате
		schedule = user_schedules[tomorrow_date.weekday()]  # Получение расписания на определенный день недели
		markup = types.InlineKeyboardMarkup()

		btn_today = types.InlineKeyboardButton("📆 Расписание на сегодня", callback_data="today")
		markup.add(btn_today)

		text_message = f"📆 *Расписание уроков на {beautiful_date}*\n\n{schedule}\n\n👇 Вы также можете посмотреть расписание на сегодня."

		bot.send_message(callback.message.chat.id, text_message, parse_mode='Markdown', reply_markup=markup)


	elif callback.data == "yesterday":
		beautiful_date = yesterday_date.strftime('%d %b. %Y г.')  # Вывод даты в красивом формате
		schedule = user_schedules[yesterday_date.weekday()]  # Получение расписания на определенный день недели
		markup = types.InlineKeyboardMarkup()

		btn_today = types.InlineKeyboardButton("📆 Расписание на сегодня", callback_data="today")
		markup.add(btn_today)

		text_message = f"📆 *Расписание уроков на {beautiful_date}*\n\n{schedule}\n\n👇 Вы также можете посмотреть расписание на сегодня."

		bot.send_message(callback.message.chat.id, text_message, parse_mode='Markdown', reply_markup=markup)


	elif callback.data == "today":
		beautiful_date = today_date.strftime('%d %b. %Y г.')  # Вывод даты в красивом формате
		schedule = user_schedules[today_date.weekday()]  # Получение расписания на определенный день недели
		markup = types.InlineKeyboardMarkup()

		btn_tomorrow = types.InlineKeyboardButton("Вперед ▶️", callback_data="tomorrow")
		btn_yesterday = types.InlineKeyboardButton("◀️ Назад", callback_data="yesterday")

		markup.row(btn_yesterday, btn_tomorrow)

		text_message = f"📆 *Расписание уроков на {beautiful_date}*\n\n{schedule}\n\n👇 Вы также можете посмотреть расписание на завтра."

		bot.send_message(callback.message.chat.id, text_message, parse_mode='Markdown', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_messages(message):
	today_date = datetime.today()
	tomorrow_date = today_date + timedelta(days=1)

	user_input = message.text.lower()
	user_schedules = None

	if str(message.chat.id) in registered:
		user_class = registered[str(message.chat.id)]

		user_schedules = text.schedules[user_class]

		print(f"{message.chat.id}({user_class}) - {user_input}")


	elif user_input in text.schedules.keys():
		registered[message.chat.id] = user_input
		bot.send_message(message.chat.id, "Вы успешно зарегистрировались!")

		user_class = user_input
		user_schedules = text.schedules[user_class]

		print(f"{message.chat.id}({user_class}) - {user_input}")

	if str(message.chat.id) not in registered:
		bot.send_message(message.chat.id,
						 "Пожалуйста, зарегистрируйтесь, указав номер и букву класса. \n\nНапример: 9Г, 11а, 8В.",
						 parse_mode='Markdown')

	elif user_input in ("📚 расписание", "/today", "today", "расписание"):
		"Вывод расписания на текущий день"

		beautiful_date = today_date.strftime('%d %b. %Y г.')  # Вывод даты в красивом формате
		schedule = user_schedules[today_date.weekday()]  # Получение расписания на определенный день недели
		markup = types.InlineKeyboardMarkup()

		btn_tomorrow = types.InlineKeyboardButton("Вперед ▶️", callback_data="tomorrow")
		btn_yesterday = types.InlineKeyboardButton("◀️ Назад", callback_data="yesterday")

		markup.row(btn_yesterday, btn_tomorrow)

		text_message = f"📆 *Расписание уроков на {beautiful_date}*\n\n{schedule}\n\n👇 Вы также можете посмотреть расписание на завтра."

		bot.send_message(message.chat.id, text_message, parse_mode='Markdown', reply_markup=markup)

	elif user_input in ("/tomorrow", "завтра", "tomorrow"):
		"Вывод расписания на завтрашний день"

		beautiful_date = tomorrow_date.strftime('%d %b. %Y г.')  # Вывод даты в красивом формате
		schedule = user_schedules[tomorrow_date.weekday()]  # Получение расписания на определенный день недели
		markup = types.InlineKeyboardMarkup()

		btn_today = types.InlineKeyboardButton("📆 Расписание на сегодня", callback_data="today")

		markup.add(btn_today)

		text_message = f"📆 *Расписание уроков на {beautiful_date}*\n\n{schedule}\n\n👇 Вы также можете посмотреть расписание на сегодня."

		bot.send_message(message.chat.id, text_message, parse_mode='Markdown', reply_markup=markup)

	elif user_input in ("❓ помощь", "помощь", "/help", "help"):
		"Вывод сообщения с командами"

		bot.send_message(message.chat.id, text.help_text_message, parse_mode='Markdown')

	elif user_input in ("/calls", "calls", "звонки", "звонок", "🔔 звонки"):
		"Расписание расписание звонков"

		markup = types.InlineKeyboardMarkup()
		btn_today = types.InlineKeyboardButton("Расписание на сегодня", callback_data="today")
		markup.add(btn_today)

		bot.send_message(message.chat.id, text.calls_text_message, parse_mode='Markdown', reply_markup=markup)

	elif user_input in ("/teachers", "teachers", "учителя"):
		bot.send_message(message.chat.id, text.teachers_text_message, parse_mode='Markdown')

	elif user_input in ("/groups", "groups", "группы"):
		"""Список классов и кабинет их классного руковоителя, а также в каком классе они сейчас"""
		bot.send_message(message.chat.id,
						 "У меня нет этих данных( \nЕсли вы ими обладаете скинте их разработчику ( @Klimvill ), пожалуйста.")

	elif user_input in ("/person", "person"):
		"Рассписание конкретного человека из школы, например, учителя, ученика"
		bot.send_message(message.chat.id,
						 "У меня нет этих данных( \nЕсли вы ими обладаете скинте их разработчику ( @Klimvill ), пожалуйста.")

	elif user_input in ("понедельник", "пн", "monday", "/monday", "mon"):
		bot.send_message(message.chat.id, f"📆 *Расписание уроков на понедельник*\n\n{user_schedules[0]}",
						 parse_mode='Markdown')

	elif user_input in ("вторник", "вт", "tuesday", "/tuesday", "tue"):
		bot.send_message(message.chat.id, f"📆 *Расписание уроков на вторник*\n\n{user_schedules[1]}",
						 parse_mode='Markdown')

	elif user_input in ("среда", "ср", "wednesday", "/wednesday", "wed"):
		bot.send_message(message.chat.id, f"📆 *Расписание уроков на среду*\n\n{user_schedules[2]}",
						 parse_mode='Markdown')

	elif user_input in ("четверг", "чт", "thursday", "/thursday", "thu"):
		bot.send_message(message.chat.id, f"📆 *Расписание уроков на четверг*\n\n{user_schedules[3]}",
						 parse_mode='Markdown')

	elif user_input in ("пятница", "пт", "friday", "/friday", "fri"):
		bot.send_message(message.chat.id, f"📆 *Расписание уроков на пятницу*\n\n{user_schedules[4]}",
						 parse_mode='Markdown')

	elif user_input in ("суббота", "сб", "saturday", "/saturday", "sat"):
		bot.send_message(message.chat.id, f"📆 *Расписание уроков на субботу*\n\n{user_schedules[5]}",
						 parse_mode='Markdown')

	elif user_input in ("воскресенье", "вс", "sunday", "/sunday", "sun"):
		bot.send_message(message.chat.id, f"📆 *Расписание уроков на воскресенье*\n\n{user_schedules[6]}",
						 parse_mode='Markdown')


	elif user_input in ("/links", "links", "ссылки"):
		bot.send_message(message.chat.id, "Ссылки на школьные порталы")

	elif user_input in ("/register", "регистрация", "register"):
		del registered[str(message.chat.id)]

	elif user_input in ("/add_class_chat", "add_class_chat", "добавить"):
		"Добавление, в чат класса"
		...

	elif user_input in "/save_data" and message.chat.id == 5980441769:
		write_file_registered()
		bot.send_message(message.chat.id, "Данные сохранены!")

	else:
		bot.send_message(message.chat.id, " Чтобы ознакомится со всеми функциями почитайте /help.")


bot.polling()
