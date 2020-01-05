import json
import socket
from companion.packages.utils import  message_to_json, handle_response, execute_command
from companion.packages.srcommand import myCommand
# from packages.mongo_requests import get_all_devices

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 8350)
    isOnline = False
    while True:
        try:
            sock.connect(server_address)
            #record command
            if not isOnline:
                continue

            elif isOnline:
                #def command prep
                    #check what devices are active by ip
                    #check what apps are active on device
                    #check if relevant to command
                #def send command and relevant info
                    #if 200 response break
                    #else retry twice unless syntax
                #def receive command from server







        except:
            continue
