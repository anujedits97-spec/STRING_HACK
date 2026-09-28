# TEAM PURVI ALL COPYRIGHT ©️
import os

class Config:
    API_ID = int(os.getenv("API_ID", "27079591"))
    API_HASH = os.getenv("API_HASH", "c81ae4c3dc026ea4bf49842a8ce4a5f9")
    TOKEN = os.getenv("TOKEN", "8719198691:AAF7ih4ZYw3u5slpMPvQCklabPBQ5suuXSI")
    MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Anujedit:Anujedit@cluster0.7cs2nhd.mongodb.net/?appName=Cluster0")
    OWNER_ID = int(os.getenv("OWNER_ID", "8729304171"))
    LOGGER_GROUP_ID = int(os.getenv("LOGGER_GROUP_ID", "-1003951808679"))
    START_PIC = os.getenv("START_PIC", "https://files.catbox.moe/ppvvg0.jpg")
