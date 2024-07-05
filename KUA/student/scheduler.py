from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
import psycopg2
import random
from django.utils import timezone
from datetime import datetime, timedelta


scheduler = BackgroundScheduler()

nickname_animal = ['사자', '고양이', '강아지', '호랑이', '매', '양', '토끼', '용', '용', '다람쥐', '돼지', '소', '쥐', '파리', '모기',
                   '까마귀', '벌', '개미', '염소', '하마', '코뿔소', '곰', '뱀', '원숭이', '고릴라', '말']

def update_data():
    # DB 연결
    try:
        conn = psycopg2.connect(host='localhost', dbname="kua", user="postgres", password="postgres")
    except psycopg2.DatabaseError as db_err:
        print(db_err)
        return False

    cur = conn.cursor()
    
    # 랜덤 숫자 만들기 
    cur.execute('SELECT id FROM student_student;')
    student_ids = cur.fetchall()
    student_number = len(student_ids)
    
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
            VALUES ( %s, %s, %s);
        ''', (student_id, nickname, nickname_change_time))
    
    conn.commit()
    conn.close()

    print("Data updated successfully!")
    return True


scheduler = BackgroundScheduler()

def start_scheduler():
    start_time = datetime(2024, 7, 4, 0, 0, 0)
    if not scheduler.running:
        # 2024년 7월 4일 오전 12시 이후 1분마다 실행되도록 설정
        scheduler.add_job(update_data, 'interval', hours=24, start_date=start_time)
        scheduler.start()