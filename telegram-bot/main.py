import json
import threading

from time import sleep
from telebot import TeleBot, types
from config import *
from data.text_messages import *
from datetime import datetime, time, timedelta
from locale import setlocale, LC_ALL

setlocale(category=LC_ALL, locale="Russian")  # Настройка локализации для правильной работы datetime

with open("/telegram-bot/data/registered_users.json", encoding="utf-8") as file:
	registered_users = json.load(file)

with open("/telegram-bot/data/schedules.json", encoding="utf-8") as file:
	schedules = json.load(file)

bot = TeleBot(API_TOKEN, parse_mode="Markdown")


def write_file_registered():
	"""Запись зарегистрированных пользователей в файл registered_users.json"""
	with open("/telegram-bot/data/registered_users.json", "w", encoding="utf-8") as file:
		json.dump(registered_users, file, ensure_ascii=False)


def checking_user_registered(chat_id: int) -> bool:
	"""Проверка зарегистрирован ли пользователь"""
	if str(chat_id) in registered_users:
		return True
	else:
		bot.send_message(chat_id,
						 "Пожалуйста, зарегистрируйтесь, написав в чат номер и букву класса. \n\nНапример: 9Г, 11а, 8В.")
		return False


def get_lesson_number(number_lessons: int):
	"""Получение номера текущего урока"""
	current_time = datetime.now().time()

	if time(0, 0) <= current_time <= time(8, 0): lesson = -1
	elif time(8, 0) <= current_time <= time(8, 40): lesson = 0
	elif time(8, 40) <= current_time <= time(9, 35) and number_lessons >= 2: lesson = 1
	elif time(9, 35) <= current_time <= time(10, 30) and number_lessons >= 3: lesson = 2
	elif time(10, 30) <= current_time <= time(11, 25) and number_lessons >= 4: lesson = 3
	elif time(11, 25) <= current_time <= time(12, 20) and number_lessons >= 5: lesson = 4
	elif time(12, 20) <= current_time <= time(13, 10) and number_lessons >= 6: lesson = 5
	elif time(13, 10) <= current_time <= time(13, 55) and number_lessons >= 7: lesson = 6
	elif time(13, 10) <= current_time <= time(15, 00) and number_lessons >= 8: lesson = 7
	elif time(15, 00) <= current_time <= time(15, 45) and number_lessons >= 9: lesson = 8
	else: lesson = "Уроки кончились"

	return lesson


def massMailing(message):
	"""Функция, которая рассылает сообщения всем зарегистрированным пользователям"""
	if message.text == "/exit":
		bot.send_message(message.chat.id, "Вы вышли из режима массовой рассылки"); return
	elif message.text is not None:
		for id_chat in registered_users.keys():
			bot.send_message(id_chat, message.text)
	elif message.photo is not None:
		for id_chat in registered_users.keys():
			bot.send_photo(id_chat, message.photo[0].file_id, caption=message.caption)
	elif message.audio is not None:
		for id_chat in registered_users.keys():
			bot.send_audio(id_chat, message.audio.file_id, caption=message.caption)
	elif message.document is not None:
		for id_chat in registered_users.keys():
			bot.send_document(id_chat, message.document.file_id, caption=message.caption)
	elif message.video is not None:
		for id_chat in registered_users.keys():
			bot.send_video(id_chat, message.video.file_id, caption=message.caption)
	else:
		bot.send_message(message.chat.id, "К сожалению возникла ошибка"); return

	bot.send_message(message.chat.id, "Рассылка прошла успешно!")


