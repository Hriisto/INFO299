import os
from slack import WebClient
import slack
from benja import Benja

# Initialize a Web API client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Create a new Benja
benja_bot = Benja("#bot")

# Get the onboarding message payload
message = benja_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)
