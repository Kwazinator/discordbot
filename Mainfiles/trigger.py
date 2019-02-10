import RobotSlave
import datetime
import subprocess
import SYNFlooder
from google_images_download import google_images_download

######################################START DEF METHODS##############################################
# for transparency, variables saved to files since program might restart often
def igiveup(channel, message, sender):
    with open('dayandhasconfig.txt', 'r') as file:
        data = file.read()
    if data < str(datetime.datetime.now().day) and datetime.datetime.now().hour >= 15:
        answer = RobotSlave.solve()
        with open('robitsanswers.txt', 'w') as file:
            file.write(answer)
        with open('dayandhasconfig.txt', 'w') as file:
            file.write(str(datetime.datetime.now().day))
    else:
        with open('robitsanswers.txt', 'r') as myfile:
            answer = myfile.read()
    return answer

def whoami(channel, message, sender):
    return "You are you."

def whoamireally(channel, message, sender):
    return "I am he, as you are he, as you are me and we are all together."

def shellcommands(channel, message, sender):
    # try catch block with subprocess in it. XD
    return "comming soon"

def test(channel, message, sender):
    return channel + ' ' + message + ' ' + sender

def google(channel, message, sender):

    response = google_images_download.googleimagesdownload()

    arguments = {"keywords":"Polar bears","limit":20,"print_urls":True}
    paths = response.download(arguments)
    print(paths)

    return ""



def help(channel, message, sender):
    return "!igiveup: provides a solution to the daily Robot Reboot Challenge !help: provides this wonderful text !reminder: dont do nuffing yet"

def ddos(channel, message, sender):
    if sender == 'chan2#2445':
        message = message[6:]
        try:
            if message == '--help':
                return 'format: !ddos x.x.x.x PortNum NumPackets'
            else:
                message = message.split(' ')
                ip = message[0]
                port = message[1]
                numpack = message[2]
                result = SYNFlooder.main(ip, int(port), int(numpack))
                return result
        except:
            return 'Error occured: please use format !ddos x.x.x.x PortNum NumPackets'
        finally:
            pass
    else:
        return 'You do not have permission to run this command'
         


def celeste(channel, message, sender):
    return message[9:]

def reminder(channel, message, sender):
    return "reminder.txt for specific people maybe set timers? and it will @them reminding them like an alarmclock"
######################################END DEF METHODS#################################################


#add the "msgtotrigger": (function returning message to send), dont forget the comma!
def GetTrigger(channel, message, sender):
    triggers = {
        "!igiveup": igiveup(channel, message, sender),
        "!help": help(channel, message, sender),
        "!reminder": reminder(channel, message, sender),
        "!whoami": whoami(channel, message, sender),
        "!whoamireally": whoamireally(channel, message, sender),
        "!shellcommands": shellcommands(channel, message, sender),
        "!test": test(channel, message, sender),
        "!celeste": celeste(channel, message, sender),
        "!ddos": ddos(channel, message, sender),
        "!google": google(channel, message, sender)
    }
    return triggers

#####################################install additional modules#####################################
#example using pip (run once then append at top for import module-name)
#subprocess.call("#!~/Desktop/GITHUB/DiscordBot/Mainfiles/venv/Scripts \n pip install module-name", shell=true)
#
####################################################################################################
