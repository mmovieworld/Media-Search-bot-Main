import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press following buttons and start searching.
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = '%E0%B4%B9%E0%B4%B2%E0%B5%8B%20%F0%9F%99%8C,%20@MMovie_World%20%E0%B5%BB%E0%B5%8D%E0%B4%B1%E0%B5%86%20%E0%B4%B8%E0%B4%BF%E0%B4%A8%E0%B4%BF%E0%B4%AE%E0%B4%BE%20%E0%B4%B8%E0%B5%86%E0%B5%BC%E0%B4%9A%E0%B5%8D%E0%B4%9A%E0%B5%8D%20%E0%B4%AC%E0%B5%8B%E0%B4%9F%E0%B5%8D%E0%B4%9F%E0%B5%8D%20%E0%B4%B5%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B4%BF%E0%B4%9F%E0%B5%8D%E0%B4%9F%E0%B5%81%E0%B4%A3%E0%B5%8D%E0%B4%9F%E0%B5%8D%20%E0%B4%88%20%E0%B4%9A%E0%B4%BE%E0%B4%B1%E0%B5%8D%E0%B4%B1%E0%B5%8D%20%E0%B4%AC%E0%B5%8B%E0%B4%9F%E0%B5%8D%E0%B4%9F%E0%B4%BF%E0%B5%BD%20Malayalam,%20Tamil,%20Hindi,%20Telugu,%20foreign%20Language%20%E0%B4%8E%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B5%80%20%E0%B4%AD%E0%B4%BE%E0%B4%B7%E0%B4%95%E0%B4%B3%E0%B4%BF%E0%B4%B2%E0%B5%86%20%E0%B4%B8%E0%B4%BF%E0%B4%A8%E0%B4%BF%E0%B4%AE%E0%B4%95%E0%B4%B3%E0%B5%81%E0%B4%82%20%E0%B4%B8%E0%B5%80%E0%B4%B0%E0%B4%BF%E0%B4%AF%E0%B4%B2%E0%B5%81%E0%B4%95%E0%B4%B3%E0%B5%81%E0%B4%82%20%E0%B4%B2%E0%B4%AD%E0%B5%8D%E0%B4%AF%E0%B4%AE%E0%B4%BE%E0%B4%A3%E0%B5%8D.%20%20%E0%B4%95%E0%B5%82%E0%B4%9F%E0%B5%81%E0%B4%A4%E0%B4%B2%E0%B5%8D%E2%80%8D%20%E0%B4%85%E0%B4%B1%E0%B4%BF%E0%B4%AF%E0%B4%BE%E0%B4%A8%E0%B5%8D%E2%80%8D%20@MMW_Search_Bot%20%E0%B5%BD%20%E0%B4%9A%E0%B5%86%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B5%8D%20START%20%E0%B4%95%E0%B5%8A%E0%B4%9F%E0%B5%81%E0%B4%A4%E0%B5%8D%E0%B4%A4%E0%B4%A4%E0%B4%BF%E0%B4%A8%E0%B5%8D%20%E0%B4%B6%E0%B5%87%E0%B4%B7%E0%B4%82%20/help%20%E0%B4%8E%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B5%8D%20%E0%B4%85%E0%B4%AF%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%81%E0%B4%95%20%E2%9E%A1%EF%B8%8F%20%20Hello%20%F0%9F%99%8C,%20@MMovie_World%20's%20search%20bot%20is%20now%20available.%20On%20this%20chat%20bot%20you%20can%20find%20Malayalam,%20Tamil,%20Hindi,%20Telugu,%20foreign%20Languages%20Movies%20and%20Series.%20%20For%20more%20details%20Got%20to%20@MMW_Search_Bot%20and%20Click%20START%20and%20type%20/help%20%E2%9E%A1%EF%B8%8F'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
