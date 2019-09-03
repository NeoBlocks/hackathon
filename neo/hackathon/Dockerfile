FROM ubuntu:bionic
SHELL ["/bin/bash", "-c"]
WORKDIR /app
RUN apt update
RUN apt install -y -f libleveldb-dev python3.7 python3.7-dev python3-pip libleveldb-dev libssl-dev g++
RUN rm /var/lib/apt/lists/* -fr
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 10
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 10
COPY neo-python/ ./
COPY ./config.json ./
RUN ["/usr/bin/pip3", "install", "wheel", "-e", "."]
RUN ["mkdir", "-p", "data"]
ENV DEBIAN_FRONTEND noninteractive
CMD ["np-prompt", "--config", "config.json", "--datadir", "/app/data"]
