FROM tangchen2018/python:3.6-alpine
ENV PYTHONUNBUFFERED 1

COPY . /project/server

WORKDIR /project/server

RUN apk add --no-cache tzdata build-base libffi-dev openssl-dev python-dev py-pip && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone


RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && mkdir -p /project/server/logs

CMD python /project/server/main.py
#CMD ["python", "/project/sso/manage.py crontab remove"]
#CMD ["python", "/project/sso/manage.py crontab add"]
