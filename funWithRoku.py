from roku import Roku
import time




ip = "10.0.0.164"
# ip = Roku.discover()
# ip = str(ip[0]).split(':')[1].replace(' ',"")
roku = Roku(ip)

# print(str(Roku.discover()[0]).split(':')[1].replace(' ', ""))

hulu = False
netflix = False

def next_episode():
    if hulu:
        roku.down()
        time.sleep(1)
        roku.play()
        # roku.enter()

hulu = True

tv = True


def pause():
    if tv:
        roku.select()

def play():
    if tv:
        roku.play()
# play()
# next_episode()
# pause()
# roku.down()
# roku.up()
# roku.select()
print(roku.commands)

def volume(pos,num):
    if pos == 'up':
        if num == 0:
            roku.volume_up()
    elif pos == 'up':
        if num == 0:
            roku.volume_down()

    elif pos == 'mute' or pos == 'unmute':
        roku.volume_mute()

    for n in range(0,num):
        if pos == 'up':
            roku.volume_up()
        elif pos == 'down':
            roku.volume_down()
#
# volume('down',2)



# print(roku.apps[0].name)
def open_app(app_name):
    for app in roku.apps:
        if app_name in str(app.name).lower():
            print(app.id)
            roku[app.name].launch()


# roku.poweron()
open_app('youtube')
# roku.select()
# roku.play()