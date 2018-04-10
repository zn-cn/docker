FROM python:3.6
MAINTAINER Zhao Nan <yun_tofar@qq.com>

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt
