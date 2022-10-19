FROM python:3.10 as dev

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 4000
CMD [ "python", "./main.py" ]
