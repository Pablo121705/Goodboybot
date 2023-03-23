import os

class Config:
    TELEGRAM_TOKEN=os.environ['TELEGRAM_TOKEN', None]
    PYRO_SESSION=os.environ['PYRO_SESSION']
    TELEGRAM_APP_HASH=os.environ['TELEGRAM_APP_HASH']
    TELEGRAM_APP_ID=int(os.environ['TELEGRAM_APP_ID'])
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
