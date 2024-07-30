FROM python:3.12.2

WORKDIR /devkor-teamb-back/KUA

COPY . /devkor-teamb-back/KUA/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python","manage.py", "runserver"]