FROM python:3.6-slim

ENV PYTHONBUFFERED 1

RUN mkdir /src
WORKDIR /src
ADD . /src/

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ \
    -r requirements.txt \
    && python manage.py migrate \
    && python manage.py collectstatic

EXPOSE 8000
CMD [ "gunicorn", "csthome.wsgi", "-b", "0.0.0.0:8000" ]
