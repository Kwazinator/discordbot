import RobotSlave
import datetime

######################################START DEF METHODS##############################################
# for transparency, variables saved to files since program might restart often
def igiveup():
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


def commands():
    message = 'Commands: '
    for key in triggers.keys():
        message += key + ' '
    return message


def help():
    return "!igiveup: provides a solution to the daily Robot Reboot Challenge !help: provides this wonderful text !reminder: dont do nuffing yet"


def reminder():
    return "reminder.txt for specific people maybe set timers? and it will @them reminding them like an alarmclock"
######################################END DEF METHODS#################################################


#add the "msgtotrigger": (function returning message to send), dont forget the comma!
def GetTrigger():
    triggers = {
        "!igiveup": igiveup(),
        "!help": help(),
        "!reminder": reminder(),
        "!commands": commands()
    }
    return triggers

#####################################install additional modules#####################################
#example using pip (run once then append at top for import module-name)
#subprocess.call("#!~/Desktop/GITHUB/DiscordBot/Mainfiles/venv/Scripts \n pip install module-name", shell=true)
#
####################################################################################################
