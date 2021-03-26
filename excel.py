import openpyxl 
import datetime

#--Открытие excel
wb = openpyxl.load_workbook('Таблица.xlsx')
sheet = wb.active
#--Открытие excel

#--Функция записи строк
def insert_excel(fn, сlass_nuvbmer, answer, v_answer, points, olimpiada):
    try:
        #--Подготовка 
        fn_Y = []
        answer_Y = []
        v_answer_Y = []
        points_Y = []
        olimpiada_Y = []

        for i in fn:
            if i != " " and i != "\n" and i != "\x0c":
                 fn_Y.append(i)

        for i in answer:
            if i != " " and i != "\n" and i != "\x0c":
                 answer_Y.append(i)

        for i in v_answer:
            if i != " " and i != "\n" and i != "\x0c":
                 v_answer_Y.append(i)

        for i in str(points):
            if i != " " and i != "\n" and i != "\x0c":
                 points_Y.append(i)

        for i in olimpiada:
            if i != " " and i != "\n" and i != "\x0c" and i != "‚" and i != "." and i != ":" and i != "/":
                 print(i)
                 olimpiada_Y.append(i)

        fio = str(''.join(fn_Y))
        otvet = str(''.join(answer_Y))   
        prav_otver = str(''.join(v_answer_Y))
        balls = str(''.join(points_Y))
        o = str(''.join(olimpiada_Y))
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
        G = f"G{cikl}"
		#--Обозначение переменных

		#--Вписывание данных в таблицу
        c1 = sheet["A1"]
        c1.value = cikl

        c2 = sheet[B]
        c2.value = fio

        c3 = sheet[C]
        c3.value = сlass_nuvbmer

        c4 = sheet[D]
        c4.value = otvet

        c5 = sheet[E]
        c5.value = prav_otver

        c6 = sheet[F]
        c6.value = balls

        c7 = sheet[G]
        c7.value = o
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
            f.write(f"Имя и Фамилия: {fn} \n")
            f.write(f"Класс: {сlass_nuvbmer} \n")
            f.write(f"Ответ ученика: {answer} \n")
            f.write(f"Правильный ответ: {v_answer} \n")
            f.write(f"Баллы набранные учеником: {points} \n")
            f.write(f"Олимпиада: {olimpiada} \n")
            f.write("----------------------- \n")
            f.close()        
        #==Логирование 

        return "Благодарю, данные были внесены" #->ОТПРАВКА ОТВЕТА

#--Функция записи строк	