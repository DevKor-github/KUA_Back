FROM python:3.12.2

WORKDIR /kua

COPY . /kua/

RUN pip install -r requirements.txt

EXPOSE 8000

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
