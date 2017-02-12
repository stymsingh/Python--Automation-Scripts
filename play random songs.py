import webbrowser
import time
import random

def func():
    text = "https://www.youtube.com/watch?v=60ItHLz5WEA  https://www.youtube.com/watch?v=UW5tV299bc0  https://www.youtube.com/watch?v=Czi8NlmuEXs"
    songs = text.split()
    while(1):
        webbrowser.open(songs[random.randint(1,len(songs))])
        time.sleep(1000)

func()
