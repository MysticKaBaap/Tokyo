from os import getenv
from dotenv import load_dotenv

load_dotenv()

STRING = getenv("SESSION")
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
BIO_MESSAGE = getenv("BIO")
SUDO = list(map(int, getenv("SUDO").split()))
