FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev curl

COPY ./env/requirements.txt /env/requirements.txt

RUN pip3 install -r ./env/requirements.txt
RUN mkdir /code

WORKDIR /code

CMD ["python3", "cloner_app.py" ]