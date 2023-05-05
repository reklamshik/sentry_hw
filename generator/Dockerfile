FROM python:3-alpine

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ADD generate_nums.py /var/server/generator.py

CMD python /var/server/generator.py
