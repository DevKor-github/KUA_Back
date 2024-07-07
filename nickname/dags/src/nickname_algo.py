from datetime import datetime
import pendulum
import psycopg2
import random

nickname_animal = ['사자', '고양이', '강아지', '호랑이', '매', '양', '토끼', '용', '용', '다람쥐', '돼지', '소', '쥐', '파리', '모기',
                   '까마귀', '벌', '개미', '염소', '하마', '코뿔소', '곰', '뱀', '원숭이', '고릴라', '말']

def get_today():
    kst = pendulum.timezone('Asia/Seoul')
    current_time = datetime.now().astimezone(kst)
    dt_now = str(current_time.date())
    print(f'{dt_now} 기준')
    dt_now = ''.join(c for c in dt_now if c not in '-')
    return dt_now

def make_random_number_list(**context):
    try:
        conn = psycopg2.connect(host='host.docker.internal', dbname="kua", user="postgres", password = "postgres")
    except psycopg2.DatabaseError as db_err:
        return db_err
    cur = conn.cursor()
    cur.execute('select count(*) from student_student;')
    student_number = cur.fetchall()[0]
    numbers = list(range(0, student_number))
    random.shuffle(numbers)
    context['task_instance'].xcom_push(key='student_number', value = student_number)
    context['task_instance'].xcom_push(key='random_number', value=numbers)
    conn.close()
    return True

def make_random_nickname(**context):
    student_number = context['task_instance'].xcom_pull(key='student_number')
    numbers = context['task_instance'].xcom_pull(key = 'random_number')
    random_animal = random.choices(nickname_animal, k=student_number)

    nicknames = []
    for i, j in zip(random_animal, numbers):
        nicknames.append(i+str(j))
    
    context['task_instance'].xcom_push(key='nicknames', value = nicknames)
    return True

def set_nickname(**context):
    nicknames = context['task_instance'].xcom_pull(key='nicknames')     
    student_number = context['task_instance'].xcom_pull(key='student_number')
    
    try:
        conn = psycopg2.connect(host='host.docker.internal', dbname="kua", user="postgres", password = "postgres", port = 5432)
    except psycopg2.DatabaseError as db_err:
        return db_err
    cur = conn.cursor()

    i = 0
    while student_number>0:
        cur.execute(f'select count(*) from student_student when id = {i};')
        is_exist = cur.fetchall()[0]
        if is_exist == 0:
            i += 1
            continue
        else:
            cur.execute(f'update student_student set nickname = {nicknames[student_number-1]} when id = {i};')
            conn.commit()
            student_number -= 1
            i += 1
    conn.close()
    return True

    
        
        

    
