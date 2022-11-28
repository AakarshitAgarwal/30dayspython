import requests

r = requests.get('https://financialmodelingprep.com/api/v3/rss_feed?page=0&apikey=6338ffcb3a553cb542903a126c26e1b1')
print(r.text)