from tinytag import TinyTag
import os
import csv
import shutil

def createCSV(songsPath, csvFileName):
    songsPathList = []

    for song in os.listdir(songsPath):
        if song.endswith(".mp3") == True:
            songsPathList.append(song)

    if not os.path.exists('male'):
        os.makedirs('male')

    if not os.path.exists('female'):
        os.makedirs('female')

    if not os.path.exists('noGender'):
        os.makedirs('noGender')

    with open(csvFileName, 'w', newline="") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(("File Name", "Title", "Year", "Gender", "Artist", "Duration (minutes)"))
        for song in songsPathList:
            tag = TinyTag.get(songsPath + "/" + song)
            writer.writerow((song, tag.title, tag.year, tag.genre, tag.artist, round(tag.duration/60, 2)))
            if tag.genre == "Male":
                shutil.copy(songsPath + "/" + song, "male")
            if tag.genre == "Female":
                shutil.copy(songsPath + "/" + song, "female")
            if not "Male" or not "Female":
                shutil.copy(songsPath + "/" + song, "noGender")

    print(f'CSV File: {songsPath}/songs.csv')

songsPath = input("Enter songs path: ")

createCSV(songsPath, "songs.csv")