def create_schedule(short_version: bool, beautiful_date, schedule_day):
	"""Создание текста расписания"""
	number = None
	count = 1

	text_message = f"📆 *Расписание уроков на {beautiful_date}*\n"

	if schedule_day != "Выходной":
		if short_version:
			for value in schedule_day:
				if value == "":
					text_message += "\n\n*Внеурочки*"
				else:
					text_message += f"\n{count}. {value}"
					count += 1
		else:
			text_message = f"📆 *Расписание уроков на {beautiful_date}*\n"
			number_current_lesson = get_lesson_number(len(schedule_day))

			if schedule_day[number_current_lesson] == "": number = number_current_lesson
			if number is not None: number_current_lesson += 1

			if number_current_lesson == "Уроки кончились":
				text_message += "\n*Уроки кончились*\n"
			elif number_current_lesson == -1:
				text_message += f"\n*Будет - {schedule_day[0]}*\n"
			else:
				text_message += f"\n*Сейчас - {schedule_day[number_current_lesson]}*\n"

			for value in schedule_day:
				if value == "":
					text_message += "\n\n*Внеурочки*"
				else:
					text_message += f"\n{count}. {value}"
					count += 1

	else:
		text_message += "\n" + schedule_day

	return text_message


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
	today_date = datetime.today()

	user_registered = checking_user_registered(callback.message.chat.id)

	if user_registered:
		user_class = registered_users[str(callback.message.chat.id)]
		user_schedules = schedules[user_class]
	else:
		return

	if callback.data[:8] == "tomorrow":
		day = int(callback.data[8:])

		tomorrow_date = today_date + timedelta(days=day)

		beautiful_date = tomorrow_date.strftime('%d %b. %Y г.')  # Вывод даты в красивом формате
		schedule = user_schedules[str(tomorrow_date.weekday())]  # Получение расписания на определенный день недели
		markup = types.InlineKeyboardMarkup()

		btn_today = types.InlineKeyboardButton("📆 Расписание на сегодня", callback_data="today")
		btn_tomorrow = types.InlineKeyboardButton("Вперед ▶️", callback_data=f"tomorrow{day + 1}")
		if day - 1 != 0:
			btn_yesterday = types.InlineKeyboardButton("◀️ Назад", callback_data=f"yesterday{day - 1}")
		else:
			btn_yesterday = types.InlineKeyboardButton("◀️ Назад", callback_data="today")

		markup.row(btn_today)
		markup.add(btn_yesterday, btn_tomorrow)

		text_message = create_schedule(True, beautiful_date, schedule)
		text_message += "\n\n👇 Вы также можете посмотреть расписание на сегодня."

		bot.send_message(callback.message.chat.id, text_message, reply_markup=markup)


	elif callback.data[:9] == "yesterday":
		day = int(callback.data[9:])

		yesterday_date = today_date + timedelta(days=day)

		beautiful_date = yesterday_date.strftime('%d %b. %Y г.')  # Вывод даты в красивом формате
		schedule = user_schedules[str(yesterday_date.weekday())]  # Получение расписания на определенный день недели
		markup = types.InlineKeyboardMarkup()

		btn_today = types.InlineKeyboardButton("📆 Расписание на сегодня", callback_data="today")

		if day + 1 != 0:
			btn_tomorrow = types.InlineKeyboardButton("Вперед ▶️", callback_data=f"tomorrow{day + 1}")
		else:
			btn_tomorrow = types.InlineKeyboardButton("Вперед ▶️", callback_data="today")

		btn_yesterday = types.InlineKeyboardButton("◀️ Назад", callback_data=f"yesterday{day - 1}")
		markup.row(btn_today)
		markup.add(btn_yesterday, btn_tomorrow)

		text_message = create_schedule(True, beautiful_date, schedule)
		text_message += "\n\n👇 Вы также можете посмотреть расписание на сегодня."

		bot.send_message(callback.message.chat.id, text_message, reply_markup=markup)


	elif callback.data == "today":
		beautiful_date = today_date.strftime('%d %b. %Y г.')  # Вывод даты в красивом формате
		schedule = user_schedules[str(today_date.weekday())]  # Получение расписания на определенный день недели
		markup = types.InlineKeyboardMarkup()

		btn_tomorrow = types.InlineKeyboardButton("Вперед ▶️", callback_data="tomorrow1")
		btn_yesterday = types.InlineKeyboardButton("◀️ Назад", callback_data="yesterday-1")

		markup.row(btn_yesterday, btn_tomorrow)

		text_message = create_schedule(False, beautiful_date, schedule)
		text_message += "\n\n👇 Вы также можете посмотреть расписание на завтра."

		bot.send_message(callback.message.chat.id, text_message, parse_mode='Markdown', reply_markup=markup)


	elif callback.data == "teachers_1_sheet":
		markup = types.InlineKeyboardMarkup()

		btn_today = types.InlineKeyboardButton("Вперед ▶️", callback_data="teachers_2_sheet")
		markup.add(btn_today)

		bot.send_message(callback.message.chat.id, teachers_text_message, parse_mode='Markdown',
						 reply_markup=markup)

	elif callback.data == "teachers_2_sheet":
		markup = types.InlineKeyboardMarkup()

		btn_today = types.InlineKeyboardButton("◀️ Назад", callback_data="teachers_1_sheet")
		markup.add(btn_today)

		bot.send_message(callback.message.chat.id, teachers_text_message_2, parse_mode='Markdown',
						 reply_markup=markup)


@bot.message_handler(commands=["start"])
def start_message(message):
	"""Обработка команды /start. Подключение кнопок."""

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

	btn_today = types.KeyboardButton("📚 Расписание")
	btn_help = types.KeyboardButton("❓ Помощь")
	btn_calls = types.KeyboardButton("🔔 Звонки")

	markup.row(btn_today)
	markup.add(btn_calls, btn_help)

	bot.send_message(message.chat.id, start_text_message, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text.lower() in ("❓ помощь", "помощь", "/help", "help"))
