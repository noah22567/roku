import json
import socket
from companion.packages.utils import  message_to_json, handle_response, execute_command
from companion.packages.srcommand import myCommand
# from packages.mongo_requests import get_all_devices

def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 8090)
    isOnline = False
    active_device = "None"
    device_list = [{"tv":"10.0.0.164"}]
    # sock.connect(server_address)
    while True:
        command = myCommand().lower()+' '+active_device
        # command = input('type command')
        message = {"command": command}
        if 'go offline' in message['command']:
            isOnline=False
            print("Closing socket")
            sock.close()
        elif 'go online' in message['command'] and not isOnline:
            isOnline=True
            print("Going online")
            sock.connect(server_address)
        elif "activate" in message['command']:
            for device in device_list:
                for key in device.keys():
                    if key in message['command']:
                        print("Activating {}".format(key))
                        active_device = device[key]

        elif "deactivate" in message['command']:
            print("Deactivating")
            active_device = None


        elif isOnline:
            retries = 0
            request = json.dumps(message_to_json(message)).encode('utf-8')
            sock.sendall(request)
            response_from_server = handle_response(sock) #waits for response
            if response_from_server:
                command = message_to_json(response_from_server)
                while True:
                    try:
                        execute_command(command)
                        break
                    except:
                        if retries > 3:
                            retries+=1
                            break
            else:
                print("something went wrong client side")
        else:
            print("another go around the world")
            continue

if __name__=="__main__":
    client()