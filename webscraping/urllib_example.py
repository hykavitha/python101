import urllib.request
import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def logging(msg_type, url, msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(msg_type, timestamp, url, msg)

def parser(response):
    logging("\tDATA_PARSER", url, "tags")
    content = response.read()
    soup = BeautifulSoup(content)
    tags = soup('a')
    print(tags)
    logging("\tDATA_TAGS", url, "tags")


    for tag in tags:
        href = tag.get("href")
        if 'https' in href:
            logging("\tURLS", url, href)
        else:
            logging("\tURLS", url, urlparse(url).netloc + href)



def data_processing(response):
    mime_type = response.getheader('Content-Type')
    url = response.geturl()

    if "text/html" in mime_type:
        logging("\tDATA_EXTRACTION", url, "text/html")
        parser(response)



def fetch(url):
    response = urllib.request.urlopen(url)


    if response.code in [200,201, 202, 203,204, 205, 206]:
        logging("RECORD", url, "Success")
        data_processing(response)
    elif response.code in [400, 401, 402, 403, 404,405, 406]:
        logging("ERROR", url, "page error")

    elif response.code in [500, 501,502, 503,504, 505 ]:
        logging("ERROR", url, "server errors")
    else:
        logging("ERROR", url, "unknown")



#196
url = 'https://www.python.org/dev/peps/pep-0257/'
fetch(url)