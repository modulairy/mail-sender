FROM python:3.8-slim

WORKDIR /modulairy


# Install dependencies

RUN pip install modulairy-mail-sender

# Run the application

CMD ["python","-m","modulairy_mail_sender"]

