import requests
#import sys
from bs4 import BeautifulSoup as bs





for line in open("ELECTION_ID"):
    election_id = line.split()[-1]
    addr = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(election_id)
    resp = requests.get(addr)


    soup = bs(resp.text, "html.parser")

    year = line.split()[0]
    election_data = year +".csv"
    with open(election_data, "w") as output:
        output.write(soup.text)
