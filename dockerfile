FROM python:3.8

WORKDIR /app        

COPY requirements.txt ./

RUN pip install –no-cache-dir -r requirements.txt

EXPOSE 8000

CMD exec gunicorn webapp.wsgi:application –bind 0.0.0.0:8000 –workers 3