FROM python:3.8
ADD . /API
WORKDIR /API
RUN pip --timeout=1000 install -r requirements.txt