def help_message(message):
	"""Вывод сообщения с командами"""
	bot.send_message(message.chat.id, help_text_message, disable_web_page_preview=True)


@bot.message_handler(func=lambda message: message.text.lower() in schedules.keys())
def register(message):
	registered_users[str(message.chat.id)] = message.text.lower()

	bot.send_message(message.chat.id, "Вы успешно зарегистрировались!")


@bot.message_handler(func=lambda message: message.text.lower() in ("📚 расписание", "/today"))
def today(message):
	"""Вывод расписания на текущий день"""
	user_registered = checking_user_registered(message.chat.id)

	if user_registered:
		user_class = registered_users[str(message.chat.id)]
		user_schedules = schedules[user_class]
	else:
		return

	today_date = datetime.today()
	schedule_day = user_schedules[str(today_date.weekday())]  # Получение расписания на определенный день недели
	beautiful_date = today_date.strftime("%d %b. %Y г.")  # Вывод даты в красивом формате

	markup = types.InlineKeyboardMarkup()

	btn_tomorrow = types.InlineKeyboardButton("Вперед ▶️", callback_data="tomorrow1")
	btn_yesterday = types.InlineKeyboardButton("◀️ Назад", callback_data="yesterday-1")

	markup.row(btn_yesterday, btn_tomorrow)

	text_message = create_schedule(False, beautiful_date, schedule_day)
	text_message += "\n\n👇 Вы также можете посмотреть расписание на завтра."

	bot.send_message(message.chat.id, text_message, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text.lower() in ("/tomorrow", "завтра", "tomorrow"))
def tomorrow(message):
	"""Вывод расписания на завтрашний день"""
	user_registered = checking_user_registered(message.chat.id)

	if user_registered:
		user_class = registered_users[str(message.chat.id)]
		user_schedules = schedules[user_class]
	else:
		return

	tomorrow_date = datetime.today() + timedelta(days=1)
	schedule_day = user_schedules[str(tomorrow_date.weekday())]  # Получение расписания на определенный день недели
	beautiful_date = tomorrow_date.strftime("%d %b. %Y г.")  # Вывод даты в красивом формате

	markup = types.InlineKeyboardMarkup()

	btn_today = types.InlineKeyboardButton("📆 Расписание на сегодня", callback_data="today")

	markup.add(btn_today)

	text_message = create_schedule(True, beautiful_date, schedule_day)
	text_message += "\n\n👇 Вы также можете посмотреть расписание на сегодня."

	bot.send_message(message.chat.id, text_message, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text.lower() in ("/calls", "calls", "звонки", "звонок", "🔔 звонки"))
def calls(message):
	"""Расписание звонков"""
	markup = types.InlineKeyboardMarkup()
	btn_today = types.InlineKeyboardButton("📆 Расписание на сегодня", callback_data="today")
	markup.add(btn_today)

	bot.send_message(message.chat.id, calls_text_message, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text.lower() in ("/teachers", "teachers", "учителя"))
def teachers(message):
	"""Список учителей"""
	markup = types.InlineKeyboardMarkup()

	btn_today = types.InlineKeyboardButton("Вперед ▶️", callback_data="teachers_2_sheet")

	markup.add(btn_today)

	bot.send_message(message.chat.id, teachers_text_message, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text.lower() in ("/groups", "groups", "группы"))
def groups(message):
	"""Список классов и кабинет их классного руководителя, а также в каком классе они сейчас"""
	bot.send_message(message.chat.id,
					 "Тут будет список классов их кабинет, классный руководитель и, возможно, расписание")


@bot.message_handler(func=lambda message: message.text.lower() in ("/person", "person"))
def person(message):
	bot.send_message(message.chat.id,
					 "Тут можно будет находить людей или классы и узнать их расписание. Например, /person 9г и выводится расписание 9г")


@bot.message_handler(
	func=lambda message: message.text.lower() in ("/extralesson", "extralesson", "допы", "дополнительные занятия"))
def extraLesson(message):
	bot.send_message(message.chat.id, "В будущем вы сможете добавлять свои дополнительные занятия сюда")


@bot.message_handler(func=lambda message: message.text.lower() in ("понедельник", "пн", "monday", "/monday", "mon"))
def monday(message):
	user_registered = checking_user_registered(message.chat.id)

	if user_registered:
		user_class = registered_users[str(message.chat.id)]
		user_schedules = schedules[user_class]
	else:
		return

	text_message = create_schedule(True, "понедельник", user_schedules["0"])

	bot.send_message(message.chat.id, text_message)


