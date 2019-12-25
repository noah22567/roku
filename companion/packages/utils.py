import requests
import json
from companion.packages.mongo_requests import get_device, get_command
import time

def message_to_json(msg):#both
    if type(msg) == bytes:
        msg = msg.decode('utf-8')
        msg = msg.replace("'",'"')
    elif type(msg) == dict:
        msg = json.dumps(msg, sort_keys=True)
    elif type(msg) == str:
        msg = msg.replace("'",'"')
    msg = json.loads(msg)
    return msg

def gen_response(data):#server tool
    try:
        res = {"status": 200, "message" : "Received", "command": data[0],"device_ip":data[1],"device_port":data[2]} #data will be a list containing endpoints method etc.
        res = json.dumps(res).encode('utf-8')
    except:
        res = {"status": "502", "message": "Incorrect format"}

    return res

def handle_response(sock):
    # start_time = time.time()
    print("waiting for response")
    data = sock.recv(1024)
    # while True:
    if len(data) > 10:
        data = message_to_json(data)# going to need a thread for timer incase of timed out
        print("Response from server: ", data)
        if data['status']:
            if data['status'] == 200:
                if 'command' in data.keys():
                    return data['command']
                else:
                    return True
            elif data['status'] == 422:#incorrect format
                return False
            elif data['status'] == 408:#timed out
                    return False
            elif data['status'] == 500:#internal error
                    return False

    # elif time.time()-start_time > 1:
    #     return "TimedOut"
    else:
        return False
        # return "IncorrectResponse"

def handle_command(data,client_ip):#server
    try:
        msg = message_to_json(data)
        command_msg = msg['command']
        print(command_msg,"message in handle")
        print("Searching for devices under client_ip: {}".format(client_ip[0]))
        command_split = command_msg.split(" ")
        print(command_split,"command split")
        got_device = get_device(command_split,client_ip[0])
        print(got_device)
        device_model = got_device[0]
        device_ip = got_device[1]
        device_port = got_device[2]

        print("here are the device model, ip, and port: ", device_model,device_ip,device_port)
        if device_ip != False:
            return [get_command(command_split,device_model),device_ip,device_port]
    except ValueError:
        return ValueError.__name__
    except IndexError:
        return IndexError.__name__
    except SyntaxError: #add except for incorrect format from line 65 and return the error
        return SyntaxError.__name__
    except:
        return "InternalError"

def execute_command(command,device_ip):#client

    print("Executing command")
    print(command)
    req = requests.Session()
    def send_command(**kwargs):

        if kwargs['method'].lower() == 'get':
            req = Request('GET', kwargs['command']['device_ip']+kwargs['command']['url'])


        elif kwargs['method'].lower() == 'post':
            req = Request('post', kwargs['command']['device_ip']+kwargs['command']['url'], data=body)



    for step in command:
        send_command(**step)