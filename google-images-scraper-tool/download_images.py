import os

# Constants
chromedriver_path = "/Users/hannojacobs/chromedriver_mac_arm64/chromedriver"
num_images_to_dl = 100
script_name = "bing_scraper.py"

# Unique part of each command: the search queries
search_queries = [
    "bee Allodapula",
    "bee Apis mellifera scutellata",
    "bee Braunsapis",
    "bee Lasioglossum",
    "bee Meliponula",
    "bee Seladonia",
    "bee Xylocopa carpenter bee",
    "bee Thyreus thyreus nitidulus",
]

for query in search_queries:
    command = f"python3 {script_name} --search '{query}' --limit {num_images_to_dl} --download --chromedriver {chromedriver_path}"
    os.system(command)
