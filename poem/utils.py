import os
from dotenv import load_dotenv


def get_api_key(a):
    load_dotenv()
    key = os.environ[a]
    return key