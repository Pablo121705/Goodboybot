import os
from os import getenv

class Config:
    TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN","7519586705:AAEPvYf5XKXre0eF6QI6q1Ne50sshH3ti04" None)
    PYRO_SESSION = getenv("PYRO_SESSION", None)
    TELEGRAM_APP_HASH= getenv('TELEGRAM_APP_HASH',"2135724a8fdecb737f31d22ec8e6894b")
    TELEGRAM_APP_ID=int(getenv('TELEGRAM_APP_ID',"25206101"))
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
    if not TELEGRAM_TOKEN or not PYRO_SESSION:
        raise ValueError("PYRO_SESSION / TELEGRAM_TOKEN not set")
