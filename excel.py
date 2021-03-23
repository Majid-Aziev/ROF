import openpyxl 
import datetime

#--Открытие excel
wb = openpyxl.load_workbook('Таблица.xlsx')
sheet = wb.active
#--Открытие excel

#--Функция записи строк
def insert_excel(fio, klass_nuvbmer, otvet, prav_otver, balls):
    try:
        #--Подготовка 
        fio_Y = []
        otvet_Y = []
        prav_otver_Y = []
        balls_Y = []
        
        for i in fio:
            if i != " " and i != "\n" and i != "\x0c":
                 fio_Y.append(i)

        for i in otvet:
            if i != " " and i != "\n" and i != "\x0c":
                 otvet_Y.append(i)

        for i in prav_otver:
            if i != " " and i != "\n" and i != "\x0c":
                 prav_otver_Y.append(i)

        for i in str(balls):
            if i != " " and i != "\n" and i != "\x0c":
                 balls_Y.append(i)
        
        fio = str(''.join(fio_Y))
        otvet = str(''.join(otvet_Y))   
        prav_otver = str(''.join(prav_otver_Y))
        balls = str(''.join(balls_Y))
        #--Подготовка 

        #--Запись данных
		#--Получение сколько строк в таблице
        cikl = int(sheet['A1'].value)
		#--Получение сколько строк в таблице

        cikl = cikl + 1 #На какой номер строки будем кидать данные

		#--Обозначение переменных
        B = f"B{cikl}" 
        C = f"C{cikl}"
        D = f"D{cikl}"
        E = f"E{cikl}"
        F = f"F{cikl}"
		#--Обозначение переменных

		#--Вписывание данных в таблицу
        c1 = sheet["A1"]
        c1.value = cikl

        c2 = sheet[B]
        c2.value = fio

        c3 = sheet[C]
        c3.value = klass_nuvbmer

        c4 = sheet[D]
        c4.value = otvet

        c5 = sheet[E]
        c5.value = prav_otver

        c6 = sheet[F]
        c6.value = balls

		#--Вписывание данных в таблицу

        wb.save("Таблица.xlsx")# Сохранение таблицы
        #--Запись данных

	#Если возникла ошибка	
    except:
        #==Логирование
        with open('log/log.txt', 'a') as f:
            f.write(f"{datetime.date.today()}, НА СЕРВЕРЕ ОШИБКА, ВНИМАНИЕ, НА СЕРВЕРЕ ОШИБКА!!!: \n")
            f.write("----------------------- \n")
            f.close()
        #==Логирование
        
        return "Упс, на сервере ошибка. Скоро исправим" #->ОТПРАВКА ОТВЕТА

	#Если всё хорошо
    else:
        #==Логирование
        with open('log/log.txt', 'a') as f:
            f.write(f"{datetime.date.today()}, Пользователь занесён в таблицу, его данные: \n")
            f.write(f"Имя и Фамилия: {fio} \n")
            f.write(f"Класс: {klass_nuvbmer} \n")            
            f.write(f"Ответ ученика: {otvet} \n")
            f.write(f"Правильный ответ: {prav_otver} \n")
            f.write(f"Баллы набранные учеником: {balls} \n")
            f.write("----------------------- \n")
            f.close()
        #==Логирование 

        return "Благодарю, данные были внесены" #->ОТПРАВКА ОТВЕТА

#--Функция записи строк		