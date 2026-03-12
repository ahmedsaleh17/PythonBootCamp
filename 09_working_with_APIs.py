import requests
from requests.exceptions import ConnectionError, HTTPError 
from urllib.request import urlopen

# api = 'https://www.python.org/~guido/'

"""
using request library 
response = requests.get(api)    
print(response.text)
"""


"""
using urlib.request 

with urlopen(api) as response:
    data = response.read()
    # print(data)
    string = data.decode()

    print(string)
"""


# error handling 

try: 
    
    # GET request with an accept header
    response = requests.get('http://api.music-catalog.com/lyrics', headers={'accept': 'application/json'})
    
    # enable raising exceptions for returned error statuscodes 
    response.raise_for_status()
    print(response.status_code)


# catch any connection errors
except ConnectionError as conn_err: 
    print(f"connection error {conn_err}")

except HTTPError as http_err:
    print(f"HTTP error {http_err}")