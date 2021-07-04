FROM python:3.8-alpine3.13

WORKDIR /app    

COPY . .

COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 80

CMD exec python manage.py runserver 0.0.0.0:80