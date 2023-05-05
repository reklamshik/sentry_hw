FROM python:3-alpine

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ADD app_with_remote_sentry.py /var/server/app.py

CMD python /var/server/app.py
