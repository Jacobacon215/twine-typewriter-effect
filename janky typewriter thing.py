# imports libraries
from tkinter import Tk

# sets up tkinter thingy (needed for clipboard manipulation)
r = Tk()

# establishes base string bullshit
#   establishes temporary string variable
tempStr = ""
#   establishes base string variable
baseStr = ""
#   time for some bullshit
#       gives instructions
print("type zqga as a separate line when finished")
#       does bullshit
while tempStr != "zqga":
	tempStr = input("line: ")
	if tempStr != "zqga":
		baseStr = baseStr + tempStr + "%gyq"
baseStr = baseStr.replace("%gyq", '''
''')



# counts number of characters in base string
charCount = int(len(baseStr))-1

# establishes secondary character count variable
currentChar = 0

# establishes delay amount, offset time amount, and time variable
delayTime = input("Time delay between characters (in seconds): ")
if delayTime == "":# this makes the default delay time zero
    delayTime = float(0)
else:
    delayTime = float(delayTime)
offsetTime = input("Time offset (how much time before the characters start appearing): ")
if offsetTime == "":# this makes the default offset time 0
    offsetTime = float(0)
else:
    offsetTime = float(offsetTime)
timeVar = str((currentChar * delayTime)+offsetTime)+"s"

# establishes the variable that the final string is going to be in
finalStr = ""

# does the thing with the thing
while currentChar <= charCount:
    # this part assembles each character's (event:) function. first, it adds the start of the event macro (for this situation) to the end of the finalStr variable (which will be what the output is). it then adds the necessary amount of time (the previous amount of delay + 1 unit of delay) to the event macro. it then closes the macro, opens an attatched hook, adds the appropriate character, and closes the hook.
    finalStr = finalStr + "(event: when time > "+timeVar+")["+baseStr[currentChar]+"]"

    # adds 1 to the "current character" variable
    currentChar = currentChar + 1

    # sets the appropriate delay time for the next character
    timeVar = str((currentChar * delayTime)+offsetTime)+"s"

# some tkinter stuff i don't understand
r.withdraw()
r.clipboard_clear()

# puts final string on clipboard
r.clipboard_append(finalStr)

# makes the string stay on the clipboard after the python window is closed
r.update()

# i don't know what this one does but the guy on stackoverflow said to do it
r.destroy()

# displays final string
input(finalStr + '''
''' + timeVar)