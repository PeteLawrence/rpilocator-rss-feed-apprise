import apprise
import feedparser
import os
import requests
import time

# Create variables from environment
FEED_URL = os.environ.get('FEED_URL')
MESSAGE_TITLE = os.environ.get('MESSAGE_TITLE')
USER_AGENT = os.environ.get('USER_AGENT')
APPRISE_TARGET = os.environ.get('APPRISE_TARGET')

# Send the push/message to apprise
def sendMessage(message):
    ap.notify(
        title=MESSAGE_TITLE,
        body=message
    )

#
print(os.environ.get('MESSAGE_TITLE'))

# Set control to blank list
control = []

# Fetch the feed
print(f'Using {FEED_URL}')
f = feedparser.parse(FEED_URL, agent=USER_AGENT)

# If there are entries in the feed, add entry guid to the control variable
if f.entries:
    for entries in f.entries:
        control.append(entries.id)

ap = apprise.Apprise()
ap.add(APPRISE_TARGET)
print(f'Sending stock updates to {APPRISE_TARGET}')
sendMessage(f'Monitoring {FEED_URL} for updates')

#Only wait 30 seconds after initial run.
time.sleep(3)

while True:
    # Fetch the feed again, and again, and again...
    f = feedparser.parse(FEED_URL, agent=USER_AGENT)

    # Compare feed entries to control list.
    # If there are new entries, send a message/push
    # and add the new entry to control variable
    for entry in f.entries:
        if entry.id not in control:
            # Product is newly in stock
            message=entry.title

            print(message)
            sendMessage(message)

            # Add entry guid to the control variable
            control.append(entry.id)

    time.sleep(59)
