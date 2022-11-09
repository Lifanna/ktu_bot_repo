from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# BTN_INCOME = InlineKeyboardButton('Внести доходы', callback_data='income')
# BTN_EXPEND = InlineKeyboardButton('Внести расходы', callback_data='expend')
# BTN_SHOW = InlineKeyboardButton('Показать статистику', callback_data='stat')

# BTN_SALARY = InlineKeyboardButton('Зарплата', callback_data='income_salary')
# BTN_GIFT = InlineKeyboardButton('Подарки', callback_data='income_gift')
# BTN_OTHER = InlineKeyboardButton('Другие', callback_data='income_other')

# BTN_ODEZHDA = InlineKeyboardButton('Одежда', callback_data='expend_odezhda')
# BTN_DOM = InlineKeyboardButton('Дом', callback_data='expend_dom')
# BTN_ZDOROVIE = InlineKeyboardButton('Здоровье', callback_data='expend_zdorovie')
# BTN_AVTOMOBIL = InlineKeyboardButton('Автомобиль', callback_data='expend_avtomobil')
BTN_MENU = InlineKeyboardButton('Главное меню', callback_data='main_menu')

MAIN_MENU = InlineKeyboardMarkup().add(BTN_MENU)
# INCOMES = InlineKeyboardMarkup().add(BTN_SALARY, BTN_GIFT, BTN_OTHER)

# EXPENDS = InlineKeyboardMarkup().add(BTN_ODEZHDA, BTN_DOM, BTN_ZDOROVIE, BTN_AVTOMOBIL, BTN_DOM_ZHIV)

# BTN_MONTH = InlineKeyboardButton('ЗА МЕСЯЦ', callback_data='stat_month')
# BTN_HALF_YEAR = InlineKeyboardButton('ЗА ПОЛУГОДИЕ', callback_data='stat_half_year')
# BTN_YEAR = InlineKeyboardButton('ЗА ГОД', callback_data='stat_year')
# PERIODS = InlineKeyboardMarkup().add(BTN_MONTH, BTN_HALF_YEAR, BTN_YEAR)
