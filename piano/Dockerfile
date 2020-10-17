FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update ##[edited]
RUN apt-get install -y 'python3'
RUN apt-get install -y 'python3-pip'
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y

WORKDIR /usr/src/piano

COPY ./requirements.txt ./
RUN ["python3", "-m", "pip", "install", "--upgrade", "pip"]
RUN ["python3", "-m", "pip", "install", "-r", "requirements.txt"]
