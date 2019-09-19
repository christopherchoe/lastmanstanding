FROM node:0.12.7 AS builder
RUN npm install webpack -g
WORKDIR /usr/src/app
RUN npm install webpack -g
COPY . .


FROM python:3.7.0-alpine3.8
WORKDIR /root/
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY --from=builder /usr/src/app .
ENV FLASK_APP=app.py
CMD flask run --host=0.0.0.0
EXPOSE 5000