@bot.message_handler(func=lambda message: message.text.lower() in ("вторник", "вт", "tuesday", "/tuesday", "tue"))
def tuesday(message):
	user_registered = checking_user_registered(message.chat.id)

	if user_registered:
		user_class = registered_users[str(message.chat.id)]
		user_schedules = schedules[user_class]
	else:
		return

	text_message = create_schedule(True, "вторник", user_schedules["1"])

	bot.send_message(message.chat.id, text_message)


@bot.message_handler(func=lambda message: message.text.lower() in ("среда", "ср", "wednesday", "/wednesday", "wed"))
def wednesday(message):
	user_registered = checking_user_registered(message.chat.id)

	if user_registered:
		user_class = registered_users[str(message.chat.id)]
		user_schedules = schedules[user_class]
	else:
		return

	text_message = create_schedule(True, "среду", user_schedules["2"])

	bot.send_message(message.chat.id, text_message)


@bot.message_handler(func=lambda message: message.text.lower() in ("четверг", "чт", "thursday", "/thursday", "thu"))
def thursday(message):
	user_registered = checking_user_registered(message.chat.id)

	if user_registered:
		user_class = registered_users[str(message.chat.id)]
		user_schedules = schedules[user_class]
	else:
		return

	text_message = create_schedule(True, "четверг", user_schedules["3"])

	bot.send_message(message.chat.id, text_message)


@bot.message_handler(func=lambda message: message.text.lower() in ("пятница", "пт", "friday", "/friday", "fri"))
def friday(message):
	user_registered = checking_user_registered(message.chat.id)

	if user_registered:
		user_class = registered_users[str(message.chat.id)]
		user_schedules = schedules[user_class]
	else:
		return

	text_message = create_schedule(True, "пятницу", user_schedules["4"])

	bot.send_message(message.chat.id, text_message)


@bot.message_handler(func=lambda message: message.text.lower() in ("суббота", "сб", "saturday", "/saturday", "sat"))
def saturday(message):
	user_registered = checking_user_registered(message.chat.id)

	if user_registered:
		user_class = registered_users[str(message.chat.id)]
		user_schedules = schedules[user_class]
	else:
		return

	text_message = create_schedule(True, "субботу", user_schedules["5"])

	bot.send_message(message.chat.id, text_message)


@bot.message_handler(func=lambda message: message.text.lower() in ("воскресенье", "вс", "sunday", "/sunday", "sun"))
def sunday(message):
	user_registered = checking_user_registered(message.chat.id)

	if user_registered:
		user_class = registered_users[str(message.chat.id)]
		user_schedules = schedules[user_class]
	else:
		return

	text_message = create_schedule(True, "воскресенье", user_schedules["6"])

	bot.send_message(message.chat.id, text_message)


@bot.message_handler(func=lambda message: message.text.lower() in ("/links", "links", "ссылки"))
def links(message):
	bot.send_message(message.chat.id, "Ссылки на школьные порталы")


@bot.message_handler(func=lambda message: message.text.lower() in (
		"/changeclass", "регистрация", "register", "изменение", "changeclass"))
def changeClass(message):
	bot.send_message(message.chat.id,
					 "Пожалуйста, зарегистрируйтесь заново, написав в чат номер и букву класса. \n\nНапример: 9Г, 11а, 8В.")


@bot.message_handler(commands=["save_data"])
def saveData(message):
	if message.chat.id not in ADMINS: return

	write_file_registered()
	bot.send_message(message.chat.id, "Данные сохранены!")


@bot.message_handler(commands=["massMailing"])
def massMailing_message(message):
	if message.chat.id not in ADMINS: return

	message = bot.send_message(message.chat.id,
							   "С помощью этой функции вы сможете устроить массовую рассылку. Напишите текст для неё в следующем сообщении.\n\n*К сообщению можно прикрепить файл, но только один, все остальные не покажутся в сообщении.*\n\n*Если вы не хотите писать сообщение, то выйти из режима можно, написав в следующем сообщении /exit*")

	bot.register_next_step_handler(message, massMailing)


@bot.message_handler(func=lambda message: True,
					 content_types=['audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact',
									'sticker'])
def default_command(message):
	bot.send_message(message.chat.id, "Чтобы ознакомится с функциями почитайте /help")



def updating_data():
	while True:
		sleep(3_600)
		write_file_registered()


threading.Thread(target=updating_data, daemon=True).start()


"Идея заключается в том, что в боте будет реализованна функция, которая позволяет скидывать контрольные выборочно, например, только 9г и 8в."
if __name__ == "__main__":
	bot.infinity_polling()
