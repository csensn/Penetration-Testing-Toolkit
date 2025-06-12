import requests

def download(url):
    get_responce = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_responce.content)

download("https://github.com/AlessandroZ/LaZagne/releases/download/v2.4.5/LaZagne.exe")