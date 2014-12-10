#This is the main script. I made it for ease of use, but users could just run their platforms' script from their designated folder if they were so inclined. 
import os
import sys
#Script Directory
DIR = os.getcwd()
#Platform script directories
WINDIR = DIR +'/WINDOWS/USBMaker_Windows.py'
MACDIR = DIR +'/MAC/USBMaker_Mac.py'
LINDIR = DIR +'/LINUX/USBMaker_Linux.py'
#Window size
#COL = Width
#ROW = Height
COL = 106
ROW = 13

# Set the Terminal window size 
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=ROW,cols=COL))

#Here we define some colors to make the text look pretty. You can find some more color codes here: 'http://tldp.org/HOWTO/Bash-Prompt-HOWTO/x329.html', or by googling "ansi color codes"
class colors:
    BLUE          = '\033[0;34m'
    GREEN         = '\033[0;32m'
    RED           = '\033[0;31m'
    MAGENTA       = '\033[0;95m'
    LMAGENTA      = '\033[1;95m'
    CYAN          = '\033[0;36m'
    WHITE         = '\033[1;37m'
    LCYAN         = '\033[1;36m'
    LGREEN        = '\033[1;32m'
    END           = '\033[0m'

url = "https://github.com/plays2/BootableUsbDriveCreator_Python/"
#This is what the menu will look like. Use this for formatting
##########################################################################################################
#										                                                                 #
#                    Welcome to the fantastical bootable USB drive creator by Plays2                     #
#              This example is written in Pyton 2.7.6 and the source code is available at:               #
#    https://github.com/plays2/BootableUsbDriveCreator_Python/If you would like to learn some python     #
#                                 To get started, please chose your platform:                            #
#										                                                                 #
#                                                A) Windows                                              #
#										         B) Mac                                                  #
#										         C) Linux                                                #
#										                                                                 #
##########################################################################################################

#Check if USBMaker has been set up
CWD = os.getcwd()
FILEPATH = CWD +"/.done.txt"
SETUP = os.path.exists(FILEPATH)
if SETUP == False:
	with open(FILEPATH, 'w') as F:
		print "Made file"
		F.write('USBMaker has been set up(:')

	pass

print colors.GREEN +"##########################################################################################################"	
print "#                                                                                                        #"	
print "#                    "+colors.WHITE +"Welcome to the fantastical bootable USB drive creator by " +colors.LGREEN +"Plays2"+colors.GREEN +"                     #"
print colors.GREEN +"#              "+colors.WHITE +"This example is written in Pyton 2.7.6 and the source code is available at:"+colors.GREEN +"               #" 
print "#"+colors.WHITE +"    "+url +  "If you would like to learn some python     "+colors.GREEN +"#"	
print "#                                 " +colors.LCYAN +"To get started, please chose your platform:                            " +colors.GREEN +"#"
print "#                                                                                                        #"
print "#                                                " +colors.MAGENTA +"A) Windows" +colors.GREEN +"                                              #"
print "#                                                " +colors.MAGENTA +"B) Mac    " +colors.GREEN +"                                              #"
print "#                                                " +colors.MAGENTA +"C) Linux  " +colors.GREEN +"                                              #"
print "#                                                                                                        #"	
print "##########################################################################################################"

PLATFORM = raw_input("Platform (A/B/C): ")

if PLATFORM in ["A", "a", "Windows", "windows"]:
	os.system("python %s" %(WINDIR))
elif PLATFORM in ["B", "b", "Mac", "mac"]:
	os.system("python %s" %(MACDIR))
elif PLATFORM in ["C", "c", "Linux", "linux"]:
	os.system("python %s" %(LINDIR))
else:
	print "Sorry, I didn't recognize that answer"

exit()