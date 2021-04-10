
############ IMPLEMENTING WEB SCRAPING USING PYTHON TO PLAY SONGS FROM SOUNDCLOUD #############

from selenium import webdriver
import requests
import bs4
import os
import time


def track():
    name = input(">>>Enter name of track: ")
    print()
    "%20".join(name.split(" "))
    browser.get(track_url + name)

    request = requests.get(track_url+name)
    soup = bs4.BeautifulSoup(request.text, "lxml")
    tracks = soup.select("h2")[3:]

    track_links = []
    track_names = []
    for index, track in enumerate(tracks):
        track_links.append(track.a.get("href"))
        track_names.append(track.text)
        print(str(index+1)+": "+track.text)
        print()

    #song selection loop
    while True:
        choice = input(">>>Enter your choice (x exit) ")
        print()
        if choice == "x":
            break
        else:
            choice = int(choice)-1

        print()
        print("Now playing "+track_names[choice])
        print()

        browser.get("http://soundcloud.com"+track_links[choice])
        play_button = browser.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a")[0]
        time.sleep(0.1)
        play_button.click()


def artist():
    name = input(">>>Enter name of artist: ")
    print()
    "%20".join(name.split(" "))
    browser.get(artist_url + name)

    request = requests.get(artist_url+name)
    soup = bs4.BeautifulSoup(request.text, "lxml")
    tracks = soup.select("h2")[3:]

    track_links = []
    track_names = []
    for index, track in enumerate(tracks):
        track_links.append(track.a.get("href"))
        track_names.append(track.text)
        print(str(index+1)+": "+track.text)
        print()

    #song selection loop
    while True:
        choice = input(">>>Input your choice (x to exit) ")
        print()
        if choice == "x":
            break
        else:
            choice = int(choice)-1
        print()
        browser.get("http://soundcloud.com"+track_links[choice])


def mix():
    name = input(">>>Enter name of mix: ")
    print()
    "%20".join(name.split(" "))
    browser.get(artist_url + name + mix_url_end)

    request = requests.get(artist_url + name + mix_url_end)
    soup = bs4.BeautifulSoup(request.text, "lxml")
    tracks = soup.select("h2")[3:]

    track_links = []
    track_names = []
    for index, track in enumerate(tracks):
        track_links.append(track.a.get("href"))
        track_names.append(track.text)
        print(str(index+1)+": "+track.text)
        print()

    #song selection loop
    while True:
        choice = input(">>>Your choice (x to exit)")
        print()
        if choice == "x":
            break
        else:
            choice = int(choice)-1

        print(">>>Now playing "+track_names[choice])
        print()

        browser.get("http://soundcloud.com"+track_links[choice])
        play_button = browser.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a")[0]
        time.sleep(0.1)
        play_button.click()


def top_charts():
    request = requests.get(top_url)
    soup = bs4.BeautifulSoup(request.text, "lxml")
    print(">>>GENRES AVAILABLE: ")
    print()
    while True:

        genres = soup.select("a[href*=genre]")[2:]
        genre_links = []

        #printing all the available genres
        for index, genre in enumerate(genres):
            print(str(index+1)+": "+genre.text)
            genre_links.append(genre.get("href"))
            print()

        print()
        choice = input(">>>YOUR CHOICE (x to exit)")
        print()

        if choice == "x":
            break
        else:
            choice = int(choice)-1

        url = "https://soundcloud.com" + genre_links[choice]
        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.text,"lxml")

        tracks = soup.select("h2")[3:]

        track_links = []
        track_names = []

        for index, track in enumerate(tracks):
            track_links.append(track.a.get("href"))
            track_names.append(track.text)
            print(str(index+1)+": "+track.text)
            print()

        #song selection loop
        while True:
            choice = input(">>>Input your choice (x to reselect a newgenre)")
            print()
            if choice == "x":
                break
            else:
                choice = int(choice)-1

            print()
            print("Now playing "+track_names[choice])
            print()

            browser.get("http://soundcloud.com"+track_links[choice])
            play_button = browser.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a")[0]
            time.sleep(0.1)
            play_button.click()


def new_hot():
    request = requests.get(new_url)
    soup = bs4.BeautifulSoup(request.text, "lxml")
    print("GENRES AVAILABLE: ")
    print()
    while True:

        genres = soup.select("a[href*=genre]")[2:]
        genre_links = []

        #printing all the available genres
        for index, genre in enumerate(genres):
            print(str(index+1)+": "+genre.text)
            genre_links.append(genre.get("href"))
            print()

        print()
        choice = input(">>>Input your choice (x to exit)")
        print()

        if choice == "x":
            break
        else:
            choice = int(choice)-1

        url = "https://soundcloud.com" + genre_links[choice]
        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.text,"lxml")
        
        tracks = soup.select("h2")[3:]

        track_links = []
        track_names = []

        for index, track in enumerate(tracks):
            track_links.append(track.a.get("href"))
            track_names.append(track.text)
            print(str(index+1)+": "+track.text)
            print()

        #song selection loop
        while True:
            choice = input(">>> Input Your choice (x to reselect a newgenre)")
            print()
            if choice == "x":
                break
            else:
                choice = int(choice)-1

            print()
            print("Now playing "+track_names[choice])
            print()

            browser.get("http://soundcloud.com"+track_links[choice])
            play_button = browser.find_elements_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a")[0]
            time.sleep(0.1)
            play_button.click()

# new, top, mix, track and artist urls
top_url = "http://soundcloud.com/charts/top"
new_url = "http://soundcloud.com/charts/new"
track_url = "http://soundcloud.com/search/sounds?q="
artist_url = "http://soundcloud.com/search/people?q="
mix_url_end = "&filer.duration=epic"

# creating the selenium browser
browser = webdriver.Chrome("D:\Ashutosh\Project\chromedriver.exe")
browser.get("https://soundcloud.com")

#main menu
print()
print("Welcome to the python soundcloud scraper")
print("Explore top genres")
print("Search for tracks, artists or mixes")
print()

while True:
    print(">>>Menu:")
    print(">>>1.Search for track")
    print(">>>2.Search for artist")
    print(">>>3.Search for mix")
    print(">>>4.Top charts")
    print(">>>5.New Hot Charts")
    print(">>>0.Exit")
    print()

    choice = int(input(">>>Your choice "))

    if choice == 0:
        browser.quit()
        break
    print()

    #SEARCH FOR TRACK
    if choice == 1:
        track()
        continue
    
    #SEARCH FOR ARTIST
    if choice == 2:
        artist()
        continue

    #SEARCH FOR MIX
    if choice == 3:
        mix()
        continue
 
    #TOP CHARTS
    if choice == 4:
        top_charts()
        continue
    
    #NEW HOT
    if choice == 5:
        new_hot()
        continue


print()
print("GOODBYE!!")



