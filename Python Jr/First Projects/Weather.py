import tkinter
import requests

wea = requests.get("https://www.google.com/search?client=opera-gx&q=weather&sourceid=opera&ie=UTF-8&oe=UTF-8")

if wea.status_code == 200:
    print (wea.text)