import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()


def write_to_log(str):
    f = open(os.getenv('PATH'), 'a')
    f.write(f"{str} {dt.datetime.now()} \n")
    f.close()