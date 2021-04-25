FROM python:3.8.9-alpine3.13
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . /code/
CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]
