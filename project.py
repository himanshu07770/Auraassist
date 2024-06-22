import subprocess
import wolframalpha
import pyttsx3
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		print("Good Morning Sir !")
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		print("Good Afternoon Sir !")
		speak("Good Afternoon Sir !")

	else:
		print("Good Evening Sir !")
		speak("Good Evening Sir !")

	assname =("Jarvis 1 point o")
	print("I am your Assistant")
	speak("I am your Assistant")
	print(assname)
	speak(assname)
	

def username():
	print("What should i call you sir")
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome Mr.", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you, Sir")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	
	server.login('creaturehackop@gmail.com', 'let@them#Thinkyou&die')
	server.sendmail('creaturehackop@gmail.com', to, content)
	server.close()
if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	
	clear()
	wishMe()
	username()
	
	while True:
		
		query = takeCommand().lower()
		
		
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("google.com")

		elif 'open stackoverflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com")

		elif 'play music' in query or "play song" in query:
			speak("Here you go with music")
			# music_dir = "G:\\Song"
			music_dir = "C:\\Users\\chhim\\Music"
			songs = os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir, songs[0]))

		elif 'time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"Sir, the time is {strTime}")

		

		elif 'email to Himanshu' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				to = "Receiver email address"
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")

		elif 'send a mail' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				speak("whome should i send")
				to = input()
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			assname = query

		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak(assname)
			print("My friends call me", assname)

		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query:
			speak("I have been created by Himanshu.")
			
		elif 'joke' in query or "tell me a joke" in query:
			speak(pyjokes.get_joke())
			
		elif "calculate" in query:
			
			app_id = "5YXJAT-KJVRU4QYLY"
			client = wolframalpha.Client(app_id)
			indx = query.lower().split().index('calculate')
			query = query.split()[indx + 1:]
			res = client.query(' '.join(query))
			answer = next(res.results).text
			print("The answer is " + answer)
			speak("The answer is " + answer)

		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

		elif "who i am" in query or "who am i" in query:
			speak("If you talk then definitely your human.")

		elif "why you came to world" in query:
			speak("Thanks to Himanshu. further It's a secret")

		

		elif 'is love' in query:
			speak("It is 7th sense that destroy all other senses")

		elif "who are you" in query:
			speak("I am your virtual assistant created by Himanshu")

		elif 'reason for you' in query:
			speak("I was created as a Minor project by Mister Himanshu ")

		elif 'change background' in query:
			ctypes.windll.user32.SystemParametersInfoW(20,
													0,
													"Location of wallpaper",
													0)
			speak("Background changed successfully")

		elif 'open 8085' in query:
			appli = r"C:\\Users\\chhim\\Downloads\\8085Compiler.jar"
			os.startfile(appli)

		elif "news" in query:
			speak("Here are some best headline from across the world\n")
			webbrowser.open("bbc.com")

		
		elif 'lock window' in query:
				speak("locking the device")
				ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
				
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop jarvis from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.nl/maps/place/" + location + "")

		elif "camera" in query or "capture photo" in query:
			ec.capture(0, "Jarvis Camera ", "img.jpg")

		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('jarvis.txt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("%H:%M:%S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		elif "show note" in query:
			speak("Showing Notes")
			file = open("jarvis.txt", "r")
			print(file.read())
			speak(file.read())

		
					
		
		elif "jarvis" in query:
			
			wishMe()
			speak("Jarvis 1 point o in your service Mister")
			speak(assname)

		elif "weather" in query:
			speak("Here is weather report of your current location\n")
			webbrowser.open("https://www.tomorrow.io/weather/")
			
		
		elif "wikipedia" in query:
			webbrowser.open("wikipedia.com")

		elif "Good Morning" in query or "morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(assname)

		
		elif "will you be my gf" in query or "will you be my bf" in query:
			speak("I'm not sure about, may be you should give me some time")

		elif "how are you" in query:
			speak("I'm fine, glad you me that")

		elif "i love you" in query:
			speak("It's hard to understand")

		elif "what is" in query or "who is" in query:
			
			
			client = wolframalpha.Client("5YXJAT-KJVRU4QYLY")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")

		

