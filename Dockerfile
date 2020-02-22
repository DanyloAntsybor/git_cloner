FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev curl

ADD . .
RUN pip3 install -r ./env/requirements.txt
CMD [ "main.py" ]