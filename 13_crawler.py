import requests


def request(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "vegamovies.gold"

with open("subdomain.txt", 'r') as word_list:
    for line in word_list:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered subdomains is: " + test_url)

with open("Directories_small.txt", 'r') as word_list:
    for line in word_list:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL is: " + test_url)
