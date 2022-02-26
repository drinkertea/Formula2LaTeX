FROM python:3.9-slim-buster

COPY . /bot
WORKDIR /bot

RUN pip install --upgrade pip && pip install --no-cache-dir -r /bot/requirements.txt
ENV PYTHONUNBUFFERED=1

CMD python /bot/run_bot.py