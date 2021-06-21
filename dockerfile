FROM python:3.8

WORKDIR /app        

COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 8000

CMD exec python manage.py runserver 0.0.0.0:8000