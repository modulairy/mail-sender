FROM python:3.8-slim

WORKDIR /modulairy


RUN pip install --upgrade pip && pip install modulairy-mail-sender


CMD ["modulairy_mail_sender"]

