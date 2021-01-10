FROM python:3.9.1

ENV MONGO_PORT "mongodb://mongo:27017/"
ENV MONGO_HOST localhost
ENV SLACK_TOKEN="xoxb-1495345635138-1519199846144-kRr0qh6jeMaQrGWV7MvJbBQw"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR ./app

COPY ./benja.py /benja.py
COPY ./benja_app.py /benja_app.py

CMD [ "python", "/benja_app.py" ]