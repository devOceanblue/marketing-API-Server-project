FROM python:3.10

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

ENV DB_HOST localhost
ENV DB_PORT 3306
ENV DB_NAME buzzvil
ENV DB_USER test_user
ENV DB_PASSWORD zxcsfqersdr123@~!

ENV LOG_LEVEL DEBUG

ENV CTR_PREDICTION_SERVER https://predict-ctr-pmj4td4sjq-du.a.run.app/


EXPOSE 8082

CMD uvicorn main:app --host 0.0.0.0 --port 8082
