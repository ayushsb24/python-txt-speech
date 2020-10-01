# Importing Modules
import pyttsx3

happy = pyttsx3.init()

# Path
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

#sets Rates
happy.setProperty('rate', 150) 

# Input
txt=input("Enter Text to Speak: ")

# Use female voice[0]
# Use male voice [1]
happy.setProperty('voice', voice_id) 
happy.say(txt)
happy.say("")

# Helps to speak
happy.runAndWait()




