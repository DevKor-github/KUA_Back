FROM python:3.12.2

WORKDIR /devkor-teamb-back

COPY . /devkor-teamb-back/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python","manage.py", "runserver"]