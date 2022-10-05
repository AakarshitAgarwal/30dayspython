import requests
from bs4 import BeautifulSoup

user = "angelinajolie"
url = 'https://www.instagram.com/'+user
r = requests.get(url) 
soup = BeautifulSoup(r.content)
followers = soup.find('meta', {'name': 'description'} )
followers_count = followers.split('Followers')[0]
print(followers_count)