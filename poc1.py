import json
from telethon.sync import TelegramClient
from telethon import functions
from config import app_name, api_id, api_hash

# Input data
channel_names = ["rybar","mig41"]

# Retrieve channel metadata from Telegram API
with TelegramClient(app_name, api_id, api_hash) as client:
    for channel_name in channel_names:
        channel_object = client(
            functions.channels.GetFullChannelRequest(channel=channel_name)
        )

        if channel_object is not None:
            print(channel_object.to_dict())

data = channel_object.to_dict()
print(json.dumps(data, indent=2, default=str))

channel_data = {
    'channel_id': data['full_chat']['id'],
    'title': data['chats'][0]['title'],
    'username': data['chats'][0]['username'],
    'description': data['full_chat']['about'],
    'participants_count': data['full_chat']['participants_count'],
    'verified': data['chats'][0]['verified'],
    'broadcast': data['chats'][0]['broadcast'],
    'creation_date': data['chats'][0]['date'],
    'reactions_limit': data['full_chat']['reactions_limit'],
}

# Print the cleaned data
print("\n=== CLEANED CHANNEL DATA ===")
print(json.dumps(channel_data, indent=2, default=str))

# Access nested data
print(f"\nChannel: {channel_data['title']}")
print(f"Subscribers: {channel_data['participants_count']:,}")
print(f"Description: {channel_data['description'][:100]}...")

