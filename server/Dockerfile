FROM python:3.10 as dev

RUN apt-get install python3-dev default-libmysqlclient-dev build-essential

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
