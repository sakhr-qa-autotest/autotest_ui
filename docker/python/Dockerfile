FROM ubuntu:22.04

RUN apt-get update --fix-missing
RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y tzdata
RUN ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/locatime
ENV TZ=Europe/Moscow

RUN apt-get install locales
RUN locale-gen en_US.UTF-8
RUN locale-gen ru_RU.UTF-8
RUN export LANG=en_US.UTF-8
RUN export LANG=C.UTF-8
RUN dpkg-reconfigure locales
RUN apt-get update -q

RUN apt-get update && apt-get install -y gnupg2
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main"  >> /etc/apt/sources.list.d/google.list'
RUN apt update
RUN apt install -y google-chrome-stable

RUN apt-get install -y software-properties-common
RUN apt-get install -y apt-transport-https
RUN apt-get install -qy --force-yes \
                      make \
                      curl \
                      vim \
                      nano \
                      net-tools \
                      iputils-ping \
                      git

RUN apt-get -y install libmagic1
RUN apt-get -y install python3
RUN apt-get -y install python3.10-venv
RUN apt-get -y install pip

RUN pip install poetry

RUN mkdir /var/pythonproject
WORKDIR /var/pythonproject/
RUN python3 -m venv .venv
RUN google-chrome --version
