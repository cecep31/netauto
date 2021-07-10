FROM python:3.8-slim

WORKDIR /app    

COPY . .

COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 80

CMD exec python manage.py runserver 0.0.0.0:80