from tinytag import TinyTag
import os
import csv
import shutil

def createCSV(songsPath, csvFileName):
    songsPathList = []

    for song in os.listdir(songsPath): #Iterate over the songs folder and collect only the ".mp3" files
        if song.endswith(".mp3") == True:
            songsPathList.append(song)

    if not os.path.exists('male'): #Create "male" folder if not exists
        os.makedirs('male')

    if not os.path.exists('female'): #Create "female" folder if not exists
        os.makedirs('female')

    if not os.path.exists('noGender'): #Create "noGender" folder if not exists
        os.makedirs('noGender')

    with open(csvFileName, 'w', newline="") as csvFile: #If not exists create a ".csv" file with the name of csvFileName variable
        writer = csv.writer(csvFile)
        writer.writerow(("File Name", "Title", "Year", "Gender", "Artist", "Duration (minutes)"))
        for song in songsPathList: #Iterate over the songsPathList list, where are stored all the songs names that was found in the first for loop
            tag = TinyTag.get(songsPath + "/" + song)
            writer.writerow((song, tag.title, tag.year, tag.genre, tag.artist, round(tag.duration/60, 2))) #Extract song metadata (e.g. song name, release year, artist name) and put it into CSV file
            
            # ******* Sort songs by gender *******
            
            if tag.genre == "Male":
                shutil.copy(songsPath + "/" + song, "male")
            if tag.genre == "Female":
                shutil.copy(songsPath + "/" + song, "female")
            if not "Male" or not "Female":
                shutil.copy(songsPath + "/" + song, "noGender")
                
            # ******* Sort songs by gender *******    

    print(f'CSV File: {songsPath}/songs.csv') #Print the path of the CSV file

songsPath = input("Enter songs path: ")

createCSV(songsPath, "songs.csv")
