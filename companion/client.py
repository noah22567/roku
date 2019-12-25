import json
import socket
from companion.packages.utils import  message_to_json, handle_response, execute_command
from companion.packages.srcommand import myCommand

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 8350)
    isOnline = True
    sock.connect(server_address)
    while True:
        command = myCommand().lower()
        # command = input('type command')
        message = {"command": command}
        if 'go offline' in message['command']:
                isOnline=False
                print("closing socket")
                sock.close()
        elif 'go online' in message['command']:
                isOnline=True
                print("going online")
                sock.connect(server_address)

        elif isOnline:
            request = json.dumps(message_to_json(message)).encode('utf-8')
            retries = 0
            sock.sendall(request)
            while True:
                response_from_server = handle_response(sock) #waits for response
                if not response_from_server:
                    break
                if response_from_server:
                   try:
                        retries+=1
                        command = message_to_json(response_from_server)['commnad']
                        execute_command(command)
                   except:
                       if retries == 2:
                           break
        else:
            print("another go around the world")
            continue

if __name__=="__main__":
    client()