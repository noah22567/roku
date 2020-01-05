import requests
import roku as Roku

COMMANDS = {
    # Standard Keys
    'home': 'Home',
    'reverse': 'Rev',
    'forward': 'Fwd',
    'play': 'Play',
    'select': 'Select',
    'left': 'Left',
    'right': 'Right',
    'down': 'Down',
    'up': 'Up',
    'back': 'Back',
    'replay': 'InstantReplay',
    'info': 'Info',
    'backspace': 'Backspace',
    'search': 'Search',
    'enter': 'Enter',
    'literal': 'Lit',

    # For devices that support "Find Remote"
    'find_remote': 'FindRemote',

    # For Roku TV
    'volume_down': 'VolumeDown',
    'volume_up': 'VolumeUp',
    'volume_mute': 'VolumeMute',

    # For Roku TV while on TV tuner channel
    'channel_up': 'ChannelUp',
    'channel_down': 'ChannelDown',

    # For Roku TV current input
    'input_tuner': 'InputTuner',
    'input_hdmi1': 'InputHDMI1',
    'input_hdmi2': 'InputHDMI2',
    'input_hdmi3': 'InputHDMI3',
    'input_hdmi4': 'InputHDMI4',
    'input_av1': 'InputAV1',

    # For devices that support being turned on/off
    'power': 'Power',
    'poweroff': 'PowerOff',
    'poweron': 'PowerOn',
}

def post_command(ip,command_name):
    ses = requests.Session()
    ses.post('http://{ip}:8060/keypress/{com}'.format(ip=ip,com =COMMANDS[command_name]))

# post_command('10.0.0.164','select')
def get_app(app_name,ip):
    for app in roku.apps:
        if app_name in str(app.name).lower():
            return app.id

def launch(ip):
    # id = get_app(app_name,)
    ses = requests.Session()
    ses.post('http://{ip}:8060/launch/837'.format(ip=ip))

import xml.etree.ElementTree as ET

url = 'http://10.0.0.164:8060/query/apps'
ses = requests.Session()
response = ses.get(url)
print(ET.iselement(response))
# print()

url = 'http://10.0.0.164:8060/query/active-app'
print(ses.get(url))

import socket
from http.client import HTTPResponse
from io import BytesIO


class _FakeSocket(BytesIO):
    def makefile(self, *args, **kw):
        return self

def discover(timeout=3, retries=2):

    group = ('239.255.255.250', 1900)

    m = '\r\n'.join([
        'M-SEARCH * HTTP/1.1',
        'HOST: {0}:{1}'.format(*group),
        'MAN: "ssdp:discover"',
        'ST: "roku:ecp"', 'MX: 3', '', ''])

    socket.setdefaulttimeout(timeout)

    responses = {}

    for _ in range(retries):
        sock = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

        sock.sendto(m.encode(), group)

        while 1:
            try:
                rhttp = HTTPResponse(_FakeSocket(sock.recv(1024)))
                rhttp.begin()
                if rhttp.status == 200:
                    responses = rhttp.getheader('location')

            except socket.timeout:
                break

    return responses



print(discover())