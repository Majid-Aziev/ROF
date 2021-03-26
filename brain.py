import cv2
import numpy as np
from PIL import Image
import pytesseract 
from excel import insert_excel
import os
import datetime

#Подготовка
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#--Функция обработки
def processing(photo, v_answer = "??????"):
    
    #--Подготовительный процес
    v_answer = v_answer[1:]
    image = Image.open(photo)
    resized_image = image.resize((489, 700))
    resized_image.save(photo)
    #--Подготовительный процес

    #--Отправка по функциям
    first_name, last_name = fn_recognition(photo)

    answer = blank_recognition(photo)
    
    class_nuvbmer = class_recognition(photo)

    points = measuring_points(answer, v_answer)

    olimpiada = olimpiada_recognition(photo)
    #--Отправка по функциям
   
    #--Проверка
    if first_name == "" or last_name == "":

        with open('log/log.txt', 'a') as f:
            f.write(f"{datetime.date.today()}, В бланке есть ошибки \n")
            f.write("----------------------- \n")      
            f.close()

        return "В бланке есть ошибки, перепроверьте бланк" #->ОТПРАВКА ОТВЕТА
    #--Проверка

    #--Подготовительный процес
    fn = f"{first_name}-{last_name}"
    #--Подготовительный процес


    #==Логирование
    with open('log/log.txt', 'a') as f:
        f.write(f"{datetime.date.today()}, Пытаюсь занести пользователя с данными: \n")
        f.write(f"Имя и Фамилия: {fn} \n")
        f.write(f"Класс: {class_nuvbmer} \n")
        f.write(f"Ответ ученика: {answer} \n")
        f.write(f"Правильный ответ: {v_answer} \n")
        f.write(f"Баллы набранные учеником: {points} \n")
        f.write(f"Олимпиада: {olimpiada} \n")
        f.write("----------------------- \n")
        f.close()
    #==Логирование


    #--Отправка на вставку в excel
    textWWW = insert_excel(fn, class_nuvbmer, answer, v_answer, points, olimpiada)
    #--Отправка на вставку в excel

    #--Удаление файла
    if os.path.isfile(photo): 
        os.remove(photo) 
    else: 
        print("File doesn't exists!")
    #--Удаление файла

    return textWWW #->ОТПРАВКА ОТВЕТА
#--Приёмная функция

#--Подсчёт баллов
def measuring_points(answer, v_answer):
    balls = 0

    if v_answer == "?????":
        balls = "?????"
        return "?????"

    v_answer = list(v_answer)
    answer = list(answer)
    i = 0

    try:
        m_balls = len(v_answer)
        
        for k in range(len(v_answer)):
            if str(v_answer[i]).lower() == str(answer[i]).lower():
                balls = balls + 1
            i += 1          
    except IndexError:
        balls = str(balls)
    
    balls = f"{balls * 100 // m_balls}%"

    return balls #->ОТПРАВКА ОТВЕТА
#--Подсчёт баллов


def olimpiada_recognition(photo):

    img = cv2.imread(photo)

    olimpiada = img[13:29, 180:458]
      
    gray_olimpiada = cv2.cvtColor(olimpiada, cv2.COLOR_BGR2GRAY)

    text_olimpiada = pytesseract.image_to_string(olimpiada, lang="rus")

    o = []

    for i in text_olimpiada:
        if i != " " and i != "\n" and i != "\x0c":
            o.append(i)

    olimpiada = ''.join(o)

    return olimpiada.lower() #->ОТПРАВКА ОТВЕТА    

#--Распознавание имени и фамилии
def fn_recognition(photo):

    img = cv2.imread(photo)

    familia = img[92:117, 79:475]
    name = img[131:155, 79:475]
      
    gray_familia = cv2.cvtColor(familia, cv2.COLOR_BGR2GRAY)
    gray_name = cv2.cvtColor(name, cv2.COLOR_BGR2GRAY)

    text_famila = pytesseract.image_to_string(gray_familia, lang="rus")
    text_name = pytesseract.image_to_string(gray_name, lang="rus")

    f = []
    n = []

    for i in text_famila:
        if i != " " and i != "\n" and i != "\x0c":
            f.append(i)

    for i in text_name:
        if i != " " and i != "\n" and i != "\x0c":
            n.append(i)

    first_name = ''.join(f)
    last_name = ''.join(n)

    return first_name.lower(), last_name.lower() #->ОТПРАВКА ОТВЕТА
#--Распознавание имени и фамилии

#--Распознавание номера класса
def class_recognition(photo):

    img = cv2.imread(photo)

    i = 110
    j = 234
    k = 0 

    while k < 10:
        k = k + 1

        i = i + 26

        if np.any(img[j, i] < 75):
            return f"{k+1}"

    return "0" #->ОТПРАВКА ОТВЕТА
#--Распознавание номера класса


#--Распознавание ответов ученика на бланке
def blank_recognition(photo):

    i = 0

    answers_number = []
    answers_bukcs = []

    for i in range(6):
        img = cv2.imread(photo)
        i = i + 1

        if i == 1:
            i = 34
            j = 342

            start_i = i
            start_j = j

            k = 0 

        elif i == 2:
            i = 279
            j = 342

            start_i = i
            start_j = j
            
            k = 0 

        elif i == 3:
            i = 34
            j = 457

            start_i = i
            start_j = j
            
            k = 0 

        elif i == 4:
            i = 279
            j = 458

            start_i = i
            start_j = j
            
            k = 0 

        elif i == 5:
            i = 34
            j = 571

            start_i = i
            start_j = j
            
            k = 0 

        elif i == 6:
            i = 279
            j = 572

            start_i = i
            start_j = j
            
            k = 0             

        while k < 40:
            k = k + 1
            if k == 5 or k == 9 or k == 13 or k == 17 or k == 21 or k == 25 or k == 29 or k == 33 or k == 37:
                j = start_j
                i = i + 22

            j = j + 22
            

            if np.any(img[j, i] < 75):
                answers_number.append(k)

    for jj in answers_number:
        if jj == 1 or jj == 5 or jj == 9 or jj == 13 or jj == 17 or jj == 21 or jj == 25 or jj == 29 or jj == 33 or jj == 37:
            answers_bukcs.append("A")
        elif jj == 2 or jj == 6 or jj == 10 or jj == 14 or jj == 18 or jj == 22 or jj == 26 or jj == 30 or jj == 34 or jj == 38:
            answers_bukcs.append("B")
        elif jj == 3 or jj == 7 or jj == 11 or jj == 15 or jj == 19 or jj == 23 or jj == 27 or jj == 31 or jj == 35 or jj == 39:
            answers_bukcs.append("C")	
        else:
            answers_bukcs.append("D")

    return answers_bukcs #->ОТПРАВКА ОТВЕТА
#--Распознавание ответов ученика на бланке

#--Конец
cv2.waitKey(0)
cv2.destroyAllWindows()
#--Конец