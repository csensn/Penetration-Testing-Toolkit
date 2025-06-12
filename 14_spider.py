import re
import requests
from anaconda_project.requirements_registry.network_util import urlparse

# def request(url):
#     try:
#         return requests.get("https://" + url)
#     except requests.exceptions.ConnectionError:
#         pass


target_url = "https://protoplasmic-utilit.000webhostapp.com/"
target_links = []


def extract_links(url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content.decode('utf-8'))


def crawl(url):
    href_links = extract_links(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)
        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            with open("result.txt", "a+") as file:
                file.write(str(link + "\n"))

            crawl(link)


crawl(target_url)

print("[+] All Links are Saved.")

with open("result.txt", "a+") as file:
    file.write("\n\nNew Links are stored from : " + target_url + "\n\n.....END.....\n\n")
