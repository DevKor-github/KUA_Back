from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
import psycopg2
import random
from django.utils import timezone
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

scheduler = BackgroundScheduler()

load_dotenv()

nickname_animal = ["소","금붕어","우파루파","여우","뱀","양","판다","호랑이","고양이","범고래","카멜레온","오리","거북이","비버","청둥오리","원숭이",
                           "쥐","표범","물소","곰","하마","강아지","게","코끼리","무당벌레","코뿔소","말","문어","벌","닭","사자","바다사자","나비","북극곰","사슴","기린","홍학","개구리","물개","앵무새"]



def update_data():
    # DB 연결
    try:
        host = os.environ.get('DB_HOST')
        dbname = os.environ.get('DB_NAME')
        dbuser = os.environ.get('DB_USER')
        dbpassword = os.environ.get('DB_PASSWORD')
        conn = psycopg2.connect(host=host, dbname=dbname,
                                user=dbuser, password=dbpassword)
    except psycopg2.DatabaseError as db_err:
        print(db_err)
        return False

    cur = conn.cursor()

    # 랜덤 숫자 만들기
    cur.execute('SELECT id FROM student_student;')
    student_ids = cur.fetchall()
    student_number = len(student_ids)

    cur.execute('SELECT id FROM student_nicknamehistory;')
    history_ids = cur.fetchall()
    history_number = len(history_ids) + 1

    if student_number == 0:
        print("No students found.")
        conn.close()
        return False

    numbers = list(range(student_number))
    random.shuffle(numbers)

    # 랜덤 닉네임 만들기
    random_animal = random.choices(nickname_animal, k=student_number)
    nicknames = []
    for i, j in zip(random_animal, numbers):
        nicknames.append(i + str(j))

    for i in range(student_number):
        student_id = student_ids[i][0]
        nickname = nicknames[i]
        nickname_change_time = timezone.now()
        cur.execute('''
            UPDATE student_student
            SET nickname = %s, nickname_change_time = %s
            WHERE id = %s;
        ''', (nickname, nickname_change_time, student_id))
        cur.execute('''
            INSERT INTO student_nicknamehistory
            VALUES ( %s, %s, %s, %s);
        ''', (history_number, nickname, nickname_change_time, student_id))
        history_number += 1

    conn.commit()
    conn.close()

    print("Data updated successfully!")
    return True


def start_scheduler():
    start_time = datetime(2024, 7, 4, 0, 0, 0)
    if not scheduler.running:
        # 2024년 7월 4일 오전 12시 이후 1분마다 실행되도록 설정
        scheduler.add_job(update_data, 'interval',
                          minutes = 1, start_date=start_time)
        scheduler.start()
