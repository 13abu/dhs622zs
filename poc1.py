from telethon.sync import TelegramClient
from telethon import functions

# Configuration data
app_name = "my_jalebi_app"
api_id = int("35206697")
api_hash = "361f05016f8aa55f5b88ce00f4231360"

# Input data
channel_names = ["rybar", "mig41"]

# Retrieve channel metadata from Telegram API
with TelegramClient(app_name, api_id, api_hash) as client:
    for channel_name in channel_names:
        channel_object = client(
            functions.channels.GetFullChannelRequest(channel=channel_name)
        )

        if channel_object is not None:
            print(channel_object.to_dict())

