from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# Направления  ИРЭФ-ЦТ 234
menu_iktfiz_dis_button_234 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Информационные сети, мобильныя и оптическая связь, квантовые коммуникации",
                             callback_data="Quantum_communications_dis_8")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_234_dis_8")
    ]
])

# Направления ИАНТЭ 234
menu_iktfiz_dis_button_234_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Современные сварочные материалы, технологии, оборудование и диагностика",
                             callback_data="Modern_ welding_materials_dis_8")
    ],
    [
        InlineKeyboardButton(text="Технология машиностроения", callback_data="Mechanical_engineering_technology_dis_8")
    ],
    [
        InlineKeyboardButton(text="Автомобильный транспорт. Сервис и эксплуатация",
                             callback_data="Road_transport_dis_8")
    ],
    [
        InlineKeyboardButton(text="Обслуживание судов и двигателей, обеспечение безопасности полетов",
                             callback_data="Ship_and_engine_maintenance_dis_8")
    ],
    [
        InlineKeyboardButton(text="Паро - и газотурбинные установки. Автомобильные двигатели",
                             callback_data="Gas_turbine_installations_dis_8")
    ],
    [
        InlineKeyboardButton(text="Технология машиностроения",
                             callback_data="Mechanical_engineering_technology_disk_8")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_234_dis_8")
    ]
])

# Направления ИКТЗИ 234
menu_iktfiz_dis_button_234_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Программная инженерия", callback_data="Software_engineering_dis_8")
    ],
    [
        InlineKeyboardButton(text="Интеллектуальные информационные системы",
                             callback_data="Intelligent_information_systems_dis_8")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_234_dis_8")
    ]
])

# Направления ИАЭП 234
menu_iktfiz_dis_button_234_3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Стандартизация, сертификация и метрология", callback_data="Standardization_dis_8")
    ],
    [
        InlineKeyboardButton(text="Управление качеством", callback_data="Quality_management_dis_8")
    ],
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_234_dis_8")
    ]
])

# назад к факультетам
back_dis_234_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Назад⬅️", callback_data="back_dic_234_8")
    ]
])
