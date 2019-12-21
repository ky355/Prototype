from bs4 import BeautifulSoup
import requests

# Set headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0' })

url = "https://termmasterschedule.drexel.edu/webtms_du/app"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())

# go into specific term

# get input of what is needed
