import requests
import json
from bs4 import BeautifulSoup

url = "https://www.theverge.com"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")

