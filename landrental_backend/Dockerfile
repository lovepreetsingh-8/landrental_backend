FROM python:3.12.2-slim-bullseye

WORKDIR /usr/src/landrental_backend

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    python3-dev \
    && apt-get clean
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/landrental_backend/entrypoint.sh
RUN chmod +x /usr/src/landrental_backend/entrypoint.sh


COPY . . 

ENTRYPOINT [ "/usr/src/landrental_backend/entrypoint.sh" ]