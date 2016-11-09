import requests
#import sys
from bs4 import BeautifulSoup as bs

addr = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"
office_id = {"President" : 1, "Senator" : 6, "Representative" : 5}

mod_addr = addr.format(office_id['President'], 'General')
resp = requests.get(mod_addr)
soup = bs(resp.text, "html.parser")

election_id = []
election_year = []



soup.find_all("tr", "election_item")

for elections in soup.find_all("tr", "election_item"):
    x = elections['id'].split('-')[-1]
    election_id.append(x)
    year = elections.find("td", "year first").string
    election_year.append(year)


with open("ELECTION_ID", "w") as output:
    for y in range(len(election_id)):
        line = " ".join([election_year[y], election_id[y]])
        output.write(line + "\n")
