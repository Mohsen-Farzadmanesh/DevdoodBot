FROM python:3

WORKDIR /app

RUN pip install pyTelegramBotAPI

COPY * /app/

CMD ["python", "bot.py"]