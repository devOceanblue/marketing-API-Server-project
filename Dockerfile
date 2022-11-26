FROM python:3.10

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

EXPOSE 8082

CMD uvicorn main:app --host 0.0.0.0 --port 8082





