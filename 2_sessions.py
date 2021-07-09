import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

def get_links():
    curr_list = 'https://en.wikipedia.org/wiki/List_of_circulating_currencies'
    all_links = []
    response = requests.get(curr_list)
    soup = BeautifulSoup(response.text, "lxml")
    curr_el = soup.select('p+table td:nth-child(2) > a, p+table td:nth-child(1) > a:nth-child(1)')
    for link_el in curr_el:
        link = link_el.get("href")
        link = urljoin(curr_list, link)
        all_links.append(link)
    return all_links

def fetch(link,s):
    response = s.get(link)
    file_name="./output/"+link.split("/")[-1]+".html"
    with open(file_name, "wb") as f:
        f.write(response.content)
    print('.',end='',flush=True)

if __name__ == '__main__':
    
    links = get_links()
    print(f"Total pages: {len(links)}")
    start_time = time.time()
    # Sessions
    s = requests.Session()
    for link in links:
        fetch(link,s)

    duration = time.time() - start_time
    print(f"\nDownloaded {len(links)} links in {duration} seconds")
    #28 seconds