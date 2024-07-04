from apscheduler.schedulers.background import BackgroundScheduler
import psycopg2
import random
from django.utils import timezone


scheduler = BackgroundScheduler()

nickname_animal = ['사자', '고양이', '강아지', '호랑이', '매', '양', '토끼', '용', '용', '다람쥐', '돼지', '소', '쥐', '파리', '모기',
                   '까마귀', '벌', '개미', '염소', '하마', '코뿔소', '곰', '뱀', '원숭이', '고릴라', '말']

def update_data():
    #DB 연결
    try:
        conn = psycopg2.connect(host='host.docker.internal', dbname="kua", user="postgres", password = "postgres")
    except psycopg2.DatabaseError as db_err:
        return db_err
    cur = conn.cursor()
    
    #랜덤 숫자 만들기 
    cur.execute('select count(*) from student_student;')
    student_number = cur.fetchall()[0]
    numbers = list(range(0, student_number))
    random.shuffle(numbers)

    #랜덤 닉네임 만들기
    random_animal = random.choices(nickname_animal, k=student_number)
    nicknames = []
    for i, j in zip(random_animal, numbers):
        nicknames.append(i+str(j))

    i = 0
    while student_number>0:
        cur.execute(f'select count(*) from student_student when id = {i};')
        is_exist = cur.fetchall()
        if is_exist == []:
            i += 1
            continue
        else:
            cur.execute(f'update student_student set nickname = {nicknames[student_number-1]} and nickname_change_time = {timezone.now()} when id = {i};')
            conn.commit()
            student_number -= 1
            i += 1

    print("Data updated successfully!")
    return True


# 스케줄링 작업 등록
scheduler.add_job(update_data, 'interval', minutes = 1)


# 스케줄링 작업 실행
scheduler.start()