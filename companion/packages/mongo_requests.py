from pymongo import MongoClient

# client = MongoClient("mongodb+srv://admin:password2256@cluster0-mpvdy.mongodb.net/test?retryWrites=true&w=majority")
def get_device(command_split, client_ip):  # recieves split command
    port = 27017
    ip = 'localhost'
    client = MongoClient(ip, port)
    db = client['companion']
    client_devices = db['client_devices']
    try:
        match_list = []
        for word in command_split:
            for match in client_devices.find({"client_ip": client_ip}):
                for device in match['supported_devices']:
                    for key in device:
                        if word in device[key]:
                            match_list.append([len(word), device['device_model'], device['device_ip'], device['device_port']])
        return sorted(match_list, key=lambda x: x[0])[-1][1:4]

    except:
        return IndexError


def get_command(command_split, device_model):
    try:
        port = 27017
        ip = 'localhost'
        client = MongoClient(ip, port)
        db = client['companion']
        device_endpoints = db['device_endpoints']

        match_list = []
        count_match = []
        for device in device_endpoints.find({"device_model": device_model}):
            for word in command_split:
                for command in device['commands'].keys():
                    if word in command:
                        match_list.append(device['commands'][command])
        for match in match_list:
            count_match.append(match_list.count(match))
        return match_list[count_match.index(max(count_match))]
    except ValueError:
        raise ValueError()


def get_all_devices(client_ip):  # recieves split command
    port = 27017
    ip = 'localhost'
    client = MongoClient(ip, port)
    db = client['companion']
    client_devices = db['client_devices']
    try:
        match_list = []
        for match in client_devices.find({"client_ip": client_ip}):
            for device in match['supported_devices']:
                for key in device:
                    if word in device[key]:
                        match_list.append([len(word), device['device_model'],
                                           device['device_ip'], device['device_port'],device['device_name']])
        return sorted(match_list, key=lambda x: x[0])[-1][1:4]

    except:
        return IndexError




