from pymongo import MongoClient

command = ['change', 'power']
ip = "127.0.0.1"

def get_device(command_split,client_ip):#recieves split command
    port = 27017
    ip = 'localhost'
    client = MongoClient(ip,port)
    db = client['companion']
    client_devices = db['client_devices']
    # try:
    match_list = []
    for word in command_split:
        for match in client_devices.find({"client_ip":client_ip}):
            for device in match['supported_devices']:
                for key in device:
                    if word in device[key]:
                        print(device['device_port'])
                        match_list.append([len(word),device['device_model'],device['device_ip'],device['device_port']])
    # print(sorted(match_list, key=lambda x: x[0]))
    return sorted(match_list, key=lambda x: x[0])[-1][1:4]

    # except:
    #     return (False,False)
    
    
print(get_device(command,ip))
