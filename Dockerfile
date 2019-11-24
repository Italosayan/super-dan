FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY requirements.txt /tmp/

RUN apt-get update && apt-get -y install cmake
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt
