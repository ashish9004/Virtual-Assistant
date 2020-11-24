import pyttsx3 #install
import datetime
import speech_recognition as sr #install
import webbrowser 
import wikipedia
import os # for path selection 
#import pyaudio and install pyaudio whl file  if u get error pyaudio, install file as per ur python ver. 
import smtplib # for email send
import pyautogui # install for take control mouse and keyboard.
import psutil # use for check sysytem prosses like cpu, battery utilization ect.
import pyjokes 



engine=pyttsx3.init('sapi5') # sapi5 is speak recon with winddow app
vioces= engine.getProperty('voices')







engine.setProperty('voices',vioces[0].id) #0 male or 1 female voice define

#print(vioces[0].id)
#2
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#3
                                        #
def wishme():
    
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello Ashish, I am your personal assistant!, Please tell me how may i help you, ")

def takecommand():
    #take microphone input from the user and return string output

    r=sr.Recognizer()
    with sr.Microphone() as source:

        print("Listining....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing....")
        message=r.recognize_google(audio,language='en-in')
        print(f"User Said:{message}\n")

    except Exception as e:
       # print(e)
        print("Pardan, Please say that again...")
        return "None " #if any prblm then take return non
    return message

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save('C:\\Users\\ashish\\Desktop\\AI_PYTHON_PROJECT/screenshot.png')

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at "+usage)

    # bettery=psutil.sensors_battery()
    # speak("battery is at")
    # speak(battery.percent)

def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])
    
#1
if __name__ == "__main__":

    wishme()
    #takecommand()

    while True:
        message=takecommand().lower() #all message cmd take lowercase

        #logic for exicuting task based on message

        if 'open youtube' in message:
            webbrowser.open("youtube.com")

        elif 'open google' in message:
            webbrowser.open("google.com")

        elif 'open facebook' in message:
            webbrowser.open ("facebook.com")

        elif 'open stackoverflow' in message:
            webbrowser.open("stackoverflow.com")

        elif 'wikipedia' in message:
            speak('Searching Wikipedia...')
            message = message.replace("wikipedia", "")
            results = wikipedia.summary(message, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif ('the time') in message or ('time') in message or('current time') in message:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")
        
        # elif 'email to Ashish' in message:

        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "yourEmail@gmail.com"    
        #         sendEmail(to, content)
        #         speak("Email has been sent!")

        #     except Exception as e:
        #         print(e)
        #         speak("Sorry Sir. I am not able to send this email") 

        elif message=='AI':
            speak('Yes Sir?', 'What can I doo for you sir?')

        elif ('thanks') in message or ('tanks') in message or ('thank you') in message:
            speak( 'You are wellcome', 'no problem')
        
        elif ('hello') in message or ('hi') in message:
            speak('Wellcome to AI virtual intelligence project. At your service sir.')

        elif ('your name') in message:
            speak('My name is AI, at your service sir')

        elif 'voice' in message:
            if 'female' in message:
                engine.setProperty('voice',voices[1].id)
            else:
                engine.setProperty('voice',vioces[0].id)
            speak("Hello sir, i have switch my voice.how is it")

        elif 'screenshot' in message:
            speak("taking screenshot")
            screenshot()
        
        elif 'cpu' in message:
            cpu()

        elif 'joke' in message:
            joke()
        
        
        
        elif ('goodbye') in message or ('bye') in message:
            speak('Goodbye sir', 'AI is powering off in 3,2,1,0')
            break
        