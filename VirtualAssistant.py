#First basic step is speech to text
import speech_recognition as sr
import playsound
from gtts import gTTS
import os
from time import ctime
import re
import webbrowser
import smtplib

#To make sure it listens
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening")
        audio = r.listen(source,phrase_time_limit = 5)
    data = ""
# #Exception Handling
    try:
        data = r.recognize_google(audio,language = 'en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data
#listen()
#Responding
basepath = os.path.dirname(__file__)

def respond(String):
    print(String)
    tts = gTTS(text = String,lang ='en')
    tts.save('speech.mp3')
    path = os.path.join(basepath,'speech.mp3')
    playsound.playsound(path)
    os.remove(path)

#Virtual Assistant Actions
def virtual_assistant(data):
    """give your actions"""
    if "how are you" in data:
        listening = True
        result = "Good and doing well"
        respond("Good and doing well")

    elif "time" in data:
        listening = True
        result = ctime()
        respond(ctime())

    elif "open google" in data.casefold():
        listening = True
        reg_ex = re.search('open google(.*)',data)
        url = "https://www.google.com/"
        if reg_ex:
            sub = reg_ex.group(1)
            url = url + 'r/'
        webbrowser.open(url)
        result = "Success"
        respond("Success")

    elif "email" in data:
        listening = True
        respond("Whom should i send email to?")
        to = listen()
        edict = {'hello':'sakethreddy.kallepu@gmail.com',
                 'new':'saketh@codegnan.com'}
        toaddr = edict[to]
        respond("What is the Subject?")
        subject = listen()
        respond("What should i tell that person?")
        message = listen()
        content = 'Subject :{}\n\n{}'.format(subject,message)
        #init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com',587)
        #identify the server
        mail.ehlo()
        mail.starttls()
        #login
        mail.login('sakethreddy.kallepu@gmail.com','') #enter mailid and password make sure you enable less secure app access
        mail.sendmail('sakethreddy.kallepu@gmail.com',toaddr,content)
        mail.close()
        result = "Email Sent"
        respond('Email Sent')

    elif "locate" in data:
        webbrowser.open('https://www.google.com/maps/search/'+data.replace("locate",""))
        result = "Located"
        respond("Located {}".format(data.replace("locate","")))

    elif "wiki" in data.casefold():
        listening = True
        respond("What should i Search")
        query = listen()
        response = requests.get('https://en.wikipedia.org/wiki/'+query)
        if response is not None:
            html = bs4.BeautifulSoup(response.text,'html.parser')
            paragraphs = html.select('p')
            intro = [i.text for i in paragraphs]
            halo =' '.join(intro)
        #result = "Extracted"
        respond(halo[:100])

    elif "word" in data.casefold(): #same you can link for other shortcuts
        listening = True
        os.startfile(r'C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE')
        result = "Success"
        respond("Success")

    elif "youtube" in data.casefold():
        listening = True
        reg_ex = re.search('youtube(.*)',data.casefold())
        print(data)
        url = "https://www.youtube.com/search?q="
        if reg_ex:
            sub = reg_ex.group(1)
        webbrowser.open(url + sub)
        respond("Success")
        result = "YouTube done"

    elif "search google" in data.casefold():
        listening = True
        reg_ex = re.search('search google(.*)',data.casefold())
        print(data)
        url = "https://www.google.com/search?q="
        if reg_ex:
            sub = reg_ex.group(1)
            print(sub,type(sub))
        webbrowser.open(url + sub)
        result = "Success"
        respond("Search for {} complete".format(sub))
    #try:
         #return listening
    #except UnboundLocalError:
       #print("Timedout..") 
    return result

    if "stop" in data:
        listening = False
        result = "GBTC"
        print("Listening Stopped")
        respond("Take Rest..take care...")
  
#time.sleep(2)
# respond("Hey Saketh how are you?")
# listening = True
# while listening == True:
#     data = listen()
#     listening = virtual_assistant(data)
    
    







