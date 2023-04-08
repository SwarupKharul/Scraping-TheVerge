import requests
import json
from bs4 import BeautifulSoup

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

for placement in placements:
    details = placement["placeable"]
    if details == None:
        continue
    url = details["url"]
    title = details["title"]
    author = details["author"]["fullName"]
    date = details["publishDate"]
    print(f"{title} by {author} on {date} - {url}]\n")
