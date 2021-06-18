FROM python:3.6.8
LABEL maintainer="andy"

ENV LC_ALL C.UTF-8
ENV LANGUAGE C.UTF-8
ENV TZ=Asia/Shanghai

RUN sed -i s/deb.debian/ftp.cn.debian/g /etc/apt/sources.list \
    && apt update \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

WORKDIR opt

COPY requirements.txt .

RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple \
    && pip install pip -U --no-cache-dir \
    && pip install --no-cache-dir -r requirements.txt
