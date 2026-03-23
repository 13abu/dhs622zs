## Proof of concept with config data hidden and data dictionary flattened

import asyncio
import sys

# Create and set event loop before any Telethon imports
if sys.platform in ('win32', 'darwin'):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from week7.utilities.logic import retrieve_and_save_channel_metadata
from week7.config import app_name, api_id, api_hash, INPUT_DIR
import os
import pandas as pd

if __name__ == '__main__':
    seed_list_name = 'indian_military_nationalism'
    channel_names = ["IndianMilitaryUpdates", "bnpkukrti", "BadrulBSL","Diplomatic_Talk","Turkeypedia","newsIEA","OsintTV","russiaukrwar","vishwahinduektasangh","hindu"]

    retrieve_and_save_channel_metadata(
        channel_names, app_name, api_id, api_hash, seed_list_name
    )