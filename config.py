import os
import platform
import configparser

home_dir = (
    os.environ["userprofile"] if platform.system() == "Windows"
    else os.path.expanduser("~")
)
config_file_full_path = os.path.join(home_dir, "dhs622.cfg")

config = configparser.ConfigParser()
config.read(config_file_full_path)

app_name=config['telegram-api-info']['app-name']
api_id=config['telegram-api-info']['api-id']
api_hash=config['telegram-api-info']['api-hash']