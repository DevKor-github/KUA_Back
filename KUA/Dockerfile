FROM python:3.12.2

WORKDIR /devkor-teamb-back

COPY . /devkor-teamb-back/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["bash", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]