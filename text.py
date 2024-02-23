start_text_message = "Приветствую вас! Пожалуйста, зарегистрируйтесь, указав номер и букву класса. \n\nНапример: 9Г, 11а, 8В."
help_text_message = """
*Бот находится в разработке.*
*Основные команды*
/help - помощь
/today - расписание на сегодня
/tomorrow - расписание на завтра

*Расписания*
/calls - рассписание звонков

Чтобы получить расписание на определенный день, напишите название этого дня (например, четверг, чт или thursday) бот поймёт, о каком дне идет речь.

*Информация*
/teachers - список всех учителей с указанием кабинета и предмета
/groups - список всех классов, их учителей и кабинета
/schedule - персональное расписание учителя или класса

*Разное*
/links - ссылки на школьные порталы
/register - изменение класса
/add - Добавление в общий чат школы
"""

calls_text_message = """
*🔔 Расписание звонков 🔔*

1 урок - 08:00-08:40
2 урок - 08:55-09:35
3 урок - 09:50-10:30
4 урок - 10:45-11:25
5 урок - 11:40-12:20
6 урок - 12:30-13:10
7 урок - 13:15-13:55
8 урок - 14:20-15:00

👇 Вы также можете посмотреть расписание уроков на сегодня
"""

teachers_text_message = """
*👩‍🏫 Список учителей 👨‍🏫*

*Русский язык, литература*
Леонтьева Анжелика Евгеньевна - 408

*Математика*
Марянова Анна Сергеевна - 306

*История, общество*
Кузнецова Елена Александровна - 40..

*Информатика*
Малеева Татьяна Петровна - 302

*Английский язык*
Муратова Анна Сергеевна - 40..

*Биология*
Платонова Ирина Николаевна - кабинет "Биологии"

*Химия*
Исаева Мария Александровна - кабинет "Химия"

*Физика*
Егорова Ольга Владимировна - 20..

*География*
Жданова Маргарита Александровна - 308

*ОБЖ*
Николенко Александр Сергеевич - 208

*Физкультура*
Ахмерова Ксения Алексеевна - спортзал

*Библиотека и музыка*
Петрова Наталья Павловна - библиотека
...

*Чувашский язык*
Грузин Владимир Владимирович - 111
"""
schedules = {
	"1а": (
		"1. Физическая культура\n2. Математика\n3. Динамическая пауза\n4. Литературное чтение\n5. Русский язык",
		"1. Литературное чтение\n2. Математика\n3. Динамическая пауза\n4. Русский язык\n5. Окружающий мир",
		"1. Литературное чтение\n2. Математика\n3. Динамическая пауза\n4. Музыка\n5. Русский язык",
		"1. Литературное чтение\n2. Математика\n3. Физическая культура\n4. Русский язык\n5. Технология",
		"1. Литературное чтение\n2. Русский язык\n3. Динамическая пауза\n4. Окружающий мир\n5. Изобразительное искусство",
		"Выходной", "Выходной"),
	"1б": (
		"1. Литературное чтение\n3. Математика\n3. Динамическая пауза\n4. Русский язык\n5. Технология",
		"1. Литературное чтение\n2. Математика\n3. Физическая культура\n4. Русский язык \n5. Изобразительное искусство",
		"1. Литературное чтение\n2. Математика\n3. Динамическая пауза\n4. Окружающий мир \n5. Русский язык",
		"1. Физическая культура\n2. Математика\n3. Динамическая пауза\n4. Литературное чтение\n5. Русский язык",
		"1. Литературное чтение\n2. Музыка\n3. Динамическая пауза\n4. Русский язык\n5. Окружающий мир",
		"Выходной", "Выходной"),
	"1в": (
		"1. Музыка\n2. Литературное чтение\n3. Динамическая пауза\n4. Русский язык\n5. Изобразительное искусство",
		"1. Литературное чтение\n2. Математика\n3. Динамическая пауза\n4. Русский язык\n5. Окружающий мир",
		"1. Физическая культура\n2. Математика\n3. Литературное чтение\n4. Русский язык\n5. Технология",
		"1. Литературное чтение\n2. Математика\n3. Динамическая пауза\n4. Русский язык\n5. Окружающий мир",
		"1. Русский язык\n2. Математика\n3. Динамическая пауза\n4. Физическая культура\n5. Литературное чтение",
		"Выходной", "Выходной"),

	"2а": (
		"1. Русский язык\n2. Математика\n3. Литературное чтение\n4. Физическая культура",
		"1. Русский язык\n2. Иностранный язык\n3. Математика\n4. Окружающий мир\n5. Литературное чтение",
		"1. Русский язык\n2. Физическая культура\n3. Математика\n4. Литературное чтение\n5. Изобразительное искусство",
		"1. Русский язык\n2. Математика\n3. Литературное чтение\n4. Музыка\n5. Окружающий мир",
		"1. Русский язык\n2. Иностранный язык\n3. Математика\n4. Технология",
		"Выходной", "Выходной"),
	"2б": (
		"1. Русский язык\n2. Окружающий мир\n3. Математика\n4. Изобразительное искусство",
		"1. Иностранный язык\n2. Физическая культура\n3. Математика\n4. Русский язык\n5. Литературное чтение",
		"1. Русский язык\n2. Математика\n3. Литературное чтение\n4. Окружающий мир\n5. Русский язык",
		"1. Иностранный язык\n2. Математика\n3. Русский язык\n4. Литературное чтение\n5. Технология",
		"1. Математика\n2. Физическая культура\n3. Русский язык\n4. Литературное чтение\n5. Музыка",
		"Выходной", "Выходной"),
	"2в": (
		"1. Русский язык\n2. Математика \n3. Физическая культура\n4. Окружающий мир",
		"1. Русский язык\n2. Музыка\n3. Иностранный язык\n4. Математика\n5. Литературное чтение",
		"1. Русский язык\n2. Математика\n3. Литературное чтение\n4. Окружающий мир\n5. ИЗО",
		"1. Русский язык\n2. Математика\n3. Иностранный язык\n4. Физкультура\n5. Литературное чтение",
		"1. Русский язык\n2. Математика\n3. Литературное чтение\n4. Технология",
		"Выходной", "Выходной"),
	"2г": (
		"1. Русский язык\n2. Математика\n3. Литературное чтение\n4. Физическая культура",
		"1. Русский язык\n2. Математика\n3. Литературное чтение\n4. Иностранный язык",
		"1. Русский язык\n2. Математика\n3. Литературное чтение\n4. Окружающий мир\n5. Технология",
		"1. Русский язык \n2. Иностранный язык\n3. Математика\n4. ИЗО\n5. Музыка",
		"1. Русский язык\n2. Литературное чтение\n3. Математика\n4. Физическая культура\n5. Окружающий мир",
		"Выходной", "Выходной"), 

	"3а": (
		"1. Физкультура\n2. Математика\n3. Русский язык\n4. Окружающий мир",
		"1. Литературное чтение\n2. Русский язык\n3. Математика\n4. ИЗО\n5. Иностранный язык",
		"1. Литературное чтение\n2. Русский язык\n3. Математика\n4. Физическая культура\n5. Технология",
		"1. Русский язык\n2. Литературное чтение\n3. Музыка\n4. Окружающий мир\n5. Родной язык",
		"1. Русский язык\n2. Математика\n3. Иностранный язык\n4. Литературное чтение",
		"Выходной", "Выходной"), 
	"3б": (
		"1. Иностранный язык\n2. Математика\n3. Музыка\n4. Русский язык",
		"1. Физическая культура\n2. Математика\n3. Русский язык\n4. Литературное чтение\n5. Окружающий мир",
		"1. Русский язык\n2. Математика\n3. Физическая культура\n4. Иностранный язык\n5. Литературное чтение",
		"1. Русский язык\n2. Литературное чтение\n3. Окружающий мир\n4. ИЗО\n5. Родной язык",
		"1. Русский язык\n2. Математика\n3. Литературное чтение\n4. Технология",
		"Выходной", "Выходной"), 
	"3в": (
		"1. Русский язык\n2. Математика\n3. Иностранный язык\n4. Музыка",
		"1. Русский язык\n2. Математика\n3. Окружающий мир\n4. Физическая культура\n5. Физическая культура",
		"1. Русский язык\n2. Литературное чтение\n3. Математика\n4. Технология\n5. Иностранный язык",
		"1. Русский язык\n2. Физическая культура\n3. Окружающий мир\n4. Литературное чтение\n5. Родной язык",
		"1. Русский язык\n2. Литературное чтение\n3. Математика\n4. Изобразительное искусство",
		"Выходной", "Выходной"), 
	
	"4а": (
		"1. Русский язык\n2. Иностранный язык\n3. Литературное чтение\n4. Физическая культура",
		"1. Музыка\n2. Математика\n3. Литературное чтение на родном языке\n4. Русский язык\n5. Окружающий мир",
		"1. Иностранный язык\n2. Русский язык\n3. Математика\n4. Литературное чтение\n5. ИЗО",
		"1. Литературное чтение\n2. Русский язык\n3. Математика\n4. ОРКСЭ\n5. Технология",
		"1. Литературное чтение\n2. Русский язык\n3. Математика\n4. ОРКСЭ",
		"Выходной", "Выходной"),
	"4б": (
		"1. Окружающий мир\n2. Математика\n3. Русский язык\n4.Литературное чтение \n5. Физическая культура",
		"1. Технология\n2. Русский язык\n3. Литературное чтение\n4. Литературное чтение на родном языке\n5. ОРКСЭ",
		"1. Русский язык\n2. Иностранный язык\n3. Математика\n4. ИЗО",
		"1. Окружающий мир\n2. Русский язык\n3. Математика\n4. Физическая культура\n5. Литературное чтение",
		"1. Математика\n2. Русский язык\n3. Музыка\n4. Иностранный язык",
		"Выходной", "Выходной"), 
	"4в": (
		"1. Русский язык\n2. Физическая культура\n3. Математика\n4. Литературное чтение",
		"1. Русский язык\n2. ИЗО\n3. Литературное чтение на родном языке\n4. Окружающий мир\n5. ОРКСЭ",
		"1. Русский язык\n2. Математика\n3. Иностранный язык\n4. Литературное чтение\n5. Технология",
		"1. Русский язык\n2. Математика\n3. Физическая культура\n4. Окружающий мир\n5. Литературное чтение",
		"1. Иностранный язык\n2. Математика\n3. Русский язык\n4. Музыка",
		"Выходной", "Выходной"), 
	
	"5а": (
		"1. Математика\n2. История\n3. Русский язык\n4. Иностранный язык\n5. Литература\n6. ОБЖ", 
		"1. Русский язык\n2. Русский язык\n3. Математика\n4. География\n5. Музыка", 
		"1. Русский язык\n2. Физкультура\n3. История\n4. Математика\n5. Литература\n6. Иностранный язык", 
		"1. Технология\n2. Технология\n3. Русский язык\n4. Математика\n5. Иностранный язык\n6. Литература", 
		"1. Физкультура\n2. Математика\n3. Русский язык\n4. ОДНК\n5. ИЗО\n6. Биология", 
		"Выходной", "Выходной"), 
	"5б": (
		"1. Русский язык\n2. Математика\n3. История\n4. Иностранный язык\n5. Литература\n6. ОДНК", 
		"1. Математика\n2. Русский язык\n3. Русский язык\n4. ОБЖ\n5. География\n6. Музыка", 
		"1. Русский язык\n2. ИЗО\n3. Математика\n4. Физкультура\n5. Литература\n6. ", 
		"1. Математика\n2. Русский язык\n3. Технология\n4. Технология\n5. Иностранный язык", 
		"1. Русский язык\n2. Физкультура\n3. Математика\n4. Биология\n5. История\n6. Литература", 
		"Выходной", "Выходной"),
	"5в": (
		"1. История\n2. Русский язык\n3. Математика\n4. Литература\n5. ОБЖ", 
		"1. География\n2. Математика\n3. ИЗО\n4. Русский язык\n5. Русский язык\n6. Иностранный язык", 
		"1. История\n2. Математика\n3. Физкультура\n4. Русский язык\n5. Музыка\n6. Литература", 
		"1. Русский язык\n2. Биология\n3. Математика\n4. Иностранный язык\n5. Технология\n6. Технология", 
		"1. Математика\n2. Русский язык\n3. Физкультура\n4. Литература\n5. Иностранный язык\n6. ОДНК", 
		"Выходной", "Выходной"), 
	
	"6а": (
		"1. История\n2. Русский язык\n3. Математика\n4. Технология\n5. Технология\n6. Литература", 
		"1. Русский язык\n2. Русский язык\n3. Обществознание\n4. Математика\n5. Физкультура\n6. Иностранный язык", 
		"1. Математика\n2. ИЗО\n3. Русский язык\n4. Биология\n5. Литература\n6. ОБЖ", 
		"1. Русский язык\n2. География\n3. Математика\n4. Иностранный язык\n5. История\n6. Музыка", 
		"1. Математика\n2. Русский язык\n3. ОМРК\n4. Литература\n5. Иностранный язык\n6. Физкультура", 
		"Выходной", "Выходной"), 
	"6б": (
		"1. Математика\n2. Русский язык\n3. История\n4. Литература\n5. Биология\n6. ИЗО", 
		"1. Русский язык\n2. Математика\n3. Технология\n4. Технология\n5. Обществознание\n6. Иностранный язык", 
		"1. Русский язык\n2. ОМРК\n3. Математика\n4. ОБЖ\n5. Литература\n6. Физкультура", 
		"1. История\n2. Математика\n3. Русский язык\n4. Иностранный язык\n5. География\n6. Физкультура", 
		"1. Русский язык\n2. Музыка\n3. Русский язык\n4. Математика\n5. Иностранный язык\n6. Литература", 
		"Выходной", "Выходной"), 
	"6в": (
		"1. Русский язык\n2. Биология\n3. Русский язык\n4. Иностранный язык\n5. Литература\n6. Математика", 
		"1. Технология\n2. Технология\n3. Русский язык\n4. Иностранный язык\n5. Математика\n6. История", 
		"1. ИЗО\n2. Русский язык\n3. Физкультура\n4. Литература\n5. Математика\n6. Музыка", 
		"1. ОБЖ\n2. Математика\n3. Русский язык\n4. Обществознание\n5. Иностранный язык\n6. География", 
		"1. Физкультура\n2. История\n3. ОМРК\n4. Математика\n5. Русский язык\n6. Литература", 
		"Выходной", "Выходной"), 
	"6г": (
		"1. Русский язык\n2. Технология\n3. Технология\n4. Математика\n5. Литература\n6. Физкультура", 
		"1. Иностранный язык\n2. Русский язык\n3. История\n4. Математика\n5. Литература\n6. Физкультура", 
		"1. Математика\n2. Биология\n3. Русский язык\n4. ИЗО\n5. ОБЖ\n6. Литература", 
		"1. Музыка\n2. Русский язык\n3. Обществознание\n4. Русский язык\n5. Математика\n6. Иностранный язык", 
		"1. История\n2. Русский язык\n3. География\n4. ОМРК\n5. Математика\n6. Иностранный язык", 
		"Выходной", "Выходной"),
	
	"7а": (
		"1. География\n2. История\n3. Алгебра\n4. Обществознание\n5. Физика\n6. Иностранный язык", 
		"1. Русский язык\n2. Физкультура\n3. Геометрия\n4. Биология\n5. Информатика\n6. Литература\n7. Родной язык", 
		"1. Алгебра\n2. Иностранный язык\n3. Русский язык\n4. Алгебра\n5. История\n6. Физика", 
		"1. Физкультура\n2. Музыка\n3. Геометрия\n4. Русский язык\n5. ОБЖ\n6. Литература\n7. Иностранный язык", 
		"1. Технология\n2. Технология\n3. Русский язык\n4. ИЗО\n5. Алгебра\n6. География", 
		"Выходной", "Выходной"), 
	"7б": (
		"1. Русский язык\n2. География\n3. Алгебра\n4. Литература\n5. История\n6. Иностранный язык", 
		"1. Биология\n2. Геометрия\n3. Физкультура\n4. Физика\n5. Русский язык\n6. Родной язык", 
		"1. Физика\n2. Иностранный язык\n3. История\n4. Алгебра\n5. Алгебра\n6. Обществознание\n7. ОБЖ", 
		"1. География\n2. Русский язык\n3. Геометрия\n4. Литература\n5. ИЗО\n6. Информатика\n7. Иностранный язык", 
		"1. Алгебра\n2. Русский язык\n3. Технология\n4. Технология\n5. Физкультура\n6. Музыка", 
		"Выходной", "Выходной"), 
	"7в": (
		"1. Алгебра\n2. ОБЖ\n3. Русский язык\n4. Физика\n5. История\n6. Литература", 
		"1. Иностранный язык\n2. Геометрия\n3. География\n4. Физкультура\n5. Технология\n6. Технология\n7. Обществознание", 
		"1. ИЗО\n2. Русский язык\n3. Алгебра\n4. Музыка\n5. Алгебра\n6. История", 
		"1. Геометрия\n2. Физкультура\n3. Русский язык\n4. Информатика\n5. Литература\n6. Иностранный язык\n7. Родной язык", 
		"1. Биология\n2. Иностранный язык\n3. Алгебра\n4. География\n5. Русский язык\n6. Физика", 
		"Выходной", "Выходной"), 
	"7г": (
		"1. Физика\n2. Алгебра\n3. Русский язык\n4. История\n5. Иностранный язык\n6. Алгебра", 
		"1. Геометрия\n2. География\n3. Музыка\n4. Русский язык\n5. Физкультура\n6. Родной язык", 
		"1. ОБЖ\n2. Алгебра\n3. Обществознание\n4. Иностранный язык\n5. Физика\n6. Технология\n7. Технология", 
		"1. Русский язык\n2. ИЗО\n3. Физкультура\n4. География\n5. Литература\n6. Геометрия", 
		"1. Алгебра\n2. Иностранный язык\n3. Биология\n4. Русский язык\n5. Литература\n6. Информатика\n7. История", 
		"Выходной", "Выходной"),
	
	"8а": (
		"1. Иностранный язык\n2. Музыка\n3. Физкультура\n4. Алгебра\n5. Алгебра\n6. История", 
		"1. Геометрия\n2. Химия\n3. Русский язык\n4. Биология\n5. Иностранный язык\n6. Физика", 
		"1. Алгебра\n2. Русский язык\n3. Физика\n4. Обществознание\n5. География\n6. Литература\n7. Родной язык", 
		"1. Геометрия\n2. Химия\n3. Французский язык\n4. ОБЖ\n5. Биология\n6. История\n7. Физкультура", 
		"1. Информатика\n2. Алгебра\n3. Иностранный язык\n4. Русский язык\n5. Литература\n6. Технология\n7. География", 
		"Выходной", "Выходной"), 
	"8б": (
		"1. Иностранный язык\n2. Физика\n3. Французский язык\n4. Физкультура\n5. Алгебра\n6. Родной язык", 
		"1. Геометрия\n2. Биология\n3. Химия\n4. Музыка\n5. Иностранный язык\n6. География\n7. Физика", 
		"1. Физкультура\n2. Технология\n3. Русский язык\n4. Литература\n5. История\n6. Алгебра", 
		"1. Русский язык\n2. Геометрия\n3. Химия\n4. История\n5. Информатика\n6. ОБЖ\n7. Обществознание", 
		"1. Русский язык\n2. География\n3. Иностранный язык\n4. Алгебра\n5. Алгебра\n6. Литература\n7. Биология", 
		"Выходной", "Выходной"), 
	"8в": (
		"1. Русский язык\n2. Алгебра\n3. Иностранный язык\n4. Литература\n5. Физкультура\n6. Родной язык", 
		"1. Физика\n2. Французский язык\n3. ОБЖ\n4. Иностранный язык\n5. Химия\n6. Геометрия\n7. Биология", 
		"1. Технология\n2. Русский язык\n3. Иностранный язык\n4. Алгебра\n5. Алгебра\n6. Литература\n7. География", 
		"1. Информатика\n2. История\n3. Геометрия\n4. Русский язык\n5. Физкультура\n6. Химия\n7. Биология", 
		"1. Музыка\n2. История\n3. Алгебра\n4. Физика\n5. География\n6. Обществознание", 
		"Выходной", "Выходной"), 
	"8г": (
		"1. Алгебра\n2. История\n3. Иностранный язык\n4. ОБЖ\n5. Русский язык\n6. Физика", 
		"1. Химия\n2. Геометрия\n3. Физика\n4. Иностранный язык\n5. Русский язык\n6. Физкультура\n7. География", 
		"1. Алгебра\n2. Алгебра\n3. Иностранный язык\n4. Информатика\n5. Литература\n6. География\n7. Родной язык", 
		"1. Химия\n2. Русский язык\n3. Обществознание\n4. Физкультура\n5. Биология\n6. Геометрия", 
		"1. История\n2. Биология\n3. Музыка\n4. Литература\n5. Технология\n6. Алгебра\n7. Французский язык", 
		"Выходной", "Выходной"),
	
	"9а": (
		"1. Русский язык\n2. Информатика\n3. Алгебра\n4. Алгебра\n5. Химия\n6. Иностранный язык", 
		"1. Физкультура\n2. История\n3. Биология\n4. Геометрия\n5. Обществознание\n6. Русский язык\n7. Литература", 
		"1. География\n2. Русский язык\n3. Алгебра\n4. Литература\n5. Физкультура\n6. Физика", 
		"1. Геометрия\n2. ОБЖ\n3. География\n4. Физика\n5. История\n6. Биология\n7. Иностранный язык", 
		"1. Литература\n2. Химия\n3. Обществознание\n4. Физика\n5. Родной язык\n6. Иностранный язык\n7. Алгебра", 
		"Выходной", "Выходной"), 
	"9б": (
		"1. Химия\n2. Алгебра\n3. Литература\n4. Информатика\n5. Иностранный язык\n6. География", 
		"1. История\n2. Русский язык\n3. Иностранный язык\n4. Геометрия\n5. Физика\n6. ОБЖ\n7. Физкультура", 
		"1. Биология\n2. Обществознание\n3. Русский язык\n4. География\n5. Иностранный язык\n6. Алгебра\n7. Алгебра", 
		"1. Биология\n2. История\n3. Русский язык\n4. Геометрия\n5. Физика\n6. Литература", 
		"1. Обществознание\n2. Литература\n3. Химия\n4. Алгебра\n5. Родной язык\n6. Физика\n7. Физкультура", 
		"Выходной", "Выходной"), 
	"9в": (
		"1. Алгебра\n2. Химия\n3. ОБЖ\n4. География\n5. Физика\n6. Физкультура", 
		"1. Русский язык\n2. Иностранный язык\n3. Геометрия\n4. Литература\n5. Биология\n6. История\n7. Обществознание", 
		"1. Иностранный язык\n2. География\n3. Алгебра\n4. Русский язык\n5. Биология\n6. Информатика\n7. Обществознание", 
		"1. Русский язык\n2. Геометрия\n3. Иностранный язык\n4. История\n5. Литература\n6. Физкультура\n7. Физика", 
		"1. Литература\n2. Физика\n3. Родной язык\n4. Химия\n5. Алгебра\n6. Алгебра", 
		"Выходной", "Выходной"), 
	"9г": (
		"1. Биология\n2. Русский язык\n3. Химия\n4. Физика\n5. География\n6. Алгебра",
		"1. Русский язык\n2. Иностранный язык\n3. История\n4. Физика\n5. Геометрия\n6. Биология\n\n*Внеурочки*\n7. Информатика\n8. Общество", 
		"1. Иностранный язык\n2. Информатика\n3. ОБЖ\n4. Физ-ра\n5. Литература\n6. Общество\n7. Алгебра\n\n*Внеурочки*\n8. Семьеведение", 
		"1. Русский язык\n2. Физика\n3. Иностранный язык\n4. Литература\n5. Геометрия\n6. История\n7. География\n\n*Внеурочки*\n8. Россия - мои горизонты\n9. Математика", 
		"1. Алгебра\n2. Алгебра\n3. Родной язык\n4. Литература\n5. Физ-ра\n6. Химия\n7. Общество\n\n*Внеурочки*\n8. Русский язык", 
		"*Внеурочки*\n1. Математика\n2. Русский язык", 
		"Выходной"),

	"10а": (
		"Админ не знает какие тут уроки( \nСкинте ему, пожалуйста, /admin", 
		"Админ не знает какие тут уроки( \nСкинте ему, пожалуйста, /admin", 
		"Админ не знает какие тут уроки( \nСкинте ему, пожалуйста, /admin", 
		"Админ не знает какие тут уроки( \nСкинте ему, пожалуйста, /admin", 
		"Админ не знает какие тут уроки( \nСкинте ему, пожалуйста, /admin", 
		"Админ не знает какие тут уроки( \nСкинте ему, пожалуйста, /admin", 
		"Админ не знает какие тут уроки( \nСкинте ему, пожалуйста, /admin"), 
	"10б": (
		"1. Физкультура\n2. Иностранный язык\n3. Биология\n4. История\n5. Обществознание\n6. Индивидуальный проект", 
		"1. Геометрия\n2. ОБЖ\n3. Информатика\n4. Обществознание\n5. Русский язык\n6. Литература\n7. Иностранный язык", 
		"1. Русский язык\n2. Физика\n3. География\n4. История\n5. Обществознание\n6. Физкультура\n7. Алгебра", 
		"1. История\n2. Иностранный язык\n3. Обществознание\n4. Химия\n5. Литература\n6. Геометрия\n7. Обществознание", 
		"1. Физика\n2. История\n3. Русский язык\n4. Иностранный язык\n5. Админ не знает какой тут урок ( Напишите ему /admin\n6. Алгебра\n7. Литература", 
		"Выходной", "Выходной"), 

	"11а": (
		"1. ОБЖ\n2. Физкультура\n3. Физика\n4. Химия\n5. Литература\n6. Математика\n7. Астрономия", 
		"1. Информатика\n2. Физика\n3. Иностранный язык\n4. Обществознание\n5. Математика\n6. Математика", 
		"1. Россия в мире\n2. Математика\n3. Информатика\n4. Физика\n5. Физкультура\n6. Литература\n7. Русский язык", 
		"1. Иностранный язык\n2. Информатика\n3. Информатика\n4. Биология\n5. Математика\n6. Литература\n7. Индивидуальный проект", 
		"1. Иностранный язык\n2. Физика\n3. Физика\n4. Физкультура\n5. Россия в мире\n6. Родной язык\n7. Математика", 
		"Выходной", "Выходной"), 
	"11б": (
		"1. ОБЖ\n2. Физкультура\n3. История\n4. Химия\n5. Литература\n6. Математика\n7. Астрономия", 
		"1. История\n2. История\n3. Иностранный язык\n4. Право\n5. Русский язык\n6. Математика", 
		"1. История\n2. Математика\n3. Русский язык\n4. Обществознание\n5. Физкультура\n6. Литература\n7. Обществознание", 
		"1. Иностранный язык\n2. Право\n3. Русский язык\n4. Биология\n5. Математика\n6. Литература\n7. Индивидуальный проект", 
		"1. Иностранный язык\n2. Математика\n3. Информатика\n4. Физкультура\n5. История\n6. Родной язык\n7. Физика", 
		"Выходной", "Выходной")
}