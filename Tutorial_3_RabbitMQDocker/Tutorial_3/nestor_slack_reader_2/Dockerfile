FROM python:3.6.3

ENV SLACK_TOKEN			        xoxb-1495345635138-1519199846144-kRr0qh6jeMaQrGWV7MvJbBQw
ENV SLACK_SIGNING_SECRET		f59fa42f8d29320e0eaa331fed4a7a26

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_slack_reader_2

COPY ./nestor_slack_reader_2.py /nestor_slack_reader_2.py

CMD [ "python", "/nestor_slack_reader_2.py" ]
