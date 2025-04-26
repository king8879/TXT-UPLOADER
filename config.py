import os

API_ID = os.environ.get"API_ID","22923037"  

API_HASH = os.environ.get("API_HASH", "dfb3666878b3851460a58461c5a50f5b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7370337739:AAH3pjIlvyyqHqdHFKWJR8hnbnuvobbkVA4")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("6554343173", ))

LOG = "-1002540145139"

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6554343173").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


