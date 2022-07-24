FROM python:3.10-alpine3.15

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN  pip3 install -r requirements.txt \
     && apk add -u gcc musl-dev \
     && apt update && apt install gcc

COPY . /app/

CMD ["python3", "manage.py", "runserver", "127.0.0.1:8000"]