FROM ubuntu:18.04

# Install python and java, unzip, curl for allure
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev default-jre unzip curl \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# Download allure command line
RUN cd / \
    && curl -OL https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.9/allure-commandline-2.13.9.zip \
    && unzip allure-commandline-2.13.9.zip -d /opt/allure  \
    && chmod +x /opt/allure/allure-2.13.9/bin/allure
ENV PATH "$PATH:/opt/allure/allure-2.13.9/bin/"

# Install requirements
COPY tmp/requirements.txt /root/
RUN pip3 install -r /root/requirements.txt
