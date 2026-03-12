import requests 
import json
from bs4 import BeautifulSoup




# Specify url
url = 'https://www.python.org/~guido/'

# send a get request to get the page content 

response = requests.get(url)
# print(response.status_code)  #200 valid response 

# get content of html page 
html_doc  = response.text
# print(html_doc)

# to organize the output and make it clear we will use beautifulsoup 
# soup = BeautifulSoup(html_doc)
# print(soup.prettify())

# get page title 
# title = soup.title
# print(title)

# get all text 
# html_text = soup.get_text()
# print(html_text)


# get all links
# links = soup.find_all('a')
# print(links)
# for link in links: 
#     print(link.get('href'))


# -------------------------------------


# working with json 
with open(file= "sample1.json") as json_file: 
    json_data = json.load(json_file)   #<class 'dict'>
    # print(type(json_data))
    print(json_data)


print("Details for our ordered fruits")
for fruit, propty in json_data.items():
    print(f'{fruit} details: ')
    print(f"it's size is {propty['size']} and it's color is {propty['color']}")
    print('--'*10)