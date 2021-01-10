FROM python:3.6.3

ENV SLACK_TOKEN			xoxb-1495345635138-1519199846144-kRr0qh6jeMaQrGWV7MvJbBQw

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /nestor_slack_writer

COPY ./nestor_slack_writer.py /nestor_slack_writer.py
COPY ./nestor_slack_writer.py /nestor_slack_writer.py

CMD [ "python", "/nestor_slack_writer.py" ]
