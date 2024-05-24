from requests import post
from dotenv import load_dotenv, dotenv_values
from time import sleep
from datetime import datetime


# Load environment variables from .env file
load_dotenv()

conf = dotenv_values(".env")


def perform_hamster_glitch():
    headers = {
        'Host': 'api.hamsterkombat.io',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://hamsterkombat.io/',
        'Authorization': f'Bearer {conf["AUTH_TOKEN"]}',
        'Content-Type': 'application/json',
        'Origin': 'https://hamsterkombat.io',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Connection': 'close',
    }
    json_data = {
        'count': 1000,
        'availableTaps': 1000,
        'timestamp': int(str(datetime.now().timestamp()).split(".")[0])
    }

    post('http://api.hamsterkombat.io/clicker/tap', headers=headers, json=json_data, proxies={"http": "http://127.0.0.1:8080"})

if __name__ == "__main__":
    while True:
        perform_hamster_glitch()
        sleep(30)