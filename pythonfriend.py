import pyttsx3
happy = pyttsx3.init()

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
#sets Rates
happy.setProperty('rate', 150) 

txt=input("Enter Text : ")
# Use female voice 
happy.setProperty('voice', voice_id) 
happy.say(txt)
happy.say("")


happy.runAndWait()




