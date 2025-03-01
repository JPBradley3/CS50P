## There is a package for API calls that can be used
## Many of themm are only web based
## Can be collaborated with online too
## This example uses itunes fro https://itunes.apple.com/search?entity=song&limit=1&term and https://itunes.apple.com/search?entity=song&limit=1&term=weezer
## We take "Weezer" out and then we apply a more general search using argv(1) from the command line

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

## This is where we edit the html link and append the end to add another band name to search with in the apple data bank.
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])
