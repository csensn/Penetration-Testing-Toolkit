import requests

target_url = "http://192.68.48.138"
data_dic = {"username":"admin","password":""}
response = requests.post(target_url, data=data_dic)
print(response.content)
