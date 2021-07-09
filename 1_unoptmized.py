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

def fetch(link):
    response = requests.get(link)
    with open("./output/"+link.split("/")[-1]+".html", "wb") as f:
        f.write(response.content)
    print('.',end='',flush=True)

if __name__ == '__main__':
    links = get_links()
    print(f"Total pages: {len(links)}")
    start_time = time.time()
    # This for loop will be optimized
    for link in links:
        fetch(link)

    duration = time.time() - start_time
    print(f"Downloaded {len(links)} links in {duration} seconds")
    #131 seconds