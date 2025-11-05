FROM python:3.12

WORKDIR /usr/src/app

COPY requirements.lock ./

RUN pip install --no-cache-dir -r requirements.lock

COPY . .

EXPOSE 8000

