# Import Libraries
import asyncio
import os
import pandas as pd
import json
from telethon.sync import TelegramClient
from telethon import functions
from telethon.tl.types import ChatFull
import time
import sys

if sys.platform == "darwin"
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)

from config import app_name, api_id, api_hash

# import data parsing

def extract_data_dictionary_from_channel_object(
    channel_object: ChatFull, channel_name: str
) -> dict:
    return {
        "channel_name": channel_name,
        "channel_id": channel_object.to_dict()["full_chat"]["id"],
        "channel_title": channel_object.to_dict()["chats"][0]["title"],
        "num_subscribers": channel_object.to_dict()["full_chat"]["participants_count"],
        "channel_bio": channel_object.to_dict()["full_chat"]["about"],
        "channel_birthdate": channel_object.to_dict()["chats"][0]["date"],
        # "api_response": channel_object.to_json(),
    }



# Input data
channel_names = ["rybar","mig41",]

output_dir = "/Users/apple/PycharmProjects/dhs622zs"

# Retrieve channel metadata from Telegram API
with TelegramClient(app_name, api_id, api_hash) as client:
    for channel_name in channel_names:
        channel_object = client(
            functions.channels.GetFullChannelRequest(channel=channel_name)
        )

        if channel_object is not None:
            print(channel_object.to_dict())
            print (".𖥔 ݁ ˖ִ ࣪⚝₊ ⊹˚.𖥔 ݁ ˖ִ ࣪⚝₊ ⊹˚.𖥔 ݁ ˖ִ ࣪⚝₊ ⊹˚.𖥔 ݁ ˖ִ ࣪⚝₊ ⊹˚.𖥔 ݁ ˖ִ ࣪⚝₊ ⊹˚.𖥔 ݁ ˖ִ ࣪⚝₊ ⊹˚.𖥔 ݁ ˖ִ ࣪⚝₊ ⊹˚.𖥔 ݁ ˖ִ ࣪⚝₊ ⊹˚")

            data = extract_data_dictionary_from_channel_object(channel_object, channel_name)
            print(json.dumps(data, indent=2, default=str))
            my_file_full_path = os.path.join(output_dir, "scary_stuff.jsonl")
            with open(my_file_full_path, 'a') as myfile:
                myfile.write(json.dumps(channel_object.to_json()) + '\n')

            df = pd.DataFrame.from_records([data])
            my_file_full_path = os.path.join(output_dir, "scary_stuff.csv")
            df.to_csv(my_file_full_path, index=False, encoding="utf-8-sig", mode='a', header=False)

        print ("☆ WAITT Y'ALL LITERALLY WE NEED THIS AS AN APP- ☆")
        time.sleep(5)
