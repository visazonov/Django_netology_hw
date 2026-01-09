import os

from dotenv import load_dotenv
load_dotenv()
PASSWORD = os.getenv('PASS_POSTGRES')
PASS = os.getenv('PASS')

print(PASSWORD)
print(PASS)
print(repr(PASSWORD))
print(repr(PASS))


