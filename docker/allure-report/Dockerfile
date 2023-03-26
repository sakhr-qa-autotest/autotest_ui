FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y openjdk-8-jre
RUN apt-get install -y openjdk-8-jdk
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
RUN mkdir /var/allure-results

COPY ./docker/allure-report/allure_2.21.0-1_all.deb /var/allure-results/
RUN ls -la /var/allure-results
RUN dpkg -i /var/allure-results/allure_2.21.0-1_all.deb
WORKDIR /var/allure-results
