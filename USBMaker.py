###TODO: 38
#Sorry if I over-comment this, just like to explain for those that want to learn from my code
#Also install gentoo
import getpass
import os

#In case my URL canges, I keep a variable up here for easy access
url = "https://github.com/plays2/BootableUsbDriveCreator_Python/"

#Here we define some colors to make the text look pretty. You can find some more color codes here: 'http://tldp.org/HOWTO/Bash-Prompt-HOWTO/x329.html', or by googling "ansi color codes"
class colors:
    BLUE    = '\033[0;34m'
    GREEN   = '\033[0;32m'
    RED     = '\033[0;31m'
    MAGENTA = '\033[0;95m'
    CYAN    = '\033[0;36m'
    WHITE   = '\033[1;37m'
    LCYAN   = '\033[1;36m'
    LGREEN  = '\033[1;32m'
    END     = '\033[0m'

#Un-comment this if you want to see what the colors look like. I left it In just in case you want to test the colors like I did. 
#Make sure when you're done using a color and you want to return to the default color, you add '+colors.END'
#If you aren't returning to normal colors, adding 'colors.END' isn't necessary
#Also make sure you use 'colors.END at the end of your script. If you don't the user's terminal will be stuck in the color you left it in.
#==========================================#
#                                          #
#    print colors.BLUE +"BLUE"			   #
#    print colors.GREEN +"GREEN"           #
#    print colors.RED +"RED"               #
#    print colors.MAGENTA +"MAGENTA"       #
#    print colors.CYAN +"CYAN"             #
#    print colors.WHITE +"WHITE"           #
#    print colors.LCYAN +"LIGHT CYAN"      #
#    print colors.LGREEN +"LIGHT GREEN"    #
#                                          #
#==========================================#

#TODO: Make the main menu prettier
#Here we start the actual program.
print colors.GREEN +"Welcome to the fantastical bootable USB drive creator by " +colors.LGREEN +"Plays2" +colors.END;
print colors.CYAN +'\n' +"This example is written in Pyton 2.7.6 and the source code is available at: " + url + " If you would like to learn some python(:"+ colors.END;

#Here we make sure the user is ready to go(:
go = raw_input('\n' +"When you're ready to get started, type 'go' and press enter: ");
if go in ["go", "Go"]:
	#first we set up some directories
	#This is the location of the script
	WKDIR = os.getcwd()
	#This is where the converted .img.dmg will go
	OUTDIR = WKDIR +"/Out/"
	#This is where the fixed .img will go //I'll change this soon
	IMGDIR = WKDIR +"/IMG/"
	#These are some booleans to see if the paths already exist
	IMGPATHEXISTS = os.path.exists(IMGDIR)
	OUTPATHEXISTS = os.path.exists(OUTDIR)

	#If these directories don't exist, we need to make them
	if IMGPATHEXISTS == False:
		print "Setting up img directory..."
		#Make the directory
		os.system('mkdir %s' %(IMGDIR))		

	if OUTPATHEXISTS == False:
		print "Setting up out directory..."
		#Make the directory
		os.system('mkdir %s' %(OUTDIR))

	#Add the file name to the end of the directory
	OUTDIRIMG = OUTDIR +"Out.img"	
	IMGDIRIMG = IMGDIR +"Img.img"
	#user is ready, now let's set up some information.
	#Now we need the path of the iso to copy to USB. 
	print colors.LCYAN +"Next, I need the path to your target ISO."
	PATH = raw_input("Drag your target iso into the terminal window." +'\n' +"Tip: Make sure the path looks something like '/Users/*your username*/Path/To/iso' and not '~/Path/To/iso' " +'\n' +"Path:");
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