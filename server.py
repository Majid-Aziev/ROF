import telebot
from telebot import types
from brain import processing

# Config
bot = telebot.TeleBot("1627673724:AAFyzRxRZ2dzooNd1BVO1-9qOJwEMcPcaLc") 

#--Телеграм кнопки быстрого доступа
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('/new_blank', '/download_blank', '/help')

keyboard2 = telebot.types.ReplyKeyboardMarkup()
keyboard2.row('Да', 'Нет')
#--Телеграм кнопки быстрого доступа

#--Обозначение переменных
src = 0 #Ссылка на файл
v_answer = 0 #Правильный ответ
#--Обозначение переменных


#--Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "*Привет!* \n Я бот созданный для распознания бланков. \n *Я вижу ты тут новенький, нажми /help для подсказки*", parse_mode='Markdown', reply_markup=keyboard1)
#--Команда /start


#--Команда /new_blank
@bot.message_handler(commands=['new_blank'])
def newBlank(message):
    bot.send_message(message.chat.id, "*Пришли фото бланка пожалуйста*", parse_mode='Markdown')
#--Команда /new_blank 


#--Команда /download_blank
@bot.message_handler(commands=['download_blank'])
def downloadBlank(message):
    bot.send_document(message.chat.id, open('Таблица.xlsx', 'rb'))
#--Команда /download_blank 


#--Команда /help
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Все доступные команды: \n/new_blank - Распознание нового бланка \n/download_blank - Скачивание excel таблицы с данными \n/help - Вызова меню помощи")
#--Команда /help


#--Команда при получение фото
@bot.message_handler(content_types=["photo"])
def photo(message):
    
    #--Загрузка файла
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    global src
    src = 'files/' + file_info.file_path # Определение переменной src
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    #--Загрузка файла

    bot.send_message(message.chat.id, "Спасибо! Добавишь правильные ответы? Напиши *Да* или *Нет*", parse_mode='Markdown', reply_markup=keyboard2)
#--Команда при получение фото 


#--Команда при написание "Да" или "Нет" или "_"
@bot.message_handler(content_types=['text'])
def lalala(message):

    #--Если пользователь ответил Да
    if message.text.lower() == "да":
            bot.send_message(message.chat.id, "Понял, пришли мне правильные ответы и в начале поставь *#*. \n Пример: *ABCBA* => *#ABCBA*", parse_mode='Markdown')
    #--Если пользователь ответил Да


    #--Если пользователь ответил Нет
    elif message.text.lower() == "нет":

            try: #--Если фото бланка есть
                textWWW = processing(src) #Отправка фото и получение ответа от функций
                bot.send_message(message.chat.id, textWWW, reply_markup=keyboard1)
            except: #--Если фото бланка нету
                bot.send_message(message.chat.id, "Ой, возникла ошибка. \nОтправьте фото бланка ещё раз пожалуйста", reply_markup=keyboard1)

    #--Если пользователь ответил Нет


    #--Если пользователь отправил данные по правильным ответам
    elif message.text[0] == "#":
        try:
            v_answer = message.text # Определение переменной v_answer
            textWWW = processing(src, v_answer) # Отправка фото, правильных ответов и получение ответа от функций
            bot.send_message(message.chat.id, textWWW, reply_markup=keyboard1)
        except:
            bot.send_message(message.chat.id, "Ой, возникла ошибка. \nОтправьте фото бланка ещё раз пожалуйста", reply_markup=keyboard1)
    #--Если пользователь отправил данные по правильным ответам
   
    #--Если другая непонятная команда
    else:
        bot.send_message(message.chat.id, "Простите, я не понял вашей команды. \n Напишите /help для вызова меню помощи", reply_markup=keyboard1)    
    #--Если другая непонятная команда

#--Команда при написание "Да" или "Нет" или "_"

# RUN
bot.polling(none_stop=True)