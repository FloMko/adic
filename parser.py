# import light http client
import requests
# import for parsing giv
from bs4 import BeautifulSoup


# set url
html = 'https://eqt-adidas.ru/'
# Adding urlencoded header for (?)
req_headers = {
    'Content-type': 'application/x-www-form-urlencoded'
}
# set
session = requests.session()
r = session.get(html)

# Need encode
text = r.text.encode('utf-8')

soup = BeautifulSoup(text)
soup.findAll('div')
soup.find('span').get_text()
