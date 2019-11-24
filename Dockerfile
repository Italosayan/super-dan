FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY requirements.txt /tmp/

RUN apt-get install cmake
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

COPY . /super_dan
