FROM python:2.7
ADD . /jusm
WORKDIR /jusm
RUN pip install -r requirements.txt
