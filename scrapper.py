import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
import sqlite3
import uuid

url = "https://www.theverge.com"
response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")

script_tag = soup.find("script", type="application/json")

# Extract the JSON data from the script tag
json_start = script_tag.string.index("{")
json_end = script_tag.string.rindex("}") + 1
json_data = json.loads(script_tag.string[json_start:json_end])

# Store json data in a json file
# stringify json data
stringified = json.dumps(json_data)

# Get the details of each articles
data = json_data["props"]["pageProps"]["hydration"]["responses"][0]["data"]
placements = data["community"]["frontPage"]["placements"]


# # Connect to the SQLite database and create a new table
# conn = sqlite3.connect("verge_articles.db")
# c = conn.cursor()
# c.execute(
#     """CREATE TABLE IF NOT EXISTS articles (id TEXT PRIMARY KEY, title TEXT, author TEXT, date DATETIME, url TEXT)"""
# )

response = []
for placement in placements:
    details = placement["placeable"]
    if details == None:
        continue
    durl = details["url"]
    title = details["title"]
    author = details["author"]["fullName"]
    date = details["publishDate"]
    id = uuid.uuid4()
    # Format the date 2023-04-05T12:30:00.000Z to pandas datetime format
    date = pd.to_datetime(date.replace(".000Z", ""))
    response.append([str(id), title, author, date, durl])


print(response)
