###TODO: 
#Sorry if I over-comment this, just like to explain for those that want to learn from my code
#Also install gentoo
import getpass
import os
import sys
import time

print "Begin linux script"
time.sleep(1)
os.system("clear")

#make a cool spinning loading thing :D (might be removed later)
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()
#change this nmber to adjust how long the spinner will spin
for _ in range(10):
    sys.stdout.write(spinner.next())
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')

#In case my URL canges, I keep a variable up here for easy access
url = "https://github.com/plays2/BootableUsbDriveCreator_Python/"

#Here we define some colors to make the text look pretty. You can find some more color codes here: 'http://tldp.org/HOWTO/Bash-Prompt-HOWTO/x329.html', or by googling "ansi color codes"
class colors:
    BLUE    = '\033[0;34m'
    GREEN   = '\033[0;32m'
    RED     = '\033[0;31m'
    MAGENTA = '\033[0;95m'
    LMAGENTA = '\033[1;95m'
    CYAN    = '\033[0;36m'
    WHITE   = '\033[1;37m'
    LCYAN   = '\033[1;36m'
    LGREEN  = '\033[1;32m'
    END     = '\033[0m'

#Make sure when you're done using a color and you want to return to the default color, you add '+colors.END'
#If you aren't returning to normal colors, adding 'colors.END' isn't necessary
#Also make sure you use 'colors.END at the end of your script. If you don't the user's terminal will be stuck in the color you left it in.

#This is what the menu will look like. Use this for formatting
##########################################################################################################
#										                                                                 #
#                    Welcome to the fantastical bootable USB drive creator by Plays2                     #
#              This example is written in Pyton 2.7.6 and the source code is available at:               #
#    https://github.com/plays2/BootableUsbDriveCreator_Python/If you would like to learn some python     #
#										                                                                 #
##########################################################################################################

print colors.GREEN +"##########################################################################################################"	
print "#										                         #"	
print "#                    "+colors.WHITE +"Welcome to the fantastical bootable USB drive creator by " +colors.LGREEN +"Plays2"+colors.GREEN +"                     #"
print colors.GREEN +"#              "+colors.WHITE +"This example is written in Pyton 2.7.6 and the source code is available at:"+colors.GREEN +"               #" 
print "#"+colors.WHITE +"    "+url +  "If you would like to learn some python     "+colors.GREEN +"#"	
print "#										                         #"	
print "##########################################################################################################"

#Here we make sure the user is ready to go
go = raw_input('\n' +"When you're ready to get started, press enter: ");

#user is ready, now let's set up some information.
#Now we need the path of the iso to copy to USB. 
print colors.CYAN +"First, I need the path to your"+colors.MAGENTA +" target ISO." +colors.CYAN
PATH = raw_input("Drag your " +colors.MAGENTA +"target iso " +colors.CYAN +"into the terminal window." +'\n' +colors.WHITE +"Tip: Make sure the path looks something like '/Users/*your username*/Path/To/iso' and not '~/Path/To/iso' " +'\n' +colors.LCYAN +"Path:" );
print "Now for the fun part. I will show a list of available usb drives. You just need to tell me which one is yours(:"
print "The best way to do this is first unplug your device and press enter. After, you will plug your usb drive back in"
print "and tell me which one showed up the second time, but not the first(:"
#We listen for raw input here just for the enter press. Not sure if there is a better way to do this, but it works for now.
ENTER = raw_input("Unplug your flash drive and press enter: ");
os.system('sudo -S ls -l /dev/disk/by-id/*usb*')
ENTER2 = raw_input("Now plug your flash drive back in an press enter: ")
os.system('sudo -S ls -l /dev/disk/by-id/*usb*')
USBID = raw_input("Now type the name of your flash drive on which you want to copy the iso" +'\n' +"Don't forget that the drive you chose will be formatted, so make sure you chose the right one!" +'\n' +"Tip: Your drive id looks something like 'disk2' and is located in the far-right column. Don't include the trailing numbers! ie: 's1' or 's2'")

#And finally, we copy the image to the Flash drive
#OUTDIRIMG is the img we want to use
#OUTUSBID  is the usb we want to use

#We add the r in the hopes of reducing wait time
os.system('sudo dd if=%s of=%s bs=1M' %(PATH, USBID))

exit();
