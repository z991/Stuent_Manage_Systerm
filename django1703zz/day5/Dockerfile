FROM python:3.6.2
LABEL maintainer zhuxuanyu
ENV PYTHONUNBUFFERED 1
RUN mkdir /docker_api
WORKDIR /docker_api
COPY . /docker_api/
RUN pip install -r requirements.txt  -i https://pypi.doubanio.com/simple

