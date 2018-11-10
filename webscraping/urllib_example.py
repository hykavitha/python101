import urllib.request
import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlparse

#log
def logging(msg_type, url, msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(msg_type +"\t"+ timestamp  +"\t"+  url  +"\t"+  msg)

#child clas
def parser(response):
    logging("\tDATA_PARSER", url, "tags")
    content = response.read()
    soup = BeautifulSoup(content)
    tags = soup('a')
    logging("\tDATA_TAGS", url, "tags")


    for tag in tags:
        href = tag.get("href")
        if href is not None and 'https' in href:
            logging("\tURLS", url, href)
        else:
            pass
            #logging("\tURLS", url, urlparse(url).netloc + href)


#base clas

def response_processing(response):
    mime_type = response.getheader('Content-Type')
    url = response.geturl()

    if "text/html" in mime_type:
        logging("\tDATA_EXTRACTION", url, "text/html")
        parser(response)

#hi kavitha

#base clas
def fetch(url):
    response = urllib.request.urlopen(url)


    if response.code in [200,201, 202, 203,204, 205, 206]:
        logging("RECORD", url, "Success")
        response_processing(response)
    elif response.code in [400, 401, 402, 403, 404,405, 406]:
        logging("ERROR", url, "page error")

    elif response.code in [500, 501,502, 503,504, 505 ]:
        logging("ERROR", url, "server errors")
    else:
        logging("ERROR", url, "unknown")



#196
#take sys args
#if the deoth is 0,1 or ...? depth_limit
#print it out
#crawling - > use taht crawler class functions
url = 'https://timesofindia.indiatimes.com/'
fetch(url)