import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

hook_url = os.getenv('URL')
urlsFile = open('urls.json')
urls = json.load(urlsFile)

statuses = {}

for url in urls['urls']:
    code = None
    try:
        code = requests.get(url).status_code
    except requests.exceptions.ConnectionError as errc:
        code = "Problem Here"
    statuses[url] = code

requests.post(
    url=hook_url,
    headers={"Content-Type": "application/json; charset=utf-8", "Accept": "application/json"},
    json={"content": json.dumps(statuses)}
)
