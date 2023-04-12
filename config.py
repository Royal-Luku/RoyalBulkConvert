# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "13556430"))
API_HASH = os.environ.get("API_HASH", "3531771c0d58b9ffc44d12f38c5edbf5")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5886907575:AAG4LY3SQh3aq9zLfM-qS3oKnaXQuPeF-_s")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1782834874")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Royal")
DATABASE_URL = os.getenv("DATABASE_URL", "Monfo url") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1782834874")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001810183335")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "worldofmovies8") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
