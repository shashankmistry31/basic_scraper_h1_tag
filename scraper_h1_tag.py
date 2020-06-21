import requests,bs4

res = requests.get('http://example.com/')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,'html.parser')
print(soup.h1) #no need of select - will get first h1 tag
