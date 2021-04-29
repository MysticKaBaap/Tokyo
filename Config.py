from os import getenv
from dotenv import load_dotenv

load_dotenv()

STRING1 = getenv("STRING1")
SUDO = list(map(int, getenv("SUDO").split()))
