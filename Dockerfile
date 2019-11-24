FROM python:3.5

COPY requirements.txt /tmp/

RUN apt-get update && apt-get -y install cmake
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

COPY . /super_dan

CMD echo "Hello world"