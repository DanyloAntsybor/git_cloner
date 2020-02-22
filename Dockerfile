FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev curl

# We copy just the requirements.txt first to leverage Docker cache
COPY ./env/requirements.txt /env/requirements.txt

RUN pip3 install -r ./env/requirements.txt
RUN mkdir /code

WORKDIR /code

#ENTRYPOINT [ "python3" ]

CMD [ "cloner_app.py" ]