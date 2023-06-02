FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./rpilocator-rss-appraise.py ./

CMD ["python", "./rpilocator-rss-appraise.py"]

ENV FEED_URL='https://rpilocator.com/feed/'
ENV MESSAGE_TITLE='RPI Locator Stock Alert'
ENV USER_AGENT='xlocator feed alert'
ENV APPRISE_TARGET='syslog://'