import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as BS


url = 'hhttps://www.cse.iitb.ac.in/academics/courses'
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8"
}
response = rq.get(url,headers=headers)
soup = BS(response.content,'html5lib')
print(soup.prettify)