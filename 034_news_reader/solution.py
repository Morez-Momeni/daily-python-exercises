"""
Problem #34: News Reader with Text-to-Speech
Date: 2026-08-27

This script fetches top news articles from News API and reads each title aloud
using text-to-speech. It demonstrates working with REST APIs, JSON parsing,
and basic TTS functionality.
"""

import requests
import json
import pyttsx3 

def speak(text : str):
    engine = pyttsx3.init()
    try: 
        engine.say(text)
        engine.runAndWait()
    except KeyboardInterrupt:
        engine.stop()



url = "https://newsapi.org/v2/everything?q=apple&from=2026-08-26&to=2026-08-26&sortBy=popularity&apiKey=9187d5778c864deba8e0e7075df05f86"

news = requests.get(url).text
news = json.loads(news)
print(news["totalResults"])


arts = news["articles"]

for article in arts:
    print(article['title'])
    speak(article['title'])


