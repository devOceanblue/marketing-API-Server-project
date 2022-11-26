FROM python:3.10

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

ENV DB_HOST localhost
ENV DB_NAME buzzvil
ENV DB_USER root
ENV DB_PASSWORD zxcsfqersdr123@~!

EXPOSE 8082

CMD uvicorn main:app --host 0.0.0.0 --port 8082





