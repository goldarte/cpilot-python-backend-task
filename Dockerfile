FROM redis

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update

RUN apt install -y \
    python3.9 \
    python3.9-dev \
    python3.9-distutils \
    build-essential \
    curl

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && ls &&\
    python3.9 get-pip.py

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN mkdir -p /server

COPY data/*.jpg /server/data/
COPY agroproto/ /server/agroproto/
COPY modules/ /server/modules/
COPY server.py /server/

COPY data/dump.rdb /data/
COPY data/start_script.sh start_script.sh

CMD ./start_script.sh
