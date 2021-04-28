from os import getenv
from dotenv import load_dotenv

load_dotenv()

API = int(getenv("API_ID"))
APD = getenv("API_HASH")
STRING1 = getenv("STRING1")
STRING2 = getenv("STRING2")
STRING3 = getenv("STRING3")
SUDO = list(map(int, getenv("SUDO").split()))