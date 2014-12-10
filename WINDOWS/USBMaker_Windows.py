###TODO: 
#Sorry if I over-comment this, just like to explain for those that want to learn from my code
#Also install gentoo
import getpass
import os
import sys
import time
import urllib
import zipfile

print "Begin windows script"
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
print "#"+colors.WHITE +"    "+url +  " If you would like to learn some python    "+colors.GREEN +"#"	
print "#										                         #"	
print "##########################################################################################################"

#Here we make sure the user is ready to go
go = raw_input('\n' +"When you're ready to get started, press enter: ");
#first we set up some directories
#This is the location of the script
WKDIR = os.getcwd()
#This is the directory of the dd binary
DDDIR = WKDIR +"/WINDOWS/bin/dd.exe"
#This is a boolean which will be true if the dd binary exists
DDEXISTS = os.path.exists(DDDIR)
#If directories/dd doesn't exist, we need to make them
if DDEXISTS == False:
	CONT1 = raw_input("You're missing the windows DD binary. Would you like to download it now? (Y/N): ")
	if CONT1 in ["Y", "y"]:
		#Download the zip archive from chrysocome's server
		DDURL = "http://www.chrysocome.net/downloads/dd-0.6beta3.zip"
		DDZIPDIR = WKDIR +"/WINDOWS/bin/dd-0.6beta3.zip"
		urllib.urlretrieve(DDURL,DDZIPDIR)
		#time.sleep(3)
		#extract the contents of the archive
		DDEXCTRACTDIR = WKDIR +"/WINDOWS/bin/"
		with zipfile.ZipFile(DDZIPDIR, "r") as z: 
			z.extractall(DDEXCTRACTDIR)
		#Delete the old archive
		os.remove(DDZIPDIR)

	elif CONT1 in ["N", "n"]:
		print "Please download the dd binary from 'http://www.chrysocome.net/downloads/dd-0.6beta3.zip' and place it in the WINDOWS/bin/ directory named 'dd.exe' and run the script again"
		exit()
	else:
		print "Invalid answer"
		exit()
	

#Add the file name to the end of the directory
OUTDIRIMG = OUTDIR +"Out.img"	
IMGDIRIMG = IMGDIR +"Img.img"
#user is ready, now let's set up some information.
#Now we need the path of the iso to copy to USB. 
print colors.CYAN +"First, I need the path to your"+colors.MAGENTA +" target ISO." +colors.CYAN
PATH = raw_input("Drag your " +colors.MAGENTA +"target iso " +colors.CYAN +"into the terminal window." +'\n' +colors.WHITE +"Tip: Make sure the path looks something like '/Users/*your username*/Path/To/iso' and not '~/Path/To/iso' " +'\n' +colors.LCYAN +"Path:" );
#Now we have to convert the ISO image to an IMG. This is a mac thing and will have to be done differently on linux and windows (Eventually)
#########          #Arguments############# #img output dir#####   #Source iso dir
hdiutil = 'hdiutil convert -format UDRW -o %s %s' %(IMGDIRIMG, PATH) 
print colors.MAGENTA +"Next I need to convert your ISO into an IMG"
print "This part will ask you for your sudo password, just enter it and let it do it's thing"
print "Also, this part could take a while depending on the size of the iso" +colors.END
os.system('sudo -S %s' %(hdiutil))
#If you haven't noticed by now, for some shitty reason Mac OS likes to add a '.dmg' to the end of the img. Which is horse shit if I do say so myself.
#Anyways we need to move it to the 'Out' directory without the .dmg extension.
BEFORE = IMGDIRIMG +'.dmg'
os.system('mv %s %s' %(BEFORE, OUTDIRIMG))
	#Now for the fun part. We need to get the ID of the users USB drive, and then unmount it, and then put the iso on it.
#First we will show a list of available drives for the user. The user will ten give us the name of said drive.
print "Now for the fun part. I will show a list of available usb drives. You just need to tell me which one is yours(:"
print "The best way to do this is first unplug your device and press enter. After, you will plug your usb drive back in"
print "and tell me which one showed up the second time, but not the first(:"
#We listen for raw input here just for the enter press. Not sure if there is a better way to do this, but it works for now.
ENTER = raw_input("Unplug your flash drive and press enter: ");
os.system('diskutil list')
ENTER2 = raw_input("Now plug your flash drive back in an press enter: ")
os.system('diskutil list')
USBID = raw_input("Now type the name of your flash drive on which you want to copy the iso" +'\n' +"Don't forget that the drive you chose will be formatted, so make sure you chose the right one!" +'\n' +"Tip: Your drive id looks something like 'disk2' and is located in the far-right column. Don't include the trailing numbers! ie: 's1' or 's2'")
#now we need to unmount the disk and transfer the img
	#Make the USBID usable for the unmount command (add /dev/ to the beginning)
USBIDUSABLE = "/dev/" +USBID
#Now unmount the disk
os.system('diskutil unmountDisk %s' %(USBIDUSABLE))
	#And finally, we copy the image to the Flash drive
#OUTDIRIMG is the img we want to use
#OUTUSBID  is the usb we want to use
OUTUSBID = "/dev/r" +USBID
#We add the r in the hopes of reducing wait time
os.system('sudo dd if=%s of=%s bs=1m' %(OUTDIRIMG, OUTUSBID))
exit();