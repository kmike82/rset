# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app
RUn apt-get update; apt-get install curl -y

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin

RUN mkdir /root/.kube
COPY config /root/.kube/config

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

CMD [ "python3", "app.py"]

