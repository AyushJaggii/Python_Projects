import requests
from bs4 import BeautifulSoup

search = "Weather in Jammu"                              # Creating the search query for Jammu weather on Google
url = f"https://www.google.com/search?&q={search}"       # Creating the URL with the search query    


r = requests.get(url)                                    # Making a GET request to the URL and getting the response
s = BeautifulSoup(r.text, "html.parser")                 # Parsing the response HTML using BeautifulSoup


update = s.find("div", class_ = "BNeawe").text
print("Current temperature in Jammu is:", update.encode('ascii', 'ignore').decode('utf-8'))
