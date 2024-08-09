import requests
from bs4 import BeautifulSoup

api_url = 'https://www.kaggle.com/datasets/arianazmoudeh/airbnbopendata'
response = requests.get(api_url)
soup = BeauitifulSoup(response.content)
print(soup.prettify